import smtplib
import os

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


def SendMail(SenderMail, Password, ReceiverMail, LogFile):

    try:
        Message = MIMEMultipart()

        Message["From"] = SenderMail
        Message["To"] = ReceiverMail
        Message["Subject"] = "Running Process Log"

        Body = "Please find the attached Process Log File."

        Message.attach(MIMEText(Body, "plain"))

        Attachment = open(LogFile, "rb")

        Payload = MIMEBase('application', 'octet-stream')

        Payload.set_payload(Attachment.read())

        encoders.encode_base64(Payload)

        Payload.add_header(
            'Content-Disposition',
            f'attachment; filename={os.path.basename(LogFile)}'
        )

        Message.attach(Payload)

        Server = smtplib.SMTP("smtp.gmail.com",587)

        Server.starttls()

        Server.login(SenderMail,Password)

        Text = Message.as_string()

        Server.sendmail(SenderMail,ReceiverMail,Text)

        Server.quit()

        return True

    except Exception as e:
        print(e)
        return False