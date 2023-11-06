from load_api import *
from utils import *
from DBManager import *


def main():
    print("Hello.")
    user_job = input("Which employer are you looking for?: ")
    api = HeadHunter_API(user_job)
    loading(api)

    api.get_info_via_API()
    api.get_id_employer()
    all_items = []
    # print(hh_api.all_id)
    for id in api.all_id:
        api.get_info_via_id(id)
        data_hh = api.final
        all_items.append(data_hh)

    merged_items = []
    for json_data in all_items:
        merged_items.extend(json_data.get('items', []))

    with open("json.json", "w", encoding='utf-8') as json_file:
        for item in merged_items:
            json.dump(item, json_file, ensure_ascii=False)
            json_file.write('\n')

    create_table(user_job)
    insert_values(user_job)
    manager = DBManager(user_job)
    print("---")
    print("Do you want to see all vacancies and employers?")
    print("Press '1' for 'yes'.")
    print("Press 'Enter' for 'no!. ")
    user_pick_q1 = input()
    if user_pick_q1 == "1":
        manager.get_companies_and_vacancies_count()
    print("---")
    print("Do you want to see all vacancies?")
    print("Press '1' for 'yes'.")
    print("Press 'Enter' for 'no!. ")
    user_pick_q2 = input()
    if user_pick_q2 == "1":
        manager.get_all_vacancies()
    print("---")
    print("Do you want to see average salary?")
    print("Press '1' for 'yes'.")
    print("Press 'Enter' for 'no!. ")
    user_pick_q3 = input()
    if user_pick_q3 == "1":
        manager.get_avg_salary()
    print("---")
    print("Do you want to see vacancies with above average salary?")
    print("Press '1' for 'yes'.")
    print("Press 'Enter' for 'no!. ")
    user_pick_q4 = input()
    if user_pick_q4 == "1":
        manager.get_vacancies_with_higher_salary()
    print("---")
    print("Do you want to see vacancies with a specific keyword?")
    print("Press '1' for 'yes'.")
    print("Press 'Enter' for 'no!. ")
    user_pick_q5 = input()
    if user_pick_q5 == "1":
        user_keyword = input("Keyword: ")
        manager.get_vacancies_with_keyword(user_keyword)

    print("That's all. Good bye.")


main()
