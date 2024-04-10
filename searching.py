import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
    return data[field]


def linear_search(unordered_numbers, number):
    index = 0
    position = []
    pocet_vyskytu = 0
    for numbers in unordered_numbers:
        if numbers == number:
            position.append(index)
            pocet_vyskytu += 1
        index += 1

    slovnik = {"positions":position, "count":pocet_vyskytu}
    return slovnik



def main():
    unordered_numbers = read_data("sequential.json", "unordered_numbers")
    print(unordered_numbers)
    number = 9
    final_dictionary = linear_search(unordered_numbers, number)
    print(final_dictionary)


if __name__ == '__main__':
    main()