import schedule
import time
from datetime import datetime

def DisplayDateTime():
    current = datetime.now()
    print("Current Date and Time :", current.strftime("%d-%m-%Y %H:%M:%S"))

def main():
    # Schedule the function to run every 1 minute
    schedule.every(1).minutes.do(DisplayDateTime)

    print("Displaying current date and time every minute...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()