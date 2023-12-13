from secret_santa_lib.secret_santa_manager import SecretSantaManager


if __name__ == '__main__':
    print('Ho ho ho! Let\'s assign some santas!')
    print()

    manager: SecretSantaManager = SecretSantaManager()

    add_santa: bool = True
    while add_santa:
        name: str = input('name: ')
        email: str = input('email address: ')
        manager.add_participant(name, email)
        print()

        add_santa = 'Y' == input('Would you like to add another? (Y/n) ')
        print()

    print('assigning and notifying santas...')
    manager.assign_and_notify_participants()
    print()

    print('All done!')

