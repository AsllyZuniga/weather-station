'''
Script description:
Get temperature and humidity from DHT11 since Arduino.
Date: 07/10/2024
Developer: Aslly Zuñiga
'''
#Import libraries
import serial
import time
import serial.tools.list_ports
from detect_arduino_port import p

#Arduino port
arduino_port = p
arduino_bau = 9600

service = serial.Serial(
    arduino_port,
    arduino_bau,
    timeout = 1
)

time.sleep(1) #Delay

while True:
    #data = service.readline.decode('utf-8').strip()
    data = service.readline().decode('utf-8').rstrip()
    
    if data:
        temperature, humidity = data.split(",") 
        
        print(f"Temperature: {temperature} °C")
        print(f"Humidity: {humidity} %")
        
        #1. Create a new model data called data test_data
        #Fields: id, temp, hum, created_at
        #2. Create a method to insert data into test_data
        #3. Update method: Insert data when detect changes in temp or hum
        #Method to insert data in database
       
    time.sleep(1)
