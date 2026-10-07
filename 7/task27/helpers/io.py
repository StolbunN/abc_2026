import datetime

def logger(message):
    current_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    print(f"[{current_time}] {message}")
