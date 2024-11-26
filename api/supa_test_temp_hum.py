import requests
from supabase import create_client, Client
from database import con, cur  # Usamos el archivo `database.py` para conexión SQLite.

# Supabase data connection: URL, KEY 
SUPABASE_URL = "https://epnzrrkcchoyvflmpadc.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVwbnpycmtjY2hveXZmbG1wYWRjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzE5NjQ2MDgsImV4cCI6MjA0NzU0MDYwOH0.rBYusgPIQZZ1CZWwoIkv0F_O3UcFWyISTKEMbtc0Rqg"

# ThingSpeak API key and URL
THINGSPEAK_WRITE_KEY = "MY2ZQZHAF7TALI54"  # Tu clave API de ThingSpeak
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# Conectar al cliente de Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Función para guardar datos en SQLite
def save_to_local_db(temperature, humidity):
    try:
        cur.execute('''
        INSERT INTO sensor_data (temperature, humidity)
        VALUES (?, ?)
        ''', (temperature, humidity))
        con.commit()
        print("Data successfully saved to local database.")
    except Exception as e:
        print(f"Error saving data to local database: {e}")

# Función para guardar datos en Supabase
def save_to_supabase(temperature, humidity):
    response = supabase.table('sensor_data').insert(
        {
            "temperature": temperature,
            "humidity": humidity
        }
    ).execute()

    if response.data:
        print(f"Sensor data saved successfully to Supabase: {response.data}")
    elif response.error:
        print(f"Error saving sensor data to Supabase: {response.error}")

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

# Función principal para manejar los datos del sensor
def handle_sensor_data(temperature, humidity):
    # Guardar en SQLite
    save_to_local_db(temperature, humidity)
    # Guardar en Supabase
    save_to_supabase(temperature, humidity)
    # Enviar a ThingSpeak
    send_to_thingspeak(temperature, humidity)

# Simulación: Captura automática de datos del sensor
def read_sensor_data():
    # Esta función debería conectarse a tus sensores reales.
    # Para este ejemplo, generamos datos aleatorios.
    import random
    temperature = round(random.uniform(15.0, 35.0), 2)  # Simulación de temperatura
    humidity = round(random.uniform(30.0, 90.0), 2)     # Simulación de humedad
    return temperature, humidity

# Main loop: Leer datos y manejarlos
try:
    while True:
        temperature, humidity = read_sensor_data()
        print(f"Captured Sensor Data -> Temperature: {temperature}, Humidity: {humidity}")
        handle_sensor_data(temperature, humidity)
        
        # Esperar 10 segundos entre lecturas
        import time
        time.sleep(10)
except KeyboardInterrupt:
    print("Sensor data capture stopped.")
    con.close()  # Cerrar la conexión SQLite al salir.
