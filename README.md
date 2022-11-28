# deepsecurity-docker
This repository holds Dockerfiles that can be used to either create easily reproducible execution environments for automation, or can be deployed to AWS Lambda for Serverless use of the [Trend Micro Deep Security Python SDK](https://automation.deepsecurity.trendmicro.com/article/20_0/python/ "Trend Micro Deep Security Python SDK"). 

Due to the difference in how Lambda functions using Docker images need to be set up, you will find two different Dockerfiles, one in the "Local" directory, and the other in the "Lambda" directory. 

**Steps to use the "Local" variant:**
1. Download [Docker Desktop](https://www.docker.com/products/docker-desktop/ "Docker Desktop") or otherwise configure Docker using one of the many online guides. 

2. Copy this Repo to your machine. 

3. Within the downloaded repo's "Local" directory, run:

`docker build example-name/ds-docker .`

4. Create a 'keyfile.config' file within your current directory. That file needs to have the following lines:

`trend_host= https://DSM-FQDN.com`

`trend_api_key= ABC123`

5. Use the following command to supply the config file to the Docker container at runtime and run whatever logic/code you may have added to main.py. 

`docker run -ti --rm --volume ${pwd}:/ds-docker/config example-name/ds-docker`

*Note:* the above command is for running on a Windows machine.

**Steps to use the "Lambda" variant:**
1. Download [Docker Desktop](https://www.docker.com/products/docker-desktop/ "Docker Desktop") or otherwise configure Docker using one of the many online guides. 

2. Copy this Repo to your machine. 

3. Within the downloaded repo's "Lambda" directory, run:

`docker build example-name/ds-lambda .`

4. Create an Amazon ECR repo for deploying the docker image to. 

5. Run the following command to tag the docker image, replacing the ECR location with your own:

`docker tag example-name/ds-lambda 123456789123.dkr.ecr.us-east-1.amazonaws.com/repo-name:latest`

6. Push your Docker image up to the ECR repository using instructions found on the AWS console. 

7. Create an AWS Lambda function, using the Docker Image you've pushed to the repository after modification. 
