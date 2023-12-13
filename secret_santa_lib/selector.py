import random
import re

from secret_santa_lib.sms_client import SmsClient, from_config


class Selector:
    __RE_PHONE_NUMBER: str = '^\+[0-9]{11,12}$'
    __CLIENT: SmsClient = from_config()

    def __init__(self):
        self.__santas: dict[str, str] = {}

    def add_santa(self, santa: str, phone_number: str) -> None:
        if not re.match(Selector.__RE_PHONE_NUMBER, phone_number):
            print('Invalid phone number.')
            print('Must match pattern: +[country code][10 digit number]')
            print('For example: +12222222222')
            return

        if santa in self.__santas:
            print(f'{santa}, {self.__santas[name]} has already been registered as a santa.')
            if phone_number == self.__santas[name]:
                return
            print(f'Updating phone number to {phone_number}')
        else:
            print(f'Added {santa}, {phone_number}')

        self.__santas[santa] = phone_number

    def select_and_notify_santas(self) -> None:
        if len(self.__santas) < 2:
            print('Not enough santas!')
            return

        remainder: list[str] = list(self.__santas.keys())

        for santa, phone_number in self.__santas.items():
            target: str = random.choice(remainder)
            while target == santa:
                target = random.choice(remainder)
            Selector.__CLIENT.notify_santa(santa, phone_number, target)
            remainder.remove(target)

