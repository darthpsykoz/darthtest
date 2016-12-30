def stringtoint(input_string):
    num_list = []
    for i in input_string.split():
        num_list.append(int(i))
    print(type(num_list), type(num_list[1]))
    return num_list

def inttodec(input_int):
    output_dec = float(input_int)
    return output_dec

