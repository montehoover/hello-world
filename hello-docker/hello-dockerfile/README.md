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

2. In the same directory, run:
```
$ docker build -t getting-started .
[+] Building 19.2s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                                                                            0.1s
...
 => => naming to docker.io/library/getting-started                                                                              0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
~/code/hello-world/hello-docker/hellod-dockerfile/app
$
```
