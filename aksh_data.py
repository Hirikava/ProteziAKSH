import csv


def save_result_to_csv(file_name: str, params):
    with open(file_name, "a") as file:
        csv_writer = csv.writer(file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(params)

