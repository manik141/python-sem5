# Date = 19/10/20203
# WAP to convert temperature to and from Clesiuc to Fahrenheit
'''
while True:
    print("\tMenu")
    print("1. To convert from Clesius to Fahrenheit")
    print("2. To convert from Fahrenheit to Clesius")
    print("3. Exit")
    choice = int(input("Enter choice: "))
    if choice== 1:
        tmp = float(input("Enter temperature in Clesius : "))
        print("In Fahrenheit -> ",(9/5*tmp) + 32)
    elif choice == 2:
        tmp = float(input("Enter temperature in Fahrenheit : "))
        print("In Clesius ->",round((tmp-32)*5/9))
    elif choice ==3:
        print("Exit program. GoodBye!")
        break
    else:
        print("Invalid choice. Try again")
'''
            #OR

def clesius_to_fahrenheit(clesius):
    #Convert temperature from Clesius to Fahrenheit.
    return (clesius *9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    #Convert temperature from Fahrenheit to Clesius.
    return (fahrenheit - 32) *5/9

#Main function to take user input and perform conversions
def main():
    print("Temperature Conversion Program")
    print("1. Clesius to Fahrenheit")
    print("2. Fahrenheit to Clesius")
    choice = int(input("Enter choice: "))
    if choice== 1:
        clesius = float(input("Enter temperature in Clesius : "))
        fahrenheit = clesius_to_fahrenheit(clesius)
        print(f"{clesius} Clesius is equal to {fahrenheit} Fahrenheit")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit : "))
        clesius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} Fahrenheit is equal to {clesius} Clesius")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()