#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    return max(a_dictionary, key=a_dictionary.get) if a_dictionary else None
