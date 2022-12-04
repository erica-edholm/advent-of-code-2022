def solve_part_1(data):
    section_overlap_count = 0
    for pairs in data:
        first_section_assignment, second_section_assignment = tuple(pairs.split(','))
        first_sections = __get_sections(first_section_assignment)
        second_sections = __get_sections(second_section_assignment)
        if __is_full_section_overlap(first_sections, second_sections):
            section_overlap_count += 1
    return section_overlap_count


def solve_part_2(data):
    section_overlap_count = 0
    for pairs in data:
        first_section_assignment, second_section_assignment = tuple(pairs.split(','))
        first_sections = __get_sections(first_section_assignment)
        second_sections = __get_sections(second_section_assignment)
        if __is_any_section_overlap(first_sections, second_sections):
            section_overlap_count += 1
    return section_overlap_count


def __get_sections(section: str):
    section_start, section_stop = tuple(section.split('-'))
    return list(range(int(section_start), int(section_stop) + 1))


def __is_full_section_overlap(first_sections: list, second_sections: list):
    second_overlap_first = all(item in first_sections for item in second_sections)
    first_overlap_second = all(item in second_sections for item in first_sections)
    return first_overlap_second or second_overlap_first


def __is_any_section_overlap(first_sections: list, second_sections: list):
    overlap = any(item in first_sections for item in second_sections)
    return overlap
