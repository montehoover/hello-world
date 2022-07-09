# Using GPUs with Docker

On WSL, it works right out of the box. Not sure about vanilla Ubuntu.
1. Run docker as normal and add `--gpus=all` for Docker to access the GPU. Ex:
    ```
    $ docker run --rm --gpus=all pytorch/pytorch:1.11.0-cuda11.3-cudnn8-devel nvidia-smi -L
    GPU 0: NVIDIA GeForce RTX 2080 Ti
    ```

If you get an error about nvidia-smi not being found then apt install `nvidia-docker2`.
1. Setup the package repository and the GPG key:
    ```
    distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
      && curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
      && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
            sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
            sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
    ```
2. Apt install `nvidia-docker2`:
    ```
    sudo apt-get update && sudo apt-get install -y nvidia-docker2
    ```

## Official instructions

There is not a great central starting point for instructions on how to use GPUs with Docker. Docker's site has [something](https://docs.docker.com/config/containers/resource_constraints/#gpu), Nvidia's site has a [smattering](https://docs.nvidia.com/ai-enterprise/deployment-guide/dg-docker.html) [of](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#install-guide) [things](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch), and you'll see three conflicting instructions:
1. Install `nvidia-docker2` and run your GPU container.
2. Install `nvidia-container-toolkit` and run your GPU container.
3. Install `nvidia-container-runtime` and run your GPU container.
There's a full explanation [here](https://github.com/NVIDIA/nvidia-docker/issues/1268), but the bottom line is that you probably only need `nvidia-container-toolkit` but `nvidia-container-runtime` is needed for Kubernetes and for earlier Docker versions, and `nvidia-docker2` contains both so it should just be your default.



## GPU-enabled docker images:
1. nvcr.io/nvidia/pytorch:22.03-py3                         https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch
2. nvcr.io/nvidia/cuda:11.6.2-cudnn8-runtime-ubuntu20.04    https://catalog.ngc.nvidia.com/orgs/nvidia/containers/cuda
3. pytorch/pytorch:1.11.0-cuda11.3-cudnn8-devel             https://hub.docker.com/r/pytorch/pytorch/tags
4. pytorch/manylinux-cuda116                                https://hub.docker.com/r/pytorch/manylinux-cuda116/tags 

Repo of dockerfiles from Nvidia, probably not helpful though:
https://gitlab.com/nvidia/container-images

Maybe the best example dockerfile: https://github.com/pytorch/elastic/blob/master/examples/Dockerfile
