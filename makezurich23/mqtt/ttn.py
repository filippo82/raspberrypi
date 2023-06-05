#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

# https://www.thethingsindustries.com/docs/integrations/mqtt/
# https://www.thethingsindustries.com/docs/integrations/mqtt/mqtt-clients/eclipse-paho/
# https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php
# https://www.thethingsnetwork.org/forum/t/a-python-program-to-listen-to-your-devices-with-mqtt/9036/13

import logging
import json

import paho.mqtt.client as mqtt

broker_address = "eu1.cloud.thethings.network"
PORT = 1883
PORT_TLS = 8883

# Username `{application id}@{tenant id}`
app_id = "makezurch-badge-2023-filippo82@ttn"

# Password (API key)
access_key = "NNSXS.JUTPHPU3ZWMAKRIAPVB2VTGC3RFP5TZGC56CI4Q.U6KTEF5N4CMVZANPJSERBTHIMHDCD3TWSIR6J7JR6NI73TAXUCQA"  # noqa

# Device ID
dev_id = "eui-2cf7f1205020024e"

# mosquitto_sub -h <Region>.thethings.network -d -t 'my-app-id/devices/my-dev-id/up'

client = mqtt.Client()  # create new instance

# Call back functions
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code: {mqtt.connack_string(rc)}")
    # subscribe for all devices of user
    # client.subscribe('temperature_v1/devices/filippo-lorawan-modem/up')
    # client.subscribe("+/devices/+/up")
    if rc == 0:
        res = client.subscribe("v3/+/devices/+/up")
        if res[0] != mqtt.MQTT_ERR_SUCCESS:
            raise RuntimeError("the client is not connected")

    if rc == 1:
        raise RuntimeError("connection failed: incorrect protocol version")
    if rc == 2:
        raise RuntimeError("connection failed: invalid client identifier")
    if rc == 3:
        raise RuntimeError("connection failed: server unavailable")
    if rc == 4:
        raise RuntimeError("connection failed: bad app_id or access_key")
    if rc == 5:
        raise RuntimeError("connection failed: not authorised")


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")


def on_message(client, userdata, message):
    # print("Message received!")
    # print("message received " ,str(message.payload.decode("utf-8")))
    print(f"Message topic: {message.topic}")
    # print(f"Message qos: {message.qos}")
    # print(f"Message retain flag: {message.retain}")
    try:
        # Format Json
        payload = json.loads(message.payload.decode("utf-8"))
        value = payload.get("uplink_message", {}).get("decoded_payload", {}).get("value", [])
        print(value)
        # temperature = payload['payload_fields']['temperature']
        # print(temperature)
        print("-----")
    except Exception as e:
        print(e)
        pass


def on_subscribe(client, userdata, mid, granted_qos):
    print(f"Subscribed: {str(mid)} {str(granted_qos)}")


def on_log(client, userdata, level, buf):
    """
    Log all MQTT protocol events, and the exceptions in callbacks
    that have been caught by Paho.
    """
    logging_level = mqtt.LOGGING_LEVEL[level]
    logging.log(logging_level, buf)


client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.on_log = on_log

client.username_pw_set(app_id, access_key)

# client.tls_set(ca_certs="mqtt-ca.pem")
client.tls_set()

# Connect to broker
client.connect(
    host=broker_address, port=PORT_TLS, keepalive=60
)

topic = f"{app_id}/devices/{dev_id}/up"

# client.subscribe(topic)

# client.loop_start()
client.loop_forever()

# and listen to server
# run = True
# while run:
#     client.loop()
