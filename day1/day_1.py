import json
import pdb
import numpy as np


def get_elf_calorie_sums(data):
    elf_calorie_sums = []
    for elf in data:

        elf_inventory_string = elf.split("\n")
        elf_inventory = [int(numeric_string) for numeric_string in elf_inventory_string]

        elf_calorie_sums.append(sum(elf_inventory))

    return elf_calorie_sums


def elf_with_most_calories(summed_data):

    elf_max_cals = max(summed_data)
    elf_with_max_cals = summed_data.index(elf_max_cals)
    return "elf #" + str(elf_with_max_cals) + " has the most calories (" + str(elf_max_cals)+ ") in their inventory!"


def top_three_calorie_elves(summed_data):
    sorted_array = np.sort(summed_data)
    rev_sorted_array = sorted_array[::-1]
    return rev_sorted_array[0:3]


if __name__ == '__main__':

    # read data
    f = open('data.txt')
    lines = f.read()
    f.close()

    # print(lines)
    elves = lines.split("\n\n")
    elf_calorie_sums = get_elf_calorie_sums(elves)

    print(elf_with_most_calories(elf_calorie_sums))
    print("top three elf calorie stores: ", top_three_calorie_elves(elf_calorie_sums))
    print("total of the top three: ", sum(top_three_calorie_elves(elf_calorie_sums)))

    # print(elf_with_most_calories(elves))

    # print(top_three_calorie_elves(elves))
