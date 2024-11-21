import requests
from supabase import create_client, Client

# Supabase data connection: URL, KEY 
SUPABASE_URL = "https://epnzrrkcchoyvflmpadc.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVwbnpycmtjY2hveXZmbG1wYWRjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzE5NjQ2MDgsImV4cCI6MjA0NzU0MDYwOH0.rBYusgPIQZZ1CZWwoIkv0F_O3UcFWyISTKEMbtc0Rqg"

# ThingSpeak API key and URL
THINGSPEAK_WRITE_KEY = "MY2ZQZHAF7TALI54"  # Tu clave API de ThingSpeak
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# Conectar al cliente de Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Función para guardar los datos de temperatura y humedad
def save_sensor_data(temperature, humidity):
    response = supabase.table('sensor_data').insert(
        {
            "temperature": temperature,
            "humidity": humidity
        }
    ).execute()

    # Manejo de la respuesta de Supabase
    if response.data:
        print(f"Sensor data saved successfully: {response.data}")
    elif response.error:
        print(f"Error saving sensor data: {response.error}")

    # Enviar datos a ThingSpeak
    send_to_thingspeak(temperature, humidity)

# Función para enviar los datos a ThingSpeak
def send_to_thingspeak(temperature, humidity):
    payload = {
        "api_key": THINGSPEAK_WRITE_KEY,
        "field1": temperature, 
        "field2": humidity     
    }
    try:
        response = requests.post(THINGSPEAK_URL, data=payload)
        if response.status_code == 200:
            print("Data successfully sent to ThingSpeak")
        else:
            print(f"Error sending data to ThingSpeak: {response.status_code}")
    except Exception as e:
        print(f"Exception occurred while sending data to ThingSpeak: {e}")

# Main
temperature = input("Temperature: ")
humidity = input("Humidity: ")
save_sensor_data(temperature, humidity)
