# PythonLambdaDockerECR
PythonLambdaDockerECR

* Learn how to run lambda on docker container and deploy Base image on ECR and use on Lambda 

#### Commands 
```
docker build -t docker-python-lambda .

docker run -p 9000:8080 docker-python-lambda:latest

curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d "{\"msg\":\"hello\"}"

```
