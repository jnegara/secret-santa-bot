from secret_santa_lib.selector import Selector
from secret_santa_lib.sms_client import SmsClient, from_config


if __name__ == '__main__':
    print('Ho ho ho! Let\'s assign some santas!')
    print()

    client: SmsClient = from_config()
    print(f'carrier options: {SmsClient.get_carriers()}')
    print()

    selector: Selector = Selector(client)

    add_santa: bool = True
    while add_santa:
        name: str = input('name: ')
        phone_number: str = input('phone number: ')
        carrier: str = input('carrier: ')
        selector.add_santa(name, phone_number, carrier)
        add_santa = input('Would you like to add another? (Y/n) ') == 'Y'
        print()

    print('Assigning and notifying santas...')
    selector.select_and_notify_santas()
    print()

    print('All done!')

