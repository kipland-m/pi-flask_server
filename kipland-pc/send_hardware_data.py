import requests
import psutil
import time

kip_pi_ip = '192.168.0.73'

while True:
    try:
        # dictionary containing hardware data
        hardware_data = {
            'cpu_usage': psutil.cpu_percent(),
            'memory_usage': psutil.virtual_memory().percent,
            'cpu_freq': psutil.cpu_freq(),
            'bytes_sent': psutil.net_io_counters().bytes_sent,
            'bytes_received': psutil.net_io_counters().bytes_recv,

        }

        response = requests.post(f'http://{kip_pi_ip}:5000/receive_hardware_data', json=hardware_data)
        for item in response:
            print(response.text)
            
        time.sleep(5)

    except Exception as e:
        print("Error:", e)
