#!/usr/bin/env python
import pika, time
import sys, os, inspect
pathapp = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(pathapp + "/config")

import Environment as env

class RabbitMQ(object):
	
	def __init__(self):
		self.credentials = pika.PlainCredentials(env.RABBIT_USER, env.RABBIT_PASS)
		self.connection = pika.BlockingConnection(pika.ConnectionParameters(env.RABBIT_HOST, env.RABBIT_PORT, env.RABBIT_VHOST, self.credentials))
		self.channel = self.connection.channel()
		
	def send_data(self, key_queue_name, message):
		print '\nSend msg to queue rabbitmq'
		print time.strftime("%H:%M:%S %Y/%m/%d")
		self.channel.queue_declare(key_queue_name)
		self.channel.basic_publish(exchange = '', routing_key = key_queue_name, body = message)
		self.connection.close()
		print "[x] Sent " + message
	
	def receive_data(self, key_queue_name):
		self.channel.queue_declare(key_queue_name)
		print "[*] Waiting for messages. To exit press CTRL+C"

		self.channel.basic_qos(prefetch_count = 1)
		self.channel.basic_consume(callback, queue = key_queue_name)
		self.channel.start_consuming()

def callback(ch, method, properties, body):
	print " Received %r" % (body)
	ch.basic_ack(delivery_tag = method.delivery_tag)