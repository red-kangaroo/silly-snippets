/**
 * Simple CUDA application template.
 */
#include <stdio.h>
#include <stdlib.h>
#include <cuda.h>
#include <cuda_runtime.h>
#include <iostream>

/**
 * This macro checks return value of the CUDA runtime call and exits
 * the application if the call failed.
 */
#define CUDA_CHECK_RETURN( value ) {							\
	cudaError_t err = value;									\
	if( err != cudaSuccess ) {									\
		fprintf( stderr, "Error %s at line %d in file %s\n",	\
				cudaGetErrorString(err), __LINE__, __FILE__ );	\
		exit( 1 );												\
	} }

#define MATRIX_SIZE 10
#define BLOCK_SIZE 2

struct Matrix{
    int width;
    int height;
    float *cell;
};


__global__ void matrixMult(Matrix A, Matrix B, Matrix C){
  int row = blockIdx.y * blockDim.y + threadIdx.y;
  int col = blockIdx.x * blockDim.x + threadIdx.x;

  float val = 0;
//   printf("Row: %d  Col: %d\n", row, col);

  if (row < A.width && col < A.height){
      for(int i = 0; i < A.width; i++){
        val += A.cell[row * A.width + i] * B.cell[i * B.width + col];
//         printf(" Val: %f ", val);
        C.cell[row * C.width + col] = val;
      }
//       printf("\n");
  }
}


int main(int argc, char **argv) {
  // Alloc:
  struct Matrix A = {
    MATRIX_SIZE,
    MATRIX_SIZE,
    NULL
  };
  struct Matrix B = {
    MATRIX_SIZE,
    MATRIX_SIZE,
    NULL
  };
  struct Matrix C = {
    MATRIX_SIZE,
    MATRIX_SIZE,
    NULL
  };

  float *in_A = new float[A.width * A.height];
  for(int i = 0; i < A.width * A.height; i++){
    in_A[i] = i + 1;
  }

  float *in_B = new float[B.width * B.height];
  for(int i=0; i < B.width * B.height; i++){
    in_B[i] = i + 1;
  }

  float *out_C = new float[C.width * C.height];

  CUDA_CHECK_RETURN(cudaMalloc(&A.cell, sizeof(float) * A.width * A.height));
  CUDA_CHECK_RETURN(cudaMalloc(&B.cell, sizeof(float) * B.width * B.height));
  CUDA_CHECK_RETURN(cudaMalloc(&C.cell, sizeof(float) * C.width * C.height));

  CUDA_CHECK_RETURN(cudaMemcpy(A.cell, in_A, sizeof(float) * A.width * A.height, cudaMemcpyHostToDevice));
  CUDA_CHECK_RETURN(cudaMemcpy(B.cell, in_B, sizeof(float) * B.width * B.height, cudaMemcpyHostToDevice));

  dim3 dimBlock(BLOCK_SIZE, BLOCK_SIZE);
  dim3 dimGrid((C.width + dimBlock.x - 1) / dimBlock.x, (C.height + dimBlock.y - 1) / dimBlock.y);

  matrixMult<<<dimGrid, dimBlock>>>(A, B, C);
  CUDA_CHECK_RETURN(cudaDeviceSynchronize());
  CUDA_CHECK_RETURN(cudaMemcpy(out_C, C.cell, sizeof(float) * C.width * C.height, cudaMemcpyDeviceToHost));

  /*for(int r = 0; r < C.height; ++r){
    for(int c = 0; c < C.width; ++c){
      printf("%d  ", out_C[r * C.width + c]);
    }
    printf("\n");
  }*/

  CUDA_CHECK_RETURN(cudaFree(A.cell));
  CUDA_CHECK_RETURN(cudaFree(B.cell));
  CUDA_CHECK_RETURN(cudaFree(C.cell));

  delete [] in_A;
  delete [] in_B;
  delete [] out_C;

  return 0;
}
