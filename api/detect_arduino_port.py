import serial
import serial.tools.list_ports

def get_arduino_port():
    ports = serial.tools.list_ports.comports()
    ##print(ports)
    
    for port in ports:
        if "Arduino" in port.description or "USB-SERIAL CH340" in port.description:
            '''
            print(f"Detected port: {port.device}")
            print(f"Name: {port.name}")
            print(f"Description: {port.description}")
            print(f"HWID: {port.hwid}")
            print(f"VID: {port.vid}")
            print(f"PID: {port.pid}")
            print(f"Serial number: {port.serial_number}")
            print(f"Manfacturer: {port.manufacturer}")
            print(f"Product: {port.product}")
            print(f"Interface: {port.interface}")
            print(f"Location: {port.location}")
            '''
            return port.device
    print("No Arduino port detected")
    return None

p = get_arduino_port()
print(p)
#get_arduino_port()

