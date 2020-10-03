# Docker

## Dockerfile

[](https://www.ctl.io/developers/blog/post/dockerfile-entrypoint-vs-cmd/)

[Best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

## Build
docker build --rm --tag sentiment-analysis-logic:1.0 .

`--rm Remove intermediate containers after a successful build (default true)`

## Run
docker run --publish 80:80 --detach --name sa sentiment-analysis-frontend:1.0

## Stop

### Stop all containers
docker stop $(docker ps -a -q)


## Multi-stage builds
[](https://docs.docker.com/develop/develop-images/multistage-build/)

## Inspect
The docker exec command is probably what you are looking for; this will let you run arbitrary commands inside an existing container.
docker exec -it sa-logic bash

## Clean up

### Dangling images
docker images -f "dangling=true" -q
docker rmi $(docker images -f "dangling=true" -q)
docker image prune

## Docker Compose

### Installation
Install required packages
sudo apt update
sudo apt install -y python3-pip libffi-dev

Install Docker Compose from pip (using Python3), possibly inside a virtual environment:
pip3 install docker-compose

[](https://www.baeldung.com/docker-compose)
[](https://docs.docker.com/compose/gettingstarted/)
Compose file version 3 [reference](https://docs.docker.com/compose/compose-file/)

### Workflow

docker-compose up

docker-compose logs -f sa-logic
