from email.mime.text import MIMEText
from smtplib import SMTP

from secret_santa_lib.config import CONFIG, EmailConfig
from secret_santa_lib.contact import Contact

class EmailClient:
    def __init__(self):
        email_config: EmailConfig = CONFIG.email()
        self.__email: str = email_config.email()
        self.__password: str = email_config.password()
        self.__hostname: str = email_config.hostname()
        self.__port: int = email_config.port()
    
    def send_email(self, contact: Contact, subject: str, message: str) -> None:
        msg: MIMEText = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = self.__email
        msg['To'] = contact.email()

        server: SMTP = SMTP(host=self.__hostname, port=self.__port)
        server.starttls()
        server.login(user=self.__email, password=self.__password)
        server.send_message(msg)
        server.quit()


