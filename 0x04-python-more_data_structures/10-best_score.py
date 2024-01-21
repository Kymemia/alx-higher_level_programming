#!/usr/bin/python3
def best_score(a_dictionary):
    return a_dictionary and max(a_dictionary, key=a_dictionary.get) or None
