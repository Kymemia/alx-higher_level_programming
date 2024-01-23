#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for x in range(list_length):
        try:
            div = my_list_1[x] / my_list_2[x]
        except Exception as j:
            if isinstance(j, TypeError):
                print("wrong type")
            elif isinstance(j, ZeroDivisionError):
                print("division by 0")
            elif isinstance(j, IndexError):
                print("out of range")
            else:
                print("other exception:", j)
            div = 0
        finally:
            new_list.append(div)
    return new_list
