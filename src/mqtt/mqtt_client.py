import pika
import sys
import signal
import mqtt_const


def send_rabbitmq_message(message, queue=mqtt_const.QUEUE_NAME):
    # Establish connection to RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue
    channel.queue_declare(queue=queue)

    # Send the message
    channel.basic_publish(
        exchange='',
        routing_key=queue,
        body=message
    )

    print(f"Sent message: {message}")
    connection.close()


def signal_handler(sig, frame):
    print("\nCtrl+C detected. Exiting...")
    sys.exit(0)


if __name__ == "__main__":
    # Register the signal handler for CTRL+C
    signal.signal(signal.SIGINT, signal_handler)

    print("Enter messages (Ctrl+C to exit):")

    while True:
        try:
            user_input = input("> ")
            if user_input.lower() in ['quit', 'exit']:
                break

            send_rabbitmq_message(user_input)

        except EOFError:
            break
