# This is from Shuhong Chen for running RAFT on some specialized animation stuff



# pytorch
FROM pytorch/pytorch:1.8.0-cuda11.1-cudnn8-devel

# basic os dependencies
RUN apt-get update && apt-get install -y \
        software-properties-common \
    && add-apt-repository universe \
    && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
        curl vim git zip unzip unrar p7zip-full wget \
        apache2 openssl libssl-dev \
        mysql-client mysql-server libmysqlclient-dev \
        ffmpeg libgl1-mesa-glx libsm6 libxext6 libxrender-dev libx11-xcb1 \
        mesa-utils xauth xorg openbox xvfb

# enable nvidia driver
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility,graphics,video

# basic python
RUN conda install \
    'matplotlib==3.3.4' \
    'pandas==1.2.4' \
    'scipy==1.6.2' \
&& pip install \
    'flask==2.0.0' \
    'mysql-connector-python==8.0.25' \
    'mysqlclient==2.0.3' \
    'patool==1.12' \
    'pyunpack==0.2.2'

# computer vision + graphics
RUN conda install \
    'scikit-image==0.18.1' \
&& pip install \
    'opencv-python==4.5.2.52' \
    'kornia==0.5.2' \
    'pygltflib==1.14.4' \
&& conda install -c conda-forge \
    'scikit-learn==0.23.2' \
    'igl==2.2.1' \
    'meshplot==0.4.0'

# pytorch
RUN conda install -c conda-forge \
    'pytorch-lightning==1.3.8' \
&& pip install \
    'comet_ml==3.9.1' \
    'neptune-client==0.9.9' \
    'wandb==0.10.32'

# jupyterlab
RUN conda install \
    'jupyterlab==3.0.14' \
&& pip install \
    'aquirdturtle-collapsible-headings==3.0.1'


##########################################################################


# sketching
COPY ./autotrace_0.40.0-20190312_ubuntu1804.deb /opt/autotrace/
RUN apt-get update \
        && apt-get install -y \
            libcairo2-dev \
            libjpeg-dev \
            libgif-dev \
            /opt/autotrace/autotrace_0.40.0-20190312_ubuntu1804.deb \
        && rm -r /opt/autotrace \
    && apt-get update \
        && DEBIAN_FRONTEND=noninteractive apt-get install -y \
            libboost-all-dev \
            libopencv-dev \
            libwxgtk3.0-gtk3-dev \
            cmake \
        && cd /opt && git clone https://github.com/SSARCandy/Coherent-Line-Drawing.git \
        && cd /opt/Coherent-Line-Drawing && ./build.sh \
        && ln -s /opt/Coherent-Line-Drawing/build/cld /usr/bin/cld \
    && pip install \
        'svgwrite==1.4.1' \
        'drawSvg==1.8.1'

# dali
RUN pip install \
    --extra-index-url https://developer.download.nvidia.com/compute/redist \
    --upgrade 'nvidia-dali-cuda110==1.3.0'

# detectron2
RUN pip install detectron2 -f \
        https://dl.fbaipublicfiles.com/detectron2/wheels/cu111/torch1.8/index.html


# blender (replace python w/ conda)
COPY ./blender-2.93.2-linux-x64.tar.xz /opt/
RUN tar -xf /opt/blender-2.93.2-linux-x64.tar.xz -C /opt/ \
    && rm /opt/blender-2.93.2-linux-x64.tar.xz \
    && ln -s /opt/blender-2.93.2-linux-x64/blender /usr/bin/blender \
    && rm -r /opt/blender-2.93.2-linux-x64/2.93/python \
    && conda create -n blender python=3.9 \
    && ln -s /opt/conda/envs/blender /opt/blender-2.93.2-linux-x64/2.93/python

# blender mmd_tools
# wget https://github.com/powroupi/blender_mmd_tools/archive/dev_test.zip
COPY ./blender_mmd_tools-dev_test.zip /opt/blender_mmd_tools/
RUN cd /opt/blender_mmd_tools \
    && unzip blender_mmd_tools-dev_test.zip \
    && mv \
        /opt/blender_mmd_tools/blender_mmd_tools-dev_test/mmd_tools/ \
        /opt/blender-2.93.2-linux-x64/2.93/scripts/addons/ \
    && cd / && rm -r /opt/blender_mmd_tools

# blender python installs
RUN conda install -n blender \
    'numpy==1.20.3'

# cupy (for softsplat)
RUN pip install \
    'cupy-cuda111==9.4.0'

# get imagesize w/out opening
RUN pip install \
    'imagesize==1.2.0'

# more opencv
RUN pip install \
    'opencv-contrib-python==4.5.3.56'

# lpips
RUN pip install \
    'lpips==0.1.4'

# correlation cuda
COPY ./correlation_package/ /opt/correlation_package/
RUN cd /opt/correlation_package && python3 setup.py install && cd /

# webp support
RUN apt-get install -y libwebp-dev \
    && conda install 'pillow==8.4.0'


##########################################################################


# # cleanup
# RUN rm -rf /root/.cache/pip \
#     && rm -rf /var/lib/apt/lists/* \
#     && conda clean -a




