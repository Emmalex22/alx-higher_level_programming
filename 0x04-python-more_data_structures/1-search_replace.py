#!/usr/bin/python3
def search_replace(my_list, search, replace):
    neo_list = []
    for x in my_list:
        if x == search:
            neo_list.append(replace)
        else:
            neo_list.append(x)
    return neo_list
