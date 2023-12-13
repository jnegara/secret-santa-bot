import configparser
import smtplib

from email.message import EmailMessage


class SmsClient:
    __CARRIERS: dict[str, str] = {
        'verizon': 'vtext.com',
        'tmobile': 'tmomail.net',
        'sprint': 'messaging.sprintpcs.com',
        'at&t': 'txt.att.net',
        'boost': 'smsmyboostmobile.com',
        'cricket': 'sms.cricketwireless.net',
        'uscellular': 'email.uscc.net',
    }

    @classmethod
    def is_valid_carrier(cls, carrier: str) -> bool:
        return carrier in cls.__CARRIERS

    @classmethod
    def get_carriers(cls) -> str:
        return ', '.join(cls.__CARRIERS.keys())

    def __init__(self, email: str, password: str, hostname: str, port: int):
        self.__email: str = email
        self.__password: str = password
        self.__client = smtplib.SMTP(host=hostname, port=port)

    def start(self) -> None:
        self.__client.starttls()
        self.__client.login(user=self.__email, password=self.__password)

    def stop(self) -> None:
        self.__client.quit()
    
    def notify_santa(self, name: str, phone_number: str, carrier: str, assignment: str) -> None:
        if not SmsClient.is_valid_carrier(carrier):
            print(f'invalid carrier: {carrier}')
        recipient: str = f'{phone_number}@{SmsClient.__CARRIERS[carrier]}'
        message: str = (
            f'\nHiya, {name}, you ho ho ho! ;)\n'
            f'{assignment} has been really nice this year! '
            'Could you please be their secret santa?\n'
            'Love, Secret Santa Bot'
        )
        self.__client.sendmail(self.__email, recipient, message)


def from_config() -> SmsClient:
    config = configparser.ConfigParser()
    config.read('config.ini')

    email_config = config['EMAIL']
    email = email_config['email']
    password = email_config['password']
    hostname = email_config['hostname']
    port = int(email_config['port'])    

    return SmsClient(email, password, hostname, port)

