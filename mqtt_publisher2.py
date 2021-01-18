import os
import time
from random import randrange

import paho.mqtt.client as mqtt 

mqttBroker = 'mqtt.eclipseprojects.io'      # Alamat broker dari MQTT
mqttTopic = 'MQTT-JSN'                   # Topik yang digunakan
client = mqtt.Client('Temperature_Outside') # Instansiasi objek MQTT publisher
client.connect(mqttBroker)                  # Melakukan koneksi dengan broker MQTT

counter = 0                                 # Counter untuk iterasi

while True:
    randNumber = randrange(10)              # Generate angka random
    client.publish(mqttTopic, randNumber)   # Melakukan publish data
    print('Just published {} to topic {}'.
            format(randNumber, mqttTopic))  # Print ke terminal data yang dikirim publisher
    counter += 1
    if(counter == 30):
        print(os.system('cls' if os.name == 'nt'    # Clearscreen tiap kali sudah 30 iterasi
                        else 'clear'))
        counter = 0
    time.sleep(1)                           # Delay 1 detik