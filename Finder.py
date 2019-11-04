"""
This is app capable of finding data from the json objects..
"""
from Hub import Hub
from formatter import get_arrays
import ReadJson

# making hub object. This is like a connector between the UserFinder and the functions in this file
hub = Hub()

# option showing and input taking
print("Hi, Chose an option to continue")
print("" * 4, "1. Press 1 for Searching")
print("" * 4, "2. Press 2 for List of Searchable")
print("" * 4, "3. Press 0 for Exit")
print("-" * 30)

option = input("Provide an Option: ")

# taking all the searchable keyword for lists
user_keys, ticket_keys, organization_keys = hub.get_keys()
# print(option)

# based on the options choosing the suitable actions
if int(option) == 0:
    print("Thank you for using..! ")
    exit()
elif int(option) == 1:
    selected = input("Press '1' of Users, Press '2' for Organizations, Press '3' for Tickets: ")
    keyword = input("Please enter the key word: ")
    value = input("Please enter the value: ")
    if int(selected) == 1:
        if keyword in user_keys:
            user_data = hub.find_user(keyword, value)

            if len(user_data) == 0:
                print("No data found")

            get_arrays('user', user_data)
            # get_test('user', user_data)
        else:
            print("Invalid keyword for users")
    elif int(selected) == 2:
        if keyword in organization_keys:
            org_data = hub.find_organization(keyword, value)
            if len(org_data) == 0:
                print("No data found")
            get_arrays('org', org_data)
            # get_test('org', org_data)
        else:
            print("Invalid key for organizations")
        
    elif int(selected) == 3:
        if keyword in ticket_keys:
            ticket_data = hub.find_ticket(keyword, value)

            if len(ticket_data) == 0:
                print("No data found")

            get_arrays('ticket', ticket_data)
            # get_test('ticket', ticket_data)
        else:
            print("Invalid key for tickets")
    else:
        print("Invalid Input")
        exit()
        
elif int(option) == 2:

    print("For Users:")
    print("-"*45)
    for key in user_keys:
        print(key)

    print("-" * 45)
    print("For Organizations:")
    print("-"*45)
    for key in organization_keys:
        print(key)
        
    print("-" * 45)
    print("For Tickets:")
    print("-" * 45)
    for key in ticket_keys:
        print(key)


else:
    print("Invalid Option. Thank you")
