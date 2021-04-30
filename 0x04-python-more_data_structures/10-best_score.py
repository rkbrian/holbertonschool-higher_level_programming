#!/usr/bin/python3
def best_score(a_dictionary):
    if bool(a_dictionary) is False:
        return None
    for j in a_dictionary:
        if a_dictionary[j] == max(list(a_dictionary[i] for i in a_dictionary)):
            maxwell = a_dictionary[j]
            return j
