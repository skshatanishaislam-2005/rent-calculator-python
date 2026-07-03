Contact = { }

while True:
    print('\n Contact Book App')
    print('1. Create Contact ')
    print('2. View Contact')
    print('3. Update Contact')
    print('4. Delete Contact')
    print('5. Search Contact')
    print('6. Count Contact')
    print('7. Exit')

    choice = input("Enter your choice = ")
    
    if choice == '1':
        name = input("Enter Your Name = ")
        if name in Contact:
            print(f"Contact name {name} already exist")
        else:
            age = int(input("Enter your age = "))
            email = input("Enter your email id = ")
            mobile = int(input("Enter your mobile number = "))
            Contact[name] = {'age': int(age) , 'email': input(email) , 'mobile': int(mobile)}
            print(f'Contacts name {name} has been created successfully!')

    elif choice == '2':
        name = input("Enter contact name to view contact  = ")
        if name in Contact:
            contacts = Contact[name]
            print(f"Name: {name}, Age : {age}, Mobile Number: {mobile}")
        else:
            print("contact not found!")

    elif choice == '3':
        name = input("Enter name to update contact  = ")
        if name in Contact:
            age = int(input("Enter your age = "))
            email = input("Enter your email id = ")
            mobile = int(input("Enter your mobile number = "))
            Contact[name] = {'age': int(age), 'email': email, 'mobile': mobile}
        else:
            print('Contact Not Found!')

    elif choice == '4':
        name = input("Enter the name you want to delete = ")
        if name in Contact:
            del Contact[name]
            print(f"Contact name {name} has been deleted successfully! ")
        else:
            print('Contact not found!')

    elif choice == '5':
        search_name = input("Enter the name to search = ")
        found = False
        for name, contacts in Contact.items():
            if search_name.lower() in name.lower():
                print(f'Found - Name {name}, Age: {age}, Mobile Number: {mobile}, Email Id: {email}')
                found = True
        if not found:
            print("No Contact Found With That Name!")
    
    elif choice == '6':
        print(f"Total Contact in your book: {len(Contact)}")
     
    elif choice == '7':
        print("BYE....BYE.....BYE.........THE PROGRAM IS NOW CLOSED")
        break

    else:
        print("INVAILD INPUT!!!")

    






