# Extra exercise
# Countdown timer with a time delay
import time

counter = int(input("Enter time in seconds: "))

while counter > 0:
    print(f"T-minus {counter}")
    counter -= 1
    time.sleep(1) # pauses the program for 1 second

print("Time's up!!!")