import smtplib
from email.message import EmailMessage

def SendMail(SenderEmail, SenderPassword, ReceiverEmail, LogFileName, Body):

    try:

        Msg = EmailMessage()

        Msg["Subject"] = "Duplicate File Removal Report"
        Msg["From"] = SenderEmail
        Msg["To"] = ReceiverEmail

        Msg.set_content(Body)

        fobj = open(LogFileName,"rb")

        FileData = fobj.read()

        fobj.close()

        FileName = LogFileName.split("\\")[-1]

        Msg.add_attachment(FileData,
                           maintype="application",
                           subtype="octet-stream",
                           filename=FileName)

        Server = smtplib.SMTP("smtp.gmail.com",587)

        Server.starttls()

        Server.login(SenderEmail,SenderPassword)

        Server.send_message(Msg)

        Server.quit()

        return True

    except Exception as E:

        print(E)

        return False