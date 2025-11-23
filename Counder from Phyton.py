import time
### Make a Counder
def counter():
    minutes = int(input("Enter time in minutes: "))
    total_seconds = minutes * 60
    while total_seconds > 0:
        print(f"{total_seconds} remaining sec")
        time.sleep(1)
        total_seconds -= 1
    print("Time is finished")

counter()

