
test_string = '2 5 6 7 123 252'

print(test_string)

print(stringtoint(test_string))

def stringtoint(input_string):
    list_form = int(input_string.split())
    return list_form

