
print("Hello World")

myname = "Monali"

print(f"Hello {myname}! How are you?")

#f means format

def hello_name(somename):
    print(f"Hello {somename}! This is a function.")

def repeat_hello(somename, n_times):
    for i in range(n_times):
        print(f"Hello there {somename}! This is print statement number: {i+1}")

if __name__ == "__main__":
    hello_name("Monali")
    hello_name("Shipra")
    hello_name("Sangita")

    repeat_hello("Sangita", 6)