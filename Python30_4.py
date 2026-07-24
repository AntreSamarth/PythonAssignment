import schedule
import time

def Display():
    print("Namaskar...")

def main():
    # Schedule the function to run every day at 9:00 AM
    schedule.every().day.at("09:00").do(Display)

    print("Waiting for 9:00 AM...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()