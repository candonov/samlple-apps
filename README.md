# samlple-apps

Steps to build an image and push to docker hub:
```
cd s3-demo-app
docker build -t candonov/s3-demo-app:latest
docker login
docker push candonov/s3-demo-app:latest
```
Image is located at [docker hub](https://hub.docker.com/r/candonov/s3-demo-app)

To use:
```
docker pull candonov/s3-demo-app
```
