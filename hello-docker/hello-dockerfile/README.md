# Dockerfiles

1. In the root folder of your project, create a file named `Dockerfile` with no file extention. Add the following lines:
    ```bash
    # Base image to build on top of
    FROM ubuntu:20.04
    # Create a new directory and cd into for future commands
    WORKDIR /new_dir
    # This is a weird convention, but the first dot is pwd (/.../hello_dockerfile) on the host machine and
    # the second dot is pwd in the docker image (/new_dir)
    COPY . .
    # Run any arbitrary bash commands. Note the commands are run as root so you don't have to use sudo
    RUN apt-get update && apt-get install tree -y
    RUN echo "hello from new.txt" > new.txt
    # The bash command to run when the container is launched
    CMD pwd && tree && cat hello.txt && cat new.txt

    ```

2. In the same directory, run the following command to build an image from the instructions in `Dockerfile` and name the image `hello-dockerfile`:
    ```
    $ docker build -t hello-dockerfile .
    [+] Building 6.8s (10/10) FINISHED
    => [internal] load build definition from Dockerfile                                                                            0.0s
    ...
    => => naming to docker.io/library/hello-dockerfile                                                                             0.0s

    Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
    ~/code/hello-world/hello-docker/hellod-dockerfile/app
    $
    ```

3. List the docker images that are present locally and you will see the image `hello-dockerfile` that you just made:
    ```
    $ docker image ls
    REPOSITORY               TAG       IMAGE ID       CREATED        SIZE
    hello-dockerfile         latest    32b1341bb6b4   2 hours ago    404MB
    ubuntu                   latest    3f4714ee068a   2 days ago     77.8MB
    docker/getting-started   latest    cb90f98fd791   12 days ago    28.8MB
    hello-world              latest    feb5d9fea6a5   7 months ago   13.3kB
    ```

4. Now you can run a container based on that image:
    ```
    $ docker run hello-dockerfile
    /new_dir
    .
    |-- Dockerfile
    |-- README.md
    |-- hello.txt
    `-- new.txt

    0 directories, 4 files
    hello world
    hello from new.txt
    ```

5. Push the image to Docker Hub:
    1. First create a repo for the image on Docker Hub:
        1. Go to https://hub.docker.com and sign up/log in.
        2. Click the Create Repository button.
        3. For the repo name, use hello-dockerfile. Make sure the Visibility is Public.
        4. Click the Create button.
    2. Rename your image with your Docker Hub username at the root so that it will go to the right place when you push it:
        ```
        $ docker tag hello-dockerfile montehoover/hello-dockerfile
        ```
    3. Notice the new image name:
        ```
        $ docker image ls
        REPOSITORY                     TAG       IMAGE ID       CREATED        SIZE
        hello-dockerfile               latest    32b1341bb6b4   2 hours ago    404MB
        montehoover/hello-dockerfile   latest    32b1341bb6b4   2 hours ago    404MB
        ubuntu                         latest    3f4714ee068a   2 days ago     77.8MB
        docker/getting-started         latest    cb90f98fd791   12 days ago    28.8MB
        hello-world                    latest    feb5d9fea6a5   7 months ago   13.3kB
        ```
    4. Login to Docker Hub through the terminal to save your credentials and be able to push the imeage to your account:
        ```
        $ docker login -u montehoover
        Password:
        Login Succeeded
        ```
    5. Now push the image:
        ```
        $ docker push montehoover/hello-dockerfile
        Using default tag: latest
        The push refers to repository [docker.io/montehoover/hello-dockerfile]
        f35bc8126b9e: Pushed
        ...
        4fc242d58285: Mounted from library/node
        latest: digest: sha256:7bfcda82400bca73764bce3ded066a562569ffad68924af2b789c538b51274bc size: 2000
        ```

6. For how to add link a container to local files, see [hello-docker-volumes](../hello-docker-volumes/README.md).
    