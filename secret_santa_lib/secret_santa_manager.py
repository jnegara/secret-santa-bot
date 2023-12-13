import random

from secret_santa_lib.contact import Contact
from secret_santa_lib.email_client import EmailClient


class SecretSantaManager:
    def __init__(self):
        self.__participants: list[Contact] = []

    def add_participant(self, name: str, email: str) -> None:
        participant: Contact = Contact(name, email)
        self.__participants.append(participant)
        print(f'added {participant.to_string()}')
    
    def assign_and_notify_participants(self) -> None:
        if len(self.__participants) < 2:
            print('not enough participants!')
            return

        assignments: list[str] = [p.name() for p in self.__participants]
        random.shuffle(assignments)
    
        while self.__is_self_assigned(assignments):
            random.shuffle(assignments)
        
        for i in range(len(assignments)):
            gifter: Contact = self.__participants[i]
            giftee: str = assignments[i]
            message: str = SecretSantaManager.__get_message(gifter.name(), giftee)

            client: EmailClient = EmailClient()
            client.send_email(gifter, 'It\'s Santa, Baby!', message)

    @classmethod
    def __get_message(cls, gifter: str, giftee: str) -> str:
        return (
            f'Dear {gifter},\n'
            '\n'
            'It\'s your fav, SantaBot, again, giving it one last try before I give in to the nog.\n'
            'If by some christmas miracle all the naughty girlies on my list get this email, '
            f'then you\'ll be stuffing {giftee}\'s stocking this Christmas.\n'
            '\n'
            'XoXo,\n'
            'SantaBot6.90'
        )

    def __is_self_assigned(self, assignments: str) -> bool:
        for i in range(len(assignments)):
            if assignments[i] == self.__participants[i].name():
                return True
        return False