import random
import re

from secret_santa_lib.sms_client import SmsClient


class Selector:
    __RE_PHONE_NUMBER: str = '^[0-9]{10}$'

    def __init__(self, client: SmsClient):
        self.__santas: dict[str, tuple[str, str]] = {}
        self.__client = client

    def add_santa(self, santa: str, phone_number: str, carrier: str) -> None:
        if not re.match(Selector.__RE_PHONE_NUMBER, phone_number):
            print(f'Invalid phone number: {phone_number}')
            print('Expected 10 digit phone number, i.e. 0123456789')
            return

        if not SmsClient.is_valid_carrier(carrier):
            print(f'invalid carrier: {carrier}')
            print(f'options: {SmsClient.get_carriers()}')
            return

        self.__santas[santa] = (phone_number, carrier)
        print(f'Added {santa}, {phone_number}, {carrier}')

    def select_and_notify_santas(self) -> None:
        if len(self.__santas) < 2:
            print('Not enough santas!')
            return

        remainder: list[str] = list(self.__santas.keys())

        self.__client.start()
        for santa, contact_info in self.__santas.items():
            target: str = random.choice(remainder)
            while target == santa:
                target = random.choice(remainder)
            phone_number, carrier = contact_info
            self.__client.notify_santa(santa, phone_number, carrier, target)
            remainder.remove(target)
        self.__client.stop()

