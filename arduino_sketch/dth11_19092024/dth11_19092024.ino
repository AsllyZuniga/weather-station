/*Sketch description: Get temperature and humidity from DTH11 Sensor
Date:19/09/2024
Developer: Aslly Zuñiga
*/

#include "DHT.h"
#define DHTTYPE DHT11
#define DHTPIN 5

float temperature = 0;
float humidity = 0;

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  dht.begin();
  Serial.begin(9600);

}

void loop() {
  delay(2000);
  temperature =  dht.readTemperature();
  humidity = dht.readHumidity();

  if(isnan (temperature) || isnan (humidity)){
    Serial.println("DHT11 reading error");
    return;
    
  }


  Serial.print("Temperatura: ");
  Serial.println(temperature);
  Serial.print("Humedad: ");
  Serial.println(humidity);
  

}























































+