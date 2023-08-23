# https://medium.com/better-programming/introduction-to-message-queue-with-rabbitmq-python-639e397cb668
# consumer.py
# Consume RabbitMQ queue

import pika
import os
from dotenv import load_dotenv

load_dotenv()

RABBITMQ_IP = os.getenv('RABBITMQ_IP')
USER_RABBITMQ = os.getenv('USER_RABBITMQ')
PASSWORD_RABBITMQ = os.getenv('PASSWORD_RABBITMQ')

connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_IP, 5672, '/', pika.PlainCredentials(USER_RABBITMQ, PASSWORD_RABBITMQ)))
channel = connection.channel()

def callback(ch, method, properties, body):
    print(f'{body} is received')

channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)
channel.start_consuming()