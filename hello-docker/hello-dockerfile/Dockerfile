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
