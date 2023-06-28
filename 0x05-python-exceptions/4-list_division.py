#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    for itr in range(list_length):
        result = 0
        try:
            result = my_list_1[itr] / my_list_2[itr]
        except (ValueError, TypeError):
            print("wrong type")
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            my_list.append(result)
    return my_list
