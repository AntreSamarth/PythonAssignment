import psutil
import logging


def ConfigureLogger():
    logging.basicConfig(
        filename="ProcessLog.txt",
        level=logging.INFO,
        format="%(asctime)s : %(levelname)s : %(message)s"
    )


def ValidateArguments():
    if len(__import__("sys").argv) != 2:
        logging.error("Invalid number of arguments.")
        logging.info("Usage : python main.py ProcessName")
        return False

    return True


def GetProcessInformation(ProcessName):
    try:
        Found = False

        logging.info(f"Searching for process : {ProcessName}")

        for process in psutil.process_iter(['pid', 'name', 'username']):
            try:
                info = process.info

                if info['name'] is not None:
                    Name = info['name'].split(".")[0]

                    if Name.lower() == ProcessName.lower():
                        Found = True

                        logging.info(
                            f"Name : {info['name']} | "
                            f"PID : {info['pid']} | "
                            f"User : {info['username']}"
                        )

                # If you want exact name including extension,
                # use this instead:
                #
                # if info['name'].lower() == ProcessName.lower():

            except (psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess):
                continue

        if Found == False:
            logging.info(f"{ProcessName} process is not running.")

    except Exception as e:
        logging.error(f"Error : {e}")