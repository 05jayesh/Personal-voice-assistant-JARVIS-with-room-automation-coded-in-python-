#include<ESP8266WiFi.h>
#include "Adafruit_MQTT.h"
#include "Adafruit_MQTT_Client.h"

#define Relay1  D1
#define Relay2  D2
#define Relay3  D3

#define WLAN_SSID "jarvis"
#define WLAN_PASS "espjarvis8266"

#define AIO_SERVER      "io.adafruit.com"
#define AIO_SERVERPORT  1883
#define AIO_USERNAME    "05jayesh"
#define AIO_KEY         "23b02f3337964e6ebc2ebd8d91a6d586" 

WiFiClient client;

Adafruit_MQTT_Client mqtt(&client,AIO_SERVER,AIO_SERVERPORT,AIO_USERNAME,AIO_KEY);

Adafruit_MQTT_Subscribe lights = Adafruit_MQTT_Subscribe(&mqtt, AIO_USERNAME"/feeds/lights");
Adafruit_MQTT_Subscribe fan    = Adafruit_MQTT_Subscribe(&mqtt, AIO_USERNAME"/feeds/fan");



void setup()
{

  pinMode(Relay1, OUTPUT);
  pinMode(Relay2, OUTPUT);
  pinMode(Relay3, OUTPUT);

  digitalWrite(Relay1, HIGH);
  digitalWrite(Relay2, HIGH);
  digitalWrite(Relay3, HIGH);

  void MQTT_connect();

  Serial.begin(115200);

  Serial.println();
  Serial.print("Connecting to");
  Serial.print("WLAN_SSID");

  WiFi.begin(WLAN_SSID, WLAN_PASS);
  while (WiFi.status()!=WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println();

  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  mqtt.subscribe(&lights);
  mqtt.subscribe(&fan);
}

void loop()
{
  MQTT_connect();

  Adafruit_MQTT_Subscribe *subscription;
  while ((subscription = mqtt.readSubscription(20000)))
  {
    if (subscription==&lights)
    {
      Serial.print(F("Got: "));
      Serial.println((char *)lights.lastread);
      int lights_state = atoi((char*)lights.lastread);
      digitalWrite(Relay1,lights_state);
      digitalWrite(Relay2,lights_state);
    }
     if (subscription==&fan)
    {
      Serial.print(F("Got: "));
      Serial.println((char *)fan.lastread);
      int fan_state = atoi((char*)fan.lastread);
      digitalWrite(Relay3,fan_state);
    }
  }
}

void MQTT_connect()
{
  int8_t ret;

  if (mqtt.connected())
  {
    return;
  }
  Serial.print("Connecting to MQTT...");
  uint8_t retries=3;

  while ((ret=mqtt.connect())!= 0)
  {
    Serial.println(mqtt.connectErrorString(ret));
    Serial.println("Retrying MQTT connection in 3 seconds...");
    mqtt.disconnect();
    delay(3000);
    //retries--;
    if (retries==0)
    {
      while(1);
    }
  }
  Serial.println("MQTT connected!");
}


