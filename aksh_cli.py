from aksh_domain import calculate_risk_of_sequela
from aksh_data import save_result_to_csv
import datetime
import argparse


def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("-f", "--file", required=True, dest="file")
    args = argument_parser.parse_args()

    gospitalization_date = datetime.datetime.now()
    second_name = input("Введите фамилию пациента:")
    name = input("Введите имя пациента:")
    surname = input("Введите отчество пациента:")
    sex = bool(input("Введите пол пациента(1 - Мужской, 0 - Женский):"))
    age = int(input("Введите возраст пациента:"))
    lg = int(input("Введите давление в лёгочной артерии (мм.рт.ст.):"))
    ka = int(input("Введите степень поражения коронарных артерий(в %):"))
    bleeding = int(input("Интраоперационная кровопотеря (мл.):"))
    charlstone = int(input("Индекс коморбидности Чарлсона:"))
    es = float(input("Риск по EuroScore (в %):"))
    sequella = bool(input("Наличие других осложнений (0 - нет осложнений, 1 - есть осложнения):"))
    dindo = int(input("Класс хирургических осложнений по Clavien-Dindo (1-5):"))
    access = bool(input("Хиругический доступ (0 - доступ симметричен, 1 - доступ несимметричен):"))
    joint = bool(input("Наложение швов (0 - швы наложены симметрично, 1 - швы наложены несимметрично:"))

    risk_cf = calculate_risk_of_sequela(age, lg, ka, bleeding, charlstone, es, sequella, dindo, access, joint)
    print(f"Результат:{risk_cf}")
    if risk_cf > -0.650215:
        print("Осложнения маловероятны")
    else:
        print("Прогнозируется наличие осложнений")

    save_result_to_csv(args.file,
                       [name, second_name, surname, sex, gospitalization_date, age, lg, ka, bleeding, charlstone, es, sequella,
                 dindo, access, joint, risk_cf])


if __name__ == "__main__":
    main()
