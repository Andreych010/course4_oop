from utils import *


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
        print('Load 0%...')
        sj_vac = SJVacancy(vacancy)
        sj_vac.to_json() #сохраняем данные из сервиса SuperJob,по ключевому слову, в файл 'sjvacancy.json'
        print('Load 25%...')
        hh_vac = HHVacancy(vacancy)
        hh_vac.to_json() #сохраняем данные из сервиса HeadHunter,по ключевому слову, в файл 'hhvacancy.json'
        print('Load 50%...')
        all_vac = Vacancy(vacancy)
        all_vac.combine_json() #обьеденяем данные SuperJob и HeadHunter в файл 'all_vacancy.json'
        print('Load 100%')
        con = Connector('all_vacancy.json')
        mix = CountMixin('all_vacancy.json')
        count_vacancy = mix.get_count_of_vacancy #кол-во всех найденных вакансий
        if count_vacancy == 0:
            exit("Мы не нашли вакансий по заданным параметрам \U0001F910, программа закрыта."
                 "\nПопробуйте поискать вакансии по другому ключевому слову")
        print(f'Мы нашли для вас {count_vacancy} вакансий')
        count = input('Cделайте выбор:\n1-Просмотреть все вакансии\n2-Просмотреть Топ вакансий\n')
        if count == '2':
            count_choise = input('Введите кол-во вакансий для вывода Топ\n')
            sorted_vacancy = con.sort_salary_max()
            vacancy_list(count_choise, sorted_vacancy) #функция класса Vacancy_list выводит строковое представление по заданным атрибутам
            Vacancy.del_json()
            print('Спасибо, что воспользовались нашим сервисом. \nВозвращайтесь в любое время.')
            break
        elif not count.isdigit() or count > '2':
            exit('Вы ввели неверные параметры запроса.Программа закрыта')
        choise_salary = input('Выберите как производить сортировку зарплпты:\n1-по максимальной\n2-по минимальной\n')
        if not count.isdigit() or count > '2':
            exit('Вы ввели неверные параметры запроса.Программа закрыта')
        elif choise_salary == '1':
            sorted_vacancy = con.sort_salary_max()
            vacancy_list(count_vacancy, sorted_vacancy)
        elif choise_salary == '2':
            sorted_vacancy = con.sort_salary_min()
            vacancy_list(count_vacancy, sorted_vacancy)
        Vacancy.del_json()
        print('Спасибо, что воспользовались нашим сервисом. \nВозвращайтесь в любое время.')
        break


if __name__ == '__main__':
    main()
