
from Class_2 import repeat_hello, hello_name

def print_even_up_to_number(input_number):
    list_of_numbers= list(range(1, input_number+1))
    print(list_of_numbers)
    for number in list_of_numbers:
        if number %2 ==0:
            print(number)



if __name__ == "__main__":
    print("Hello World")
    repeat_hello(somename="Monali", n_times= 5)
    hello_name(somename="Monali")

    list_of_names = ["Sangita", "John", "William"]
    for name in list_of_names:
        hello_name(name)
        #list variable

    number_list = (1, 2, 3,4,5)
    print(number_list)

    for number in number_list:
        print(number)

    print_even_up_to_number(21)





