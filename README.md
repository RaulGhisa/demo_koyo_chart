# Foreword
This repository is for small robotics software tools that will be used throughout my PhD. The Python library requirements are for PIP and should be installed from `requirements.txt`... for all projects, might want to comment out what you will not need.

`TODO:` have separate requirement file for each tool. 

## Text 2 Speech
run `python src/text_2_speech.py` \
the generated audio files are saved in `out` directory

## RabbitMQ Server on Docker 
1. install RabbitMQ using Docker as described here: `https://www.rabbitmq.com/docs/download`
2. in `src/mqtt/docker_setup/` run `bash start_docker_rabbitmq.sh` to run the Docker container and mount the `rabbitmq.conf` into the container
3. make sure the network you are connected to allows traffic to port `5672` (AMQP server) and `15672` (optional - RabbitMQ Management Interface), Eduroam or CMS will block them
4. goes without saying that this is for development only, all security measures provided by the RabbitMQ broker were shot down, check `src/mqtt/docker_setup/rabbitmq.conf` too see what is disabled
