import schedule
import time

def Display():
    print("Coding kr...")

def main():
    # Schedule the function to run every 30 minutes
    schedule.every(30).minutes.do(Display)

    print("Program started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()