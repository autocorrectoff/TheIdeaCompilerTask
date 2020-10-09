from datetime import datetime
import random
import math
import sys
from insertion_sort import sort_dates
from radix_sort import sort_strings

def sort_by_gender_and_lastname_asc(records):
    females = []
    males = []
    for record in records:
        if record["gender"].lower() == "female":
            females.append(record)
        if record["gender"].lower() == "male":
            males.append(record)
    sorted_females = sort_strings(females, "l_name", 3)
    sorted_males = sort_strings(males, "l_name", 3)
    return sorted_females + sorted_males

def sort_by_lastname_desc(records):
    return list(reversed(sort_strings(records, "l_name", 3)))

def generate_file_name():
    seed = random.randrange(sys.maxsize)
    random.seed(seed)
    return "output/output-{}.txt".format(math.floor(random.random() * 100000))

def output_to_file(records, output_file, heading):
    with open(output_file, "a") as fout:
        fout.write("{}\n".format(heading))
        fout.write("--------------------------\n\n")
        for record in records:
            line = "{}\t\t{}\t\t{}\t\t{}\t\t{}\n".format(record["l_name"], record["f_name"], record["gender"], record["birth_date"].strftime("%m/%d/%Y"), record["color"])
            fout.write(line)
        fout.write("--------------------------\n\n")   

def merge_records_lists(*records):
    all_records = []
    for list in records:
        all_records += list
    return all_records

def format_date(date_str, format):
    return datetime.strptime(date_str, format)

def format_gender(gender):
    if gender.upper() == "M":
        return "Male"
    elif gender.upper() == "F":
        return "Female"

def parse_space_file_records(records_lines):
    records = []
    for lines in records_lines:
        records_dict = {}
        split_record = lines.split()
        records_dict["l_name"] = split_record[0].strip()
        records_dict["f_name"] = split_record[1].strip()
        records_dict["gender"] = format_gender(split_record[3].strip())
        records_dict["birth_date"] = format_date(split_record[4].strip(), "%m-%d-%Y")
        records_dict["color"] = split_record[5].strip()
        records.append(records_dict)
    return records

def parse_pipe_file_records(records_lines):
    records = []
    for lines in records_lines:
        records_dict = {}
        split_record = lines.split("|")
        records_dict["f_name"] = split_record[1].strip()
        records_dict["l_name"] = split_record[0].strip()
        records_dict["gender"] = format_gender(split_record[3].strip())
        records_dict["color"] = split_record[4].strip()
        records_dict["birth_date"] = format_date(split_record[5].strip(), "%m-%d-%Y")
        records.append(records_dict)
    return records

def parse_comma_file_records(records_lines):
    records = []
    for lines in records_lines:
        records_dict = {}
        split_record = lines.split(",")
        records_dict["l_name"] = split_record[0].strip()
        records_dict["f_name"] = split_record[1].strip()
        records_dict["gender"] = split_record[2].strip()
        records_dict["color"] = split_record[3].strip()
        records_dict["birth_date"] = format_date(split_record[4].strip(), "%m/%d/%Y")
        records.append(records_dict)
    return records

def load_file_lines_as_strings(file_location):
    lines = []
    with open(file_location, "r") as fin:
        for line in fin:
            if line.isspace():
                continue
            lines.append(line.strip())
    return lines

def startup():
    # load file lines
    comma_file_lines = load_file_lines_as_strings("input/comma.txt")
    pipe_file_lines = load_file_lines_as_strings("input/pipe.txt")
    space_file_lines = load_file_lines_as_strings("input/space.txt")

    # split content by separators
    records_1 = parse_comma_file_records(comma_file_lines)
    records_2 = parse_pipe_file_records(pipe_file_lines)
    records_3 = parse_space_file_records(space_file_lines)

    # merge into single list
    records = merge_records_lists(records_1, records_2, records_3)
    #print(records)

    output_file = generate_file_name()

    # sort and save to file
    records_by_gender = sort_by_gender_and_lastname_asc(records)
    output_to_file(records_by_gender, output_file, "gender then lastname ascending")
    records_by_birthdate = sort_dates(records)
    output_to_file(records_by_birthdate, output_file, "dateofbirth ascending")
    records_by_last_name = sort_by_lastname_desc(records)
    output_to_file(records_by_last_name, output_file, "lastname descending")

    print("Saved output at: {}".format(output_file))

if __name__ == "__main__":
    startup()