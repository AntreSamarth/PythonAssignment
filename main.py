import sys
import logging
import ProcessInfo
import MailSender


def main():

    try:

        if len(sys.argv) != 3:
            print("Usage : python main.py DirectoryName ReceiverEmail")
            return

        DirectoryName = sys.argv[1]
        ReceiverMail = sys.argv[2]

        LogFile = ProcessInfo.ConfigureLogger(DirectoryName)

        if ProcessInfo.ValidateDirectory(DirectoryName) == False:
            return

        ProcessInfo.GetProcessInformation()

        SenderMail = "antresamarth744@gmail.com"

        Password = "Your_App_Password"

        Status = MailSender.SendMail(
            SenderMail,
            Password,
            ReceiverMail,
            LogFile
        )

        if Status == True:
            logging.info("Mail sent successfully.")

        else:
            logging.error("Unable to send mail.")

    except Exception as e:
        logging.error(f"Error : {e}")


if __name__ == "__main__":
    main()