import file_operation
import Note
import ui
import os
import time

number = 6  # сколько знаков МИНИМУМ может быть в тексте заметки

class Clear_time_sleep:
    def time_sleep():
        time.sleep(1)
    def clear():
        os.system('cls')
    

def add():
    note = ui.create_note(number)
    array = file_operation.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_operation.write_file(array, 'a')
    Clear_time_sleep.time_sleep()
    Clear_time_sleep.clear()
    print('Заметка добавлена...')
    Clear_time_sleep.time_sleep()
    Clear_time_sleep.clear()

def show(text):
    logic = True
    array = file_operation.read_file()
    if text == 'date':
        Clear_time_sleep.time_sleep()
        Clear_time_sleep.clear()
        date = input('Введите дату в формате dd.mm.yyyy: ')
        Clear_time_sleep.time_sleep()
        Clear_time_sleep.clear()
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
    if logic == True:
        Clear_time_sleep.time_sleep()
        Clear_time_sleep.clear()
        print('Нет ни одной заметки...')
        Clear_time_sleep.time_sleep()
        Clear_time_sleep.clear()


def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    Clear_time_sleep.time_sleep()
    Clear_time_sleep.clear()

    array = file_operation.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note(number)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                Clear_time_sleep.time_sleep()
                Clear_time_sleep.clear()
                print('Заметка изменена...')
                Clear_time_sleep.time_sleep()
                Clear_time_sleep.clear()
            if text == 'del':
                array.remove(notes)
                Clear_time_sleep.time_sleep()
                Clear_time_sleep.clear()
                print('Заметка удалена...')
                Clear_time_sleep.time_sleep()
                Clear_time_sleep.clear()
            if text == 'show':
                Clear_time_sleep.time_sleep()
                Clear_time_sleep.clear()
                print(Note.Note.map_note(notes))
                Clear_time_sleep.time_sleep()
                Clear_time_sleep.clear()
    if logic == True:
        Clear_time_sleep.time_sleep()
        Clear_time_sleep.clear()
        print('Такой заметки нет, возможно, вы ввели неверный id')
        Clear_time_sleep.time_sleep()
        Clear_time_sleep.clear()
    file_operation.write_file(array, 'a')
