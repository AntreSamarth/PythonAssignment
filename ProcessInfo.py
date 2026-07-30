import psutil
import logging
import os


def ConfigureLogger(DirectoryName):
    LogFile = os.path.join(DirectoryName, "ProcessLog.txt")

    logging.basicConfig(
        filename=LogFile,
        level=logging.INFO,
        format="%(asctime)s : %(levelname)s : %(message)s",
        force=True
    )

    return LogFile


def ValidateDirectory(DirectoryName):
    if os.path.isdir(DirectoryName):
        return True
    else:
        logging.error("Directory does not exist.")
        return False


def GetProcessInformation():
    try:
        logging.info("Running Process Information")
        logging.info("-" * 60)

        for process in psutil.process_iter(['pid', 'name', 'username']):
            try:
                info = process.info

                logging.info(
                    f"Name : {info['name']} | "
                    f"PID : {info['pid']} | "
                    f"User : {info['username']}"
                )

            except (psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess):
                continue

        logging.info("-" * 60)
        logging.info("Process information collected successfully.")

    except Exception as e:
        logging.error(f"Error : {e}")