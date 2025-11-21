
microservices devOps project with FastAPI, Docker swarm, Github actions CI/CD, and pytest

![CI/CD](https://github/azizchrigui31-bit/devopsfastapi/actions/workflows/ci-cd.yml/badge.svg)

- **users-service**: User managment API (FastAPI + pytest)
- **product-service**: Product catalog
- **order-service**: Order processing 
- **nginx**: Load balancer

'''bash

docker stack deploy -c docker-compose.swarm.yml devopsapp

docker service ls

curl http://localhost/users/
