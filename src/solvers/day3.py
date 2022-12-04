def solve_part_1(data):
    priorities = 0
    for rucksack in data:
        items = len(rucksack)
        first_rucksack, second_rucksack = rucksack[items // 2:], rucksack[:items // 2]
        common_items = ''.join(set(first_rucksack).intersection(second_rucksack))
        for item in common_items:
            priorities += __get_item_priority(item)
    return priorities


def solve_part_2(data):
    priorities = 0
    for i in range(0, len(data), 3):
        first_rucksack = data[i]
        second_rucksack = data[i + 1]
        third_rucksack = data[i + 2]
        common_items = ''.join(set(first_rucksack).intersection(second_rucksack).intersection(third_rucksack))
        for item in common_items:
            priorities += __get_item_priority(item)
    return priorities


def __get_item_priority(item):
    if item.islower():
        # a-z should have priority 1-26
        return ord(item) - 96
    else:
        # A-Z should have priority 27-56
        return ord(item) - 38
