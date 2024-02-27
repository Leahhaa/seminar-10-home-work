main_menu = ['Главное меню',
             'Открыть телефонную книгу',
             'Сохранить контакт',
             'Покказать контакты',
             'Создать контакты',
             'Найти контакты',
             'Изменить контакты',
             'Удалить контакты',
             'Выход']

choise_main_menu = f'Выберите пункт меню ({1}-{len(main_menu)-1}): '
choise_main_menu_error = f'Нужно ввксти число от 1 до {len(main_menu)-1})!'

phone_book_opened_successeful = 'Телефонная книга открыта успешно!'
phone_book_saved_successeful = 'Телефонная книга успешно сохранена!'

empty_phone_book_error = 'Телефонная книга пуста или не открыта!'
 
input_new_contact = ['Введиет имя контакта: ',
                     'Введите номер контакта: ',
                     'Введите комент контакта: ']


no_changes = 'Или ENTER , чтобы оставить без изменений'

edit_contact  = [f'Введите новое имя ({no_changes}): ',
         f'Введите новое телефон ({no_changes}): ',
         f'Введите новое коменнт ({no_changes}): ',]



input_search_word = 'Введите слово для поиска: '
input_search_word_for_edit = 'Введите слово для поиска, который хотите изменить: '
input_search_word_for_delete = 'Введите слово для поиска, который хотите удалить: '
input_id_for_edit = 'Введите айди контакта который хотите изменить: '
input_id_for_delete = 'Введите айди контакта который хотите удалить: '



def new_contact_added_successful(name):
    return f'Контакт "{name}" успешно добавлен!'

def find_contact_no_result(word):
    return f'Контакты содержашие "{word}" не найдены'

def edit_contact_successful(name) ->str:
    return f'Конаткт "{name}" успешно изменён'


def delete_contact_successful(name) ->str:
    return f'Конаткт "{name}" успешно удалён'