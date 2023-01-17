/**
 * Simple CUDA application template.
 */
#include <stdio.h>
#include <stdlib.h>
#include <cuda.h>
#include <cuda_runtime.h>
#include <iostream>
//#include <chrono>

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

#define VECTOR_SIZE 256
#define BLOCK_SIZE 64

__global__ void vectorSum(int *A, int *B, int *C, int length){
	int i = blockDim.x * blockIdx.x + threadIdx.x;
	if(i < length)
		C[i] = A[i] + B[i];
}


int main(int argc, char **argv) {
  //auto time_start = std::chrono::steady_clock::now();

  // Alloc:
  int *d_A = NULL, *d_B = NULL, *d_C = NULL;
  int *h_A = NULL, *h_B = NULL, *h_C = NULL;

  h_A = (int*)malloc(sizeof(int) * VECTOR_SIZE);
  h_B = (int*)malloc(sizeof(int) * VECTOR_SIZE);
  h_C = (int*)malloc(sizeof(int) * VECTOR_SIZE);

  for(int i = 0; i < VECTOR_SIZE; ++i) {
    h_A[i] = i;
    h_B[i] = i;
    h_C[i] = 0; // Because output.
  }

  CUDA_CHECK_RETURN(cudaMalloc(&d_A, sizeof(int) * VECTOR_SIZE));
  CUDA_CHECK_RETURN(cudaMalloc(&d_B, sizeof(int) * VECTOR_SIZE));
  CUDA_CHECK_RETURN(cudaMalloc(&d_C, sizeof(int) * VECTOR_SIZE));

  CUDA_CHECK_RETURN(cudaMemcpy(d_A, h_A, sizeof(int) * VECTOR_SIZE, cudaMemcpyHostToDevice));
  CUDA_CHECK_RETURN(cudaMemcpy(d_B, h_B, sizeof(int) * VECTOR_SIZE, cudaMemcpyHostToDevice));

  int GRID_SIZE = (VECTOR_SIZE + BLOCK_SIZE - 1) / BLOCK_SIZE;
  vectorSum<<<GRID_SIZE, BLOCK_SIZE>>>(d_A, d_B, d_C, VECTOR_SIZE);

  // Await:
  CUDA_CHECK_RETURN(cudaDeviceSynchronize());
  CUDA_CHECK_RETURN(cudaMemcpy(h_C, d_C, sizeof(int) * VECTOR_SIZE, cudaMemcpyDeviceToHost));

  for(int i = 0; i < VECTOR_SIZE; i++)
  {
    printf("Inputs: %d, %d  Output: %d\n", h_A[i], h_B[i], h_C[i]);
  }

  // Free all:
  free(h_A);
  free(h_B);
  free(h_C);
  CUDA_CHECK_RETURN(cudaFree(d_A));
  CUDA_CHECK_RETURN(cudaFree(d_B));
  CUDA_CHECK_RETURN(cudaFree(d_C));

  //auto time_end = std::chrono::steady_clock::now();
  //std::chrono::duration<double> time_total = time_end - time_start;
  //printf("Elapsed seconds: %d\n", time_total.count());

  return 0;
}
