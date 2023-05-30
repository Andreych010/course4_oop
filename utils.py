from classes import *


def vacancy_list(count, sorted_vacancy):
    '''
    Класс Vacancy_list выводит строковое представление по заданным атрибутам
    '''
    for i in range(int(count)):
        vac = Vacancy_list(sorted_vacancy[i]['source'], sorted_vacancy[i]['name'],
                           sorted_vacancy[i]['url'],
                           sorted_vacancy[i]['city'], sorted_vacancy[i]['requirement'],
                           sorted_vacancy[i]['currency'],
                           sorted_vacancy[i]['salary_from'], sorted_vacancy[i]['salary_to'])
        print(vac)