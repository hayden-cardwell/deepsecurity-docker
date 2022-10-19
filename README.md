# deepsecurity-docker
Easily create a Docker image that will download and configure the [Trend Micro Deep Security Python SDK](https://automation.deepsecurity.trendmicro.com/article/20_0/python/ "Trend Micro Deep Security Python SDK"), and run scripts in a quick and easy fashion. 

Steps to use:
1. Download [Docker Desktop](https://www.docker.com/products/docker-desktop/ "Docker Desktop") or otherwise configure Docker using one of the many online guides. 

2. Copy this Repo to your machine. 

3. Within the downloaded repo's directory, run:

`docker build example-name/ds-docker .`

4. Create a 'keyfile.config' file within your current directory. That file needs to have the following lines:

`trend_host= https://DSM-FQDN.com`

`trend_api_key= ABC123`

5. Use the following command to supply the config file to the Docker container at runtime and run whatever logic/code you may have added to main.py. 

`docker run -ti --rm --volume ${pwd}:/ds-docker/config example-name/ds-docker`

*Note:* the above command is for running on a Windows machine.
