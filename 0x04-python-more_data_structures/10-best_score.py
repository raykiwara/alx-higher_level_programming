#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        keys = list(a_dictionary.keys())
        score = 0
        leader = ""
        for i in keys:
            if a_dictionary[i] > score:
                score = a_dictionary[i]
                leader = i
        return leader
    else:
        return None
