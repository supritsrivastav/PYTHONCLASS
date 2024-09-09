import time

def display_current_time():
    while True:
        current_time = time.strftime("%H:%M:%S")
        print(f"Current time: {current_time}")
        time.sleep(2)

if __name__ == "__main__":
    display_current_time()
