from classes import *


def main():
    while True:
        vacancy = input('Введите ключевое слово по которому будем искать вакансии:\n').replace(' ', '')
        if not vacancy.isalpha():
            print('Вы ввели не слово.')
            print('Для продолжения введите:\n1-для продолжени\n2-для выхода')
            answer = input()
            if answer == '1':
                continue
            elif answer == '2':
                exit('Возвращайтесь в любое время.')
        else:
            print('Идёт поиск вакансий на SuperJob...')
            sj_vac = SJVacancy(vacancy)
            sj_vac.to_json()
            print('Ищем вакансии на HeadHunter...')
            hh_vac = HHVacancy(vacancy)
            hh_vac.to_json()
            print('Формируем список\U0001F600...')
            all_vac = Vacancy(vacancy)
            all_vac.combine_json()
        con = Connector('all_vacancy.json')
        mix = CountMixin('all_vacancy.json')
        count_vacancy = mix.get_count_of_vacancy
        while True:
            if count_vacancy == 0:
                exit("Вакансий не нашлось, программа закрыта. Попробуйте поискать вакансию по другому ключевому слову")
            else:
                print(f'Мы нашли для вас {count_vacancy} вакансий')
                count = input('Введите количество вакансий, которые вы хотели бы посмотреть\n')
                if not count.isdigit() or int(count) == 0 or int(count) > count_vacancy:
                    print(f'Введите любое целое число больше ноля')
                    continue
                else:
                    sorted_vacancy = con.sort_salary()
                    items = []
                    for i in range(int(count)):
                        vac = Vacancy_list(sorted_vacancy[i]['source'], sorted_vacancy[i]['name'],
                                           sorted_vacancy[i]['url'],
                                           sorted_vacancy[i]['city'], sorted_vacancy[i]['requirement'],
                                           sorted_vacancy[i]['currency'],
                                           sorted_vacancy[i]['salary_from'], sorted_vacancy[i]['salary_to'])
                        items.append(vac)
                        print(vac)
                    break
        Vacancy.del_json()
        print('Спасибо, что воспользовались нашим сервисом. \nВозвращайтесь в любое время.')
        break

if __name__ == '__main__':
    main()
