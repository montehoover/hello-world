It's not clear what is required to run CUDA/GPUs on docker images. Here are a couple of sets of instructions I was trying to follow:

https://pytorch.org/elastic/0.2.0/examples.html
1. Install [Nvidia Container Toolkit](https://github.com/NVIDIA/nvidia-docker)
2. docker run some-gpu-docker-image (see below)
Note: The pytorch elastic example contains a good dockerfile

https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch
Same as above

https://docs.docker.com/desktop/windows/wsl/#gpu-support
1. Install some beta drivers for WSL2 GPU Paravirtualization
2. docker run some-gpu-docker-image

https://docs.docker.com/config/containers/resource_constraints/#gpu
1. Install nvidia-container-runtime
    1. Add nvidia-container-runtime apt repo (see below)
    2. apt-get install nvidia-container-runtime
2. docker run ubuntu and it will have access to gpus


So far I have simply run nvidia's pytorch image and Cuda worked, and I ran ubuntu and nvidia-smi worked (but it didn't have cuda (nvcc didn't work)). If I run into any problems, my first step will be to install that Nvidia Container Toolkit like they suggested.




## Add nvidia-container-runtime apt repo:
curl -s -L https://nvidia.github.io/nvidia-container-runtime/gpgkey | \
  sudo apt-key add -
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-container-runtime/$distribution/nvidia-container-runtime.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-runtime.list
sudo apt-get update


## GPU-enabled docker images:
1. nvcr.io/nvidia/pytorch:22.03-py3                         https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch
2. nvcr.io/nvidia/cuda:11.6.2-cudnn8-runtime-ubuntu20.04    https://catalog.ngc.nvidia.com/orgs/nvidia/containers/cuda
3. pytorch/pytorch:1.11.0-cuda11.3-cudnn8-devel             https://hub.docker.com/r/pytorch/pytorch/tags
4. pytorch/manylinux-cuda116                                https://hub.docker.com/r/pytorch/manylinux-cuda116/tags 

Repo of dockerfiles from Nvidia, probably not helpful though:
https://gitlab.com/nvidia/container-images

Maybe the best example dockerfile: https://github.com/pytorch/elastic/blob/master/examples/Dockerfile
