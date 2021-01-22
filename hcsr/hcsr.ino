
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#define trigPin D4 //2
#define echoPin D3 //0
#define solenoidPin D5
 
const char* ssid = "robby :)";
const char* password =  "123456789";
const char* mqttServer = "mqtt.eclipseprojects.io";
const int mqttPort = 1883;
 
WiFiClient espClient;
PubSubClient client(espClient);

long duration;
int distance;

unsigned long now;
unsigned long lastMsg = 0;
#define MSG_BUFFER_SIZE  (50)
char msg[MSG_BUFFER_SIZE];

void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  pinMode(solenoidPin, OUTPUT);
  Serial.begin(9600); // Starts the serial communication
  setup_wifi();
}

void loop() {
      ukurjarak();
      if (!client.connected()) {
        reconnect();
      }
      client.loop();
    // Prints the distance on the Serial Monitor
      while(distance<=15){
        digitalWrite(solenoidPin,HIGH);
        Serial.print("Distance: ");
        Serial.println(distance);
        clientpablis();
        ukurjarak();
        delay(1000);
      }
      digitalWrite(solenoidPin,LOW);
    Serial.print("Distance: ");
    Serial.println(distance);
    clientpablis();
    delay(1000);
}

void ukurjarak(){
  // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  
  // Calculating the distance
  distance= duration*0.034/2;
}

void setup_wifi() {

  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");
 
  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);
 
  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");
 
    if (client.connect("ESP8266Client")) {
 
      Serial.println("connected");  
 
    } else {
 
      Serial.print("failed with state ");
      Serial.print(client.state());
      delay(2000);
 
    }
  }
}

void callback(char* topic, byte* payload, unsigned int length) {
 
  Serial.print("Message arrived in topic: ");
  Serial.println(topic);
 
  Serial.print("Message:");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
 
  Serial.println();
  Serial.println("-----------------------");
 
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");

    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(1000);
    }
  }
}

void clientpablis(){
  now = millis();
    if (now - lastMsg > 100) {
      lastMsg = now;
      snprintf (msg, MSG_BUFFER_SIZE, "%ld", distance);
      Serial.print("Publish message: ");
      Serial.println(msg);
      client.publish("MQTT-JSN", msg);
    }
}
