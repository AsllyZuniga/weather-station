/*
DATE 19/09/2024
DEVELOPER : Aslly Zuñiga
SKETCH DESCRIPTION: GET TEMPERATURE AND HUMIDITY FROM DHT 11
*/
#include "DHT.h"
#define DHTTYPE DHT11
#define DHTPIN  8


float temp = 0;
float hum = 0;

DHT dht(DHTPIN, DHTTYPE);


void setup() {
  dht.begin();
  Serial.begin(9600);

}

void loop() {
  delay (2000);

temp = dht.readTemperature();
hum = dht.readHumidity();

Serial.print(temp);
Serial.print(",");
Serial.println(hum);

}