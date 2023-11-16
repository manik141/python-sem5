database=[]
def add_record(name,age,city):
    record=(name,age,city)
    database.append(record)
    print("Record added successfully")

def display_records():
    print("Database record")
    for record in database:
        print("Name:",record[0])
        print("Age:",record[1])
        print("City:",record[2])
        print("-"*20)
while True:
    print("\nMenu:")
    print("1.Add Record")
    print("2.Display Record")
    print("3.Exit")
    choice=input("Enter your choice:")
    if choice=='1':
        name=input("Enter name: ")
        age=input("Enter age: ")
        city=input("Enter city: ")
        add_record(name,age,city)
    elif choice=='2':
        display_records()
    elif choice=='3':
        print("Exiting the program.Goodbye!")
        break
    else:
        print("Invalid choice. Please try again")
        