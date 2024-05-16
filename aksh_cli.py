from aksh_domain import calculate_risk_of_sequela
from aksh_data import save_result_to_csv
import datetime
import argparse


def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("-f", "--file", required=True, dest="file")
    args = argument_parser.parse_args()

    gospitalization_date = datetime.datetime.now()
    name = input("Введите имя пациента:")
    second_name = input("Введите фамилию пациента:")
    surname = input("Введите отчество пациента:")
    sex = bool(input("Введите пол пациента(1-муж, 0-жен):"))
    age = int(input("Введите возраст:"))
    lg = int(input("Введите давление в лёгочной артерии (мм ртут столба):"))
    ka = int(input("Введите степень поражения коронарных артверий:"))
    bleeding = int(input("Bleeding:"))
    charlstone = int(input("Charlstone:"))
    es = int(input("EuroScore:"))
    sequella = bool(input("Ослажнения:"))
    dindo = int(input("Dindo (1-6):"))
    access = bool(input("Доступ:"))
    joint = bool(input("Швы:"))

    risk_cf = calculate_risk_of_sequela(age, lg, ka, bleeding, charlstone, es, sequella, dindo, access, joint)
    print(f"Какая-то хуета:{risk_cf}")
    if risk_cf > -0.650215:
        print("Осложнения маловероятны")
    else:
        print("Прогнозируется наличие осложнений")

    save_result_to_csv(args.file,
                       [name, second_name, surname, sex, gospitalization_date, age, lg, ka, bleeding, charlstone, es, sequella,
                 dindo, access, joint, risk_cf])


if __name__ == "__main__":
    main()
