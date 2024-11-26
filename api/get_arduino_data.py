'''
Script description:
Get temperature and humidity from DHT11 since Arduino.
Date: 07/10/2024
Developer: Aslly Zuñiga
'''
#Import libraries
import serial
import serial.tools.list_ports
import time
from detect_arduino_port import p

port = p

def  get_arduino_port():
    ports = serial.tools.list_ports.comports()
    print(ports)
    #Con estas lineas se trae los puertos de la PC

#Arduino port
arduino_port = port
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
        #print(data)
        temperature, humidity = data.split(",")
        print(f"Temperature: {temperature} °C")
        print(f"Humidity: {humidity} %")

#Aqui el INSERT INTO        

#1. Crear una nuevo modelo de datos (tabla "test_data")
#Campos necesarios: id, temp, hum, fecha de creacion
#2. Crear un metodo para insertar datos en la tabla creada "test_data"
#3. Actualizar metodo (debe cumplir con, si detecta cambios inserta los datos): Los datos insertados detectan cambios en la temp y hum
#4. Crear un menu de opciones que se llame List sensor data
#5. Crear un menu de opciones que permita graficar con Matplotlib

    time.sleep(1)