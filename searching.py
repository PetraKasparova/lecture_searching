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
    """
    Creates dictionary of position and count of number
    :param unordered_numbers: (list), list of loaded data
    :param number: (int), number to be found
    :return: (dict), dictionary of position and count of number
    """
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


def pattern_search(dna_sequence, find_pattern):
    """
    Finds index of position of finding pattern
    :param dna_sequence: (str), loaded dna sequence
    :param find_pattern: (str), pattern to be found
    :return: (set), count of founded patterns
    """
    sequence_index = 0
    pattern_lenght = len(find_pattern)
    count_of_patterns = set()
    m = len(find_pattern)
    while sequence_index < len(dna_sequence) - (len(find_pattern) + 1):
        pattern_index = 0
        while pattern_index < m:
            if dna_sequence[sequence_index + pattern_index] != find_pattern[pattern_index]:
                break
            pattern_index += 1

        if pattern_index == m:
            count_of_patterns.add(sequence_index + (pattern_lenght//2))
        sequence_index += 1


    return count_of_patterns


def main():
    unordered_numbers = read_data("sequential.json", "unordered_numbers")
    print(unordered_numbers)

    number = 9
    final_dictionary = linear_search(unordered_numbers, number)
    print(final_dictionary)

    dna_sequence = read_data("sequential.json",  "dna_sequence")
    find_pattern = "ATA"
    searching_pattern = pattern_search(dna_sequence, find_pattern)
    print(searching_pattern)


if __name__ == '__main__':
    main()