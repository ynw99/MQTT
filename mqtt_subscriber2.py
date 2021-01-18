import paho.mqtt.client as mqtt
import time

mqttBroker = 'mqtt.eclipseprojects.io'      # Alamat broker dari MQTT
mqttTopic = 'MQTT-JSN'                      # Topik yang digunakan
client = mqtt.Client('Smartphone')  # Instansiasi objek MQTT publisher
client.connect(mqttBroker)                  # Melakukan koneksi dengan broker MQTT


def on_message(client, userdata, message):
        print('Received message: {}'.
            format(message.payload.decode('utf-8')))


client.loop_start()                         # Memulai looping untuk subscriber

client.subscribe(mqttTopic)
client.on_message = on_message              # Jika mendapat data dari publisher maka akan memanggil fungsi on_message()
time.sleep(30)                              # Istirahat tiap 30 detik

client.loop_stop()                          # Memberhentikan looping untuk subscriber