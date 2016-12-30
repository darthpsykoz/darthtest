def stringtoint(input_string):
    num_list = []
    for i in input_string.split():
        num_list.append(int(i))
    print(type(num_list), type(num_list[1]))
    return num_list

#def inttodec(input_int):
test_string = '2 5 6 7 123 252'

print(test_string)



print(stringtoint(test_string))