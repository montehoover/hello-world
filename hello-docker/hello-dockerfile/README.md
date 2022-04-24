# Dockerfiles

1. In the root folder of your project, create a file named `Dockerfile` with no file extention. Add the following lines:
    ```
    FROM node:12-alpine
    # Adding build tools to make yarn install work on Apple silicon / arm64 machines
    RUN apk add --no-cache python2 g++ make
    WORKDIR /app
    COPY . .
    RUN yarn install --production
    CMD ["node", "src/index.js"]
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

3. List the docker images that are present locally and you will see the image `getting-started` that you 
    ```
    $ docker image ls
    REPOSITORY               TAG       IMAGE ID       CREATED        SIZE
    hello-dockerfile         latest    32b1341bb6b4   2 hours ago    404MB
    ubuntu                   latest    3f4714ee068a   2 days ago     77.8MB
    docker/getting-started   latest    cb90f98fd791   12 days ago    28.8MB
    hello-world              latest    feb5d9fea6a5   7 months ago   13.3kB
    ```

4. Now you can run a container based on the image you created:
    ```
    $ docker run -dp 3000:3000 hello-dockerfile
    b2bcbec33aa5bdc78badae655584a2660e9785da216170fc52f46f0a42811599
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
    