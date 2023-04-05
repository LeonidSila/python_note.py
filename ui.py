import Note
import function
    
def create_note(number):
    function.Clear_time_sleep.time_sleep()
    function.Clear_time_sleep.clear()
    title = check_len_text_input(
        input('Введите название: '), number)
    body = check_len_text_input(
        input('Введите описание заметки: '), number)
    function.Clear_time_sleep.time_sleep()
    function.Clear_time_sleep.clear()
    return Note.Note(title=title, body=body)


def menu():
    print("\n1 - Вывод всех заметок из файла\n2 - Добавление заметки\n3 - Удаление заметки\n4 - Редактирование заметки\n5 - Выборка заметок по дате\n6 - Показать заметку по id\n7 - Выход\n\nВведите номер: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        function.Clear_time_sleep.time_sleep()
        function.Clear_time_sleep.clear()
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
        function.Clear_time_sleep.time_sleep()
        function.Clear_time_sleep.clear()
    else:
        return text


def goodbuy():
    function.Clear_time_sleep.time_sleep()
    function.Clear_time_sleep.clear()
    print("Выход")
    function.Clear_time_sleep.time_sleep()
    function.Clear_time_sleep.clear()