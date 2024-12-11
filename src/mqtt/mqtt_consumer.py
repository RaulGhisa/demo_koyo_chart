import pika
import mqtt_const


class RabbitMQBroker:
    def __init__(self, host='localhost'):
        # Establish connection
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host)
        )
        self.channel = self.connection.channel()

    def create_queue(self, queue_name):
        # Declare a queue (creates if not exists)
        self.channel.queue_declare(queue=queue_name)

    def publish_message(self, queue_name, message):
        # Publish a message to a specific queue
        self.channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=message
        )
        print(f"Sent message to {queue_name}: {message}")

    def consume_messages(self, queue_name, callback):
        # Set up message consumption
        self.channel.basic_consume(
            queue=queue_name,
            on_message_callback=callback,
            auto_ack=True
        )
        print(f"Waiting for messages on {queue_name}. To exit press CTRL+C")
        self.channel.start_consuming()

    def close(self):
        # Close connection
        self.connection.close()


def message_handler(ch, method, properties, body):
    print(f"Received message: {body.decode()}")


def main():
    # Create broker instance
    broker = RabbitMQBroker()

    # Define queue
    broker.create_queue(mqtt_const.QUEUE_NAME)

    # Publish messages
    # broker.publish_message(queue_name, "Hello RabbitMQ!")
    # broker.publish_message(queue_name, "This is a test message")

    # Consume messages (uncomment to run)
    broker.consume_messages(mqtt_const.QUEUE_NAME, message_handler)


if __name__ == "__main__":
    main()
