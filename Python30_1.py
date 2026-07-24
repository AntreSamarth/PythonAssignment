import schedule
import time

def Display():
    print("Jay Ganesh...")

def main():
    # Schedule the Display function to run every 2 seconds
    schedule.every(2).seconds.do(Display)

    # Keep the scheduler running
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()