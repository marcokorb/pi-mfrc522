# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import time

from rfid import RFID expovariate

BROKER_URL = 'test.mosquitto.org'
CLIENT_ID = 'pi-mfrc522'
RC522_READ_TOPIC = '{}/read'.format(CLIENT_ID)


client = mqtt.Client(CLIENT_ID)
print('connected to: ', BROKER_URL)
client.connect(BROKER_URL, 80, 60)
client.loop_start()

rfid = RFID()


while True:
	tag_id = rfid.reader.read_id_no_block()
	print(tag_id)
	client.publish(RC522_READ_TOPIC, tag_id)
	time.sleep(3)
