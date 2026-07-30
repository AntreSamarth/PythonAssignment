import sys
import logging
import ProcessInfo

def main():
    try:
        if len(sys.argv) != 2:
            print("Usage : python main.py DirectoryName")
            return

        DirectoryName = sys.argv[1]

        if ProcessInfo.ValidateDirectory(DirectoryName) == False:
            print("Directory does not exist.")
            return

        ProcessInfo.ConfigureLogger(DirectoryName)

        ProcessInfo.GetProcessInformation()

    except Exception as e:
        logging.error(f"Error : {e}")

if __name__ == "__main__":
    main()