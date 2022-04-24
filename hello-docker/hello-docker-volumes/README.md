# Docker Volumes

Based on the tutorial from https://docs.docker.com/get-started/02_our_app/. Using a simple Node.js app for creating a to-do list, this goes through the steps of creating a space on your hard drive where the sqlite database can get stored and reused by future container instances.

1. Cd into the app folder and notice the source files, the `package.json` dependencies list, the `yarn.lock`, and the `Dockerfile` that together make a working Node.js app.
    ```
    $ cd app/
    ~/code/hello-world/hello-docker/hello-docker-volumes/app
    $ ls
    Dockerfile  package.json  spec  src  yarn.lock
    ```

2. Build a docker image for this app:
    ```
    $ docker build -t todo-app .
    [+] Building 17.7s (11/11) FINISHED                                                                                                                                                                                              
    => [internal] load build definition from Dockerfile         0.0s
    ...                                                                                                                            
    ~/code/hello-world/hello-docker/hello-docker-volumes/app
    $ docker image ls
    REPOSITORY                     TAG                                        IMAGE ID       CREATED          SIZE
    todo-app                       latest                                     45489d9de354   20 seconds ago   404MB
    ```
    Note: You can run the app with `docker run -dp 3000:3000 todo-app`, add a todo list item, delete the container and start it again to see that items are not persisted after a container.

3. Create a "volume", or the space on the local hard drive where data will be stored:
    ```
    $ docker volume create todo-db
    todo-db
    ~/code/hello-world
    $ docker volume ls
    DRIVER    VOLUME NAME
    local     todo-db
    ```

4. Now run the app and have the volume from our local hard drive mounted in the container filesystem at the location where it stores the sqlite database. Thus any changes to the database when running the app are actually written to the local hard drive instead of the container filesystem which gets thrown away. If you look at `app/src/persistence/persistence/sqlite.js` line 3 you'll see that the database is stored at `/etc/todos/todo.db`. So we want to link our volume to `/etc/todos`. Run a new instance of the app with this volume linked:
    ```
    $ docker run -dp 3000:3000 -v todo-db:/etc/todos todo-app
    9e4fd4fc76ef9cf3e1989c2a9b34c06d973edfd17b3ba1ef7f2353254f35fd33
    ```



