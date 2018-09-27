# Example Api2 Project #

This is a small example that uses Python and Flask to provision a simple REST api. It uses the Tox build system and Pytest for running tests.

The api will listen for requests on **port 8080**. Note that this is the port number that the build pipelines will use when defining the ECS tasks and load balancer rules. Changing the api to use a different port will result in incorrect deployment of the resulting container.

It will respond to the following requests:

- /
- /systeminfo
- /systeminfo?detail=all
- /systeminfo?detail=properties
- /systeminfo?detail=environment

Note that the `systeminfo` requests can return detailed Python system property and environment variable information. Care should to taken to ensure this is only deployed for development purposes.

## Local Execution ##
To enable this Python and PIP need to be installed and configured. The Dockerfile specifies Python version 3.6.

To run locally, execute:

```
export FLASK_APP=ccsexampleapi2/main.py
flask run --port=8080
```

This will start the api on port `8080`. The run on a different port, for example `18080` simply change the port number that is specified.

You may wish to use a different port when an application and api are being run locally. See the example application repository, `CCSExampleApp2`.

Now the api is running locally it is possible make requests to it, for example using curl:

`curl http://localhost:8080/`

will return a JSON object like: `{"dateAndTime":"Thursday, 27. September 2018 01:31PM","id":"1c062164-dbb4-40f9-b015-b7798e484ef1"}`.

## Build Pipeline ##
The corresponding example build pipeline project is in the `CCSDevEnvironment` repository as `/terraform/build/api2`. The pipeline currently needs to be stored within the `CCSDevEnvironment` repository because it requires access to various Terraform modules.

## Dockerfile ##
The project includes a simple Docker file, this is used by the build pipeline to generate the container image. It is a standard file for a Python project. It must expose port 8080.

To build the Docker image locally execute:

`docker build -t <image-name> .`

The resulting image can be executed using:

`docker run -p 8080:8080 <image-name>`
