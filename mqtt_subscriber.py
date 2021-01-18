import time

import MySQLdb as mysql
import paho.mqtt.client as mqtt 

mqttBroker = 'mqtt.eclipseprojects.io'      # Alamat broker dari MQTT
mqttTopic = 'MQTT-JSN'                      # Topik yang digunakan
client = mqtt.Client('Smartphone')          # Instansiasi objek MQTT subscriber
client.connect(mqttBroker)                  # Melakukan koneksi dengan broker MQTT

# Konfigurasi Database
DBNAME = 'dbtest'
DBHOST = 'localhost'
DBPASSWORD = ''
DBUSER = 'root'

db = mysql.connect(DBHOST, DBUSER, DBPASSWORD, DBNAME)  # Menghubungkan python ke database

cur = db.cursor()                           # db cursor untuk melaksanakan query

def on_message(client, userdata, message):
    print('Received message: {}'.
        format(message.payload.decode('utf-8')))        # Printout ke terminal data yang diterima dari subscriber
    
    try:
        cur.execute('INSERT INTO table_name VALUES {}'.format(message)) # Insert data message ke database
        print('Data inserted succesfully')

    except:
        print('Unable to insert the data')

client.loop_start()                         # Memulai looping untuk subscriber

client.subscribe(mqttTopic)
client.on_message = on_message              # Jika mendapat data dari publisher maka akan memanggil fungsi on_message()
time.sleep(30)                              # Istirahat tiap 30 detik

client.loop_stop()                          # Memberhentikan looping untuk subscriber