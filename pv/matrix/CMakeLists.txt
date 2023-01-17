cmake_minimum_required(VERSION 3.12)
set(PROJECT_NAME "AK9PV")
project(${PROJECT_NAME})

find_package(CUDA REQUIRED)

set(SOURCES matrixMult.cu)

list(APPEND CMAKE_CXX_FLAGS "-O2 -ffast-math -Wall")
list(APPEND CUDA_NVCC_FLAGS "--compiler-options -fno-strict-aliasing -lineinfo -use_fast_math --ptxas-options -dlcm=cg")
list(APPEND CUDA_NVCC_FLAGS "-gencode arch=compute_35,code=sm_35 -Wno-deprecated-gpu-targets -allow-unsupported-compiler")

cuda_add_executable(${PROJECT_NAME} ${SOURCES})

target_link_libraries(${PROJECT_NAME} /usr/local/cuda-12.0/lib64/libcudart.so)
