import requests
from supabase import create_client, Client
import serial
import time

# Configuración de Supabase
SUPABASE_URL = "https://epnzrrkcchoyvflmpadc.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVwbnpycmtjY2hveXZmbG1wYWRjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzE5NjQ2MDgsImV4cCI6MjA0NzU0MDYwOH0.rBYusgPIQZZ1CZWwoIkv0F_O3UcFWyISTKEMbtc0Rqg"

THINGSPEAK_WRITE_KEY = "MY2ZQZHAF7TALI54"  # Clave API de ThingSpeak
THINGSPEAK_URL = "https://api.thingspeak.com/update"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Configuración de la comunicación serie
ser = serial.Serial('COM10', 9600, timeout=1)

def save_sensor_data(temperature, humidity):
    try:
        response = supabase.table('sensor_data').insert(
            {
                "temperature": temperature,
                "humidity": humidity
            }
        ).execute()
        if response.data:
            print(f"Datos guardados en Supabase: {response.data}")
        elif response.error:
            print(f"Error al guardar en Supabase: {response.error}")
    except Exception as e:
        print(f"Error al conectar con Supabase: {e}")

    send_to_thingspeak(temperature, humidity)

def send_to_thingspeak(temperature, humidity):
    payload = {
        "api_key": THINGSPEAK_WRITE_KEY,
        "field1": temperature,
        "field2": humidity
    }
    try:
        response = requests.post(THINGSPEAK_URL, data=payload)
        if response.status_code == 200:
            print("Datos enviados a ThingSpeak correctamente")
        else:
            print(f"Error al enviar a ThingSpeak: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error al enviar datos a ThingSpeak: {e}")

def main():
    while True:
        try:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                print(f"Línea recibida: {line}")

                if "Temp:" in line and "Hum:" in line:
                    temp_hum = line.split(", ")
                    temperature = float(temp_hum[0].split(": ")[1])
                    humidity = float(temp_hum[1].split(": ")[1])

                    print(f"Temperatura: {temperature}°C, Humedad: {humidity}%")
                    save_sensor_data(temperature, humidity)

            time.sleep(10)

        except Exception as e:
            print(f"Error en el bucle principal: {e}")

if __name__ == "__main__":
    print("Iniciando lectura de datos...")
    try:
        main()
    except KeyboardInterrupt:
        print("Programa detenido por el usuario")
