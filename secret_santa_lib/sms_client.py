import configparser

from twilio.rest import Client


class SmsClient:
    def __init__(self, account_sid: str, auth_token: str, phone_number: str):
        self.__client: Client = Client(account_sid, auth_token)
        self.__phone_number: str = phone_number

    def notify_santa(self, santa: str, phone_number: str, target: str) -> None:
        msg: str = (
            f'Hiya, {santa}, you ho ho ho! ;)\n'
            f'{target} has been really nice this year! '
            'Could you please be their secret santa?\n'
            'Love, Secret Santa Bot'
        )

        self.__client.messages \
            .create(
                body=msg,
                from_=self.__phone_number,
                to=phone_number
            )


def from_config() -> SmsClient:
    config = configparser.ConfigParser()
    config.read('config.ini')

    twilio_conf = config['TWILIO']
    account_sid = twilio_conf['AccountSid']
    auth_token = twilio_conf['AuthToken']
    phone_number = twilio_conf['PhoneNumber']

    return SmsClient(account_sid, auth_token, phone_number)

