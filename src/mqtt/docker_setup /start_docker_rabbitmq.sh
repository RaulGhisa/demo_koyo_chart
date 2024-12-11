docker run --name rabbitmq -p 5672:5672 -p 15672:15672 -v ./rabbitmq.conf:/etc/rabbitmq/rabbitmq.conf rabbitmq:4.0-management
