import text


def show_main_menu()-> int:
    for i, item in enumerate(text.main_menu):
        if i:
            print(f'\t{i}. {item}')
        else:
            print(item)
    while True:
        choise = input(text.choise_main_menu)
        if choise.isdigit() and 0 < int(choise) < len(text.main_menu):
            return int(choise)
        print(text.choise_main_menu_error)

def show_contacts(phone_book: dict, error_message):
    if phone_book:
        print('\n' + '=' * 71)
        for u_id, contact in phone_book.items():
            print(f'{u_id:>3}. {contact[0]:<20} | {contact[1]:<20} | {contact[2]:<20}')
        print('=' * 71+ '\n')
    else:
        show_message(error_message)


def show_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')

def input_data(message) -> list[str] | str:
    if isinstance(message, str):
        return input('\n' + message)
    return [input(mes) for mes in message]

