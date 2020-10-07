#!/usr/bin/env python3

from datetime import date

def scan(txt):
    print(txt, end='')
    return input()

def send(txt):
    global file_number
    file_name = "ev-report/adds/f" + str(file_number)
    print(file_name, txt)
    with open(file_name, "w") as f:
        f.write(str(txt))
    file_number += 1

def lab_num_course():
    number = scan("Отчёт по лабораторной работе № ")
    course = scan("по курсу ")
    send(number)
    send(course)
    

month_ru = {
    1 : "января",
    2 : "февраля",
    3 : "марта",
    4 : "апреля",
    5 : "мая",
    6 : "июня",
    7 : "июля",
    8 : "августа",
    9 : "сентября",
    10 : "октября",
    11 : "ноября",
    12 : "декабря"
}        

def stud():
    group = scan("Студент группы ")
    fio = scan("ФИО ")
    number = scan("№ по списку ")
    contacts = scan("Контакты www, e­mail, telegram: ")
    date_today = date.today()
    day = date_today.day
    month = month_ru[date_today.month]
    year = date_today.year
    

    
    send(group)
    send(fio)
    send(number)
    send(contacts)
    send(day)
    send(month)
    send(year)

def teacher():
    doc = scan("Преподаватель (должность): ")
    name = scan("ФИО: ")
    send(doc)
    send(name)

def preamble():
    theme = scan("Тема: ")
    aim = scan("Цель работы: ")
    variant = scan("Вариант: ")
    task = scan("Задание: ")
    send(theme)
    send(aim)
    send(variant)
    send(task)

def idea():
    print("Идея, метод, алгоритм решения задачи(в формах: словесной, псевдокода, графической [блок­схема, диаграмма, рисунок, таблица] или формальные спецификации с пред­ и постусловиями)")
    idea = input()

def scenario():
    print("Сценарий выполнения работы [план работы, первоначальный текст программы в черновике (можно на отдельном листе) и тесты либо соображения по тестированию].")
    idea = input()

def proto():
    proto = scan("Файл с протоколом: ")

from os import system
    
def main():
    global file_number
    file_number = 1
    lab_num_course()
    stud()
    teacher()
    preamble()
    idea()
    scenario()
    
    system("cd ev-report; xelatex report.tex")
    
if __name__ == "__main__":
    main()
