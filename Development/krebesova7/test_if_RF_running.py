import psutil
import time

pid = 45484

try:
    process = psutil.Process(pid)
    print(f"Monitoring process with PID: {pid}")

    while True:
        cpu_usage = process.cpu_percent(interval=1.0)
        if cpu_usage > 0.0:
            print(f"CPU Active: Status: {process.status()}, CPU: {cpu_usage}%, Memory: {process.memory_info().rss / 1e6} MB")

except Exception as e:
    print(f"An error occurred: {e}")
    