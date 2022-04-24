# Base image
FROM node:12-alpine
# Run a bash command to install system dependencies
# Adding build tools to make yarn install work on Apple silicon / arm64 machines
RUN apk add --no-cache python2 g++ make
# Create the following directory in the docker image and cd into it for future commands
WORKDIR /app
# Copy from pwd on host machine (first dot) into pwd in image (second dot)
COPY . .
# Run a bash command during the image build process
RUN yarn install --production
# The bash command to run once the container starts
CMD ["node", "src/index.js"]
