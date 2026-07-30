import sys
import logging
import ProcessInfo


def main():
    try:
        ProcessInfo.ConfigureLogger()

        if ProcessInfo.ValidateArguments() == False:
            return

        ProcessName = sys.argv[1]

        ProcessInfo.GetProcessInformation(ProcessName)

    except Exception as e:
        logging.error(f"Error : {e}")


if __name__ == "__main__":
    main()