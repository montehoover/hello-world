# Run GUI apps from Docker container

## Option 1. Using Xauth

1. Create the following Dockerfile:
    ```
    FROM ubuntu:20.04

    RUN : \
        && apt-get update \
        && apt-get install -y \
            firefox
            xauth
    ```
2. Build it:
    ```
    docker built -t gui .
    ```
3. Copy the xauth cookie from your desktop so you can paste it in step 5.
    ```
    $ xauth list
    monte/unix:  MIT-MAGIC-COOKIE-1  ae2ce802ac69befa09e29ed7908fc298
    ```
4. Run the container. Pass it the DISPLAY environment variable and tell it to use network driver of the host:
    ```
    docker run -it --env=DISPLAY --net=host gui
    ```
5. Use `xauth add` to add the xauth cookie to the container that you copied from your desktop. Note that you have to add a 0 after the colon in `<user>/unix:`. If all it displays is the "file does not exist" message then it was successful.
    ```
    root@monte:/# xauth add monte/unix:0  MIT-MAGIC-COOKIE-1  ae2ce802ac69befa09e29ed7908fc298
    xauth:  file /root/.Xauthority does not exist
    ```
6. Run `firefox` to show that it's working:
    ```
    root@monte:/# firefox
    ```

