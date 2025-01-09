## Advent of code in python year 2023

Using this repo to test out Jenkins as well as a CI/CD platform

- create a docker network. We will call ours jenkins
```
docker network create jenkins
```
- Run Jenkins Image in Docker

```bash
docker run -p 8080:8080 -p 50000:50000 --network jenkins --restart=on-failure jenkins/jenkins:lts-jdk17
```

- Install Docker Plugin
- Install Blue Ocean Plugin (optional)

---

Running an Jenkins Agent in a seperate docker container

```
docker run -d --restart=always -p 127.0.0.1:2376:2375 --network jenkins -v /var/run/docker.sock:/var/run/docker.sock alpine/socat tcp-listen:2375,fork,reuseaddr unix-connect:/var/run/docker.sock
```


