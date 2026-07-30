import psutil
import logging
import os

def ConfigureLogger(DirectoryName):
    LogFile = os.path.join(DirectoryName, "ProcessLog.txt")

    logging.basicConfig(
        filename=LogFile,
        level=logging.INFO,
        format="%(asctime)s : %(levelname)s : %(message)s"
    )

def ValidateDirectory(DirectoryName):
    if os.path.exists(DirectoryName) == False:
        return False

    if os.path.isdir(DirectoryName) == False:
        return False

    return True

def GetProcessInformation():
    try:
        logging.info("Running Process Information")

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

        logging.info("Process information collected successfully.")

    except Exception as e:
        logging.error(f"Error : {e}")