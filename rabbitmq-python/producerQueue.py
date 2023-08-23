# https://medium.com/better-programming/introduction-to-message-queue-with-rabbitmq-python-639e397cb668
# producer.py
# This script will publish MQ message to my_exchange MQ exchange

import pika
import os
from dotenv import load_dotenv

load_dotenv()

RABBITMQ_IP = os.getenv('RABBITMQ_IP')
USER_RABBITMQ = os.getenv('USER_RABBITMQ')
PASSWORD_RABBITMQ = os.getenv('PASSWORD_RABBITMQ')

connection = pika.BlockingConnection(pika.ConnectionParameters('RABBITMQ_IP', 5672, '/', pika.PlainCredentials('USER_RABBITMQ', 'PASSWORD_RABBITMQ')))
channel = connection.channel()

channel.basic_publish(exchange='my_exchange', routing_key='', body='Hello World!')

connection.close()