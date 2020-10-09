def sort_dates(list):
    for i in range(len(list)):
        cursor = list[i]
        cursor_date = list[i]["birth_date"]
        pos = i
        while pos > 0 and list[pos - 1]["birth_date"] > cursor_date:
            list[pos] = list[pos - 1]
            pos = pos - 1
        list[pos] = cursor
    return list