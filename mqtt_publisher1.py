import os
import time
from random import uniform

import paho.mqtt.client as mqtt 

mqttBroker = 'mqtt.eclipseprojects.io'      # Alamat broker dari MQTT
mqttTopic = 'MQTT-JSN'                   # Topik yang digunakan
client = mqtt.Client('Temperature_Inside')  # Instansiasi objek MQTT publisher
client.connect(mqttBroker)                  # Melakukan koneksi dengan broker MQTT

counter = 0

while True:
    randNumber = uniform(20.0, 21.0)        # Generate angka random
    client.publish(mqttTopic, randNumber)   # Melakukan publish data
    print('Just published {} to topic {}'.
            format(randNumber, mqttTopic))  # Print ke terminal data yang dikirim publisher
    counter += 1
    if(counter == 30):
        print(os.system('cls' if os.name == 'nt'    # Clearscreen tiap kali sudah 30 iterasi
                        else 'clear'))
        counter = 0
    time.sleep(1)                           # Delay 1 detik