
def is_prime(input_number):
    list_of_numbers_from_2_to_nminusone = list(range(2,input_number))
    print(f"list of numbers = {list_of_numbers_from_2_to_nminusone}")
    for number in list_of_numbers_from_2_to_nminusone:
        if input_number % number == 0:
            return False
    return True


if __name__=="__main__":
    print("This is a file for testing prime number")


    input_numbers = [2,3,4,5,6,7,8,9,10,11,12]
    for num in input_numbers:
        if is_prime(num):
           print(f" Input number is {num}. It is a prime number")

        else:
           print(f" Input number is {num}. It is not a prime number")

