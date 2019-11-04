"""
Here there are tow functions which are responsible for slicing data from the filtered JSON object
and Showing data in console
"""


# this function is responsible for showing the output in console
def printing(object):
    for index, item in enumerate(object):
        print("Record ", str(index + 1))
        print("-" * 50)

        for key, value in item.items():
            print(str(key) + " : " + str(value))

        print("-" * 50)


main_array = []


# this function is responsible for slicing data from the filtered data object
def get_arrays(type, data_object):
    if type == 'user':
        ticket_records = ''
        organization_records = ''
        user_data = []
        for element in data_object:
            if element.get('ticket_records'):
                ticket_records = element.get('ticket_records')
                del element['ticket_records']
            else:
                ticket_records = []
            if element.get('organization_records'):
                organization_records = element.get('organization_records')
                del element['organization_records']
            else:
                organization_records = []
            user_data.append(element)

        for user_item in user_data:
            for organization_item in organization_records:
                if str(user_item.get('organization_id')) == str(organization_item.get('_id')):
                    for key, value in organization_item.items():
                        user_item[str(key) + "_org"] = value
            for ticket_item in ticket_records:
                if str(ticket_item.get('submitter_id')) == str(user_item.get('_id')) or str(
                        ticket_item.get('assignee_id')) == str(user_item.get('_id')):
                    for key, value in ticket_item.items():
                        user_item[str(key) + "_ticket"] = value
                else:
                    pass
            main_array.append(user_item)

        # print(main_array)
        printing(main_array)

    if type == 'org':
        ticket_records = ''
        organization_records = []
        user_data = ''

        for element in data_object:
            if element.get('user_records'):
                user_data = element.get('user_records')
                del element['user_records']
            else:
                user_data = []
            if element.get('ticket_records'):
                ticket_records = element.get('ticket_records')
                del element['ticket_records']
            else:
                ticket_records = []

            organization_records.append(element)

        for organization_item in organization_records:
            for user_item in user_data:
                if str(organization_item.get('_id')) == str(user_item.get('organization_id')):
                    for key, value in user_item.items():
                        organization_item[str(key) + "_user"] = value
                else:
                    pass

            for ticket_item in ticket_records:
                if str(ticket_item.get('organization_id')) == str(organization_item.get('_id')):
                    for key, value in ticket_item.items():
                        organization_item[str(key) + "_ticket"] = value
                else:
                    pass
            main_array.append(organization_item)
        # print(main_array)
        printing(main_array)

    if type == 'ticket':
        ticket_records = []
        organization_records = ''
        user_data = ''

        for element in data_object:
            if element.get('user_records'):
                user_data = element.get('user_records')
                del element['user_records']
            else:
                user_data = []
            if element.get('organization_records'):
                organization_records = element.get('organization_records')
                del element['organization_records']
            else:
                organization_records = []

            ticket_records.append(element)

        for ticket_item in ticket_records:
            for user_item in user_data:
                if str(user_item.get('_id')) == str(ticket_item.get('submitter_id')) or str(
                        user_item.get('_id')) == str(ticket_item.get('assignee_id')):
                    for key, value in user_item.items():
                        ticket_item[str(key) + "_user"] = value
                else:
                    pass

            for organization_item in organization_records:
                if str(organization_item.get('_id')) == str(ticket_item.get('organization_id')):
                    for key, value in organization_item.items():
                        ticket_item[str(key) + "_org"] = value

                else:
                    pass

            main_array.append(ticket_item)
            printing(main_array)


""" END """
# this function is responsible for slicing data from the filtered data object
# def get_arrays(type, data_object):
#     # based on the type taking the data and passing those data to printing function
#     if type == 'user':
#         ticket_data = []
#         organization_data = []
#         user_data = []
#         for item in data_object:
#             ticket_data = item.get('ticket_records')
#             organization_data = item.get('organization_records')
#             del item['ticket_records']
#             del item['organization_records']
#             user_data.append(item)
#
#         # print(user_data)
#         # print(ticket_data)
#         # print(organization_data)
#         printing(user_data, ticket_data, organization_data)
#
#     elif type == 'org':
#         ticket_data = []
#         organization_data = []
#         user_data = []
#
#         for item in data_object:
#             ticket_data = item.get('ticket_records')
#             user_data = item.get('user_records')
#             del item['ticket_records']
#             del item['user_records']
#             organization_data.append(item)
#         printing(user_data, ticket_data, organization_data)
#
#     elif type == 'ticket':
#         ticket_data = []
#         organization_data = []
#         user_data = []
#
#         for item in data_object:
#             organization_data = item.get('organization_records')
#             user_data = item.get('user_records')
#             del item['organization_records']
#             del item['user_records']
#             ticket_data.append(item)
#         printing(user_data, ticket_data, organization_data)


# print(main_array)

# print(main_array)

# this function is responsible for showing the output in console
# def printing(user_data, ticket_data, organization_data):
#     for index, data in enumerate(user_data):
#         print("-" * 40)
#         print("User Record " + str(index + 1))
#         print("-" * 40)
#         print("_id " + " : " + str(data.get('_id')))
#         print("url " + " : " + str(data.get('url')))
#         print("external_id " + " : " + str(data.get('external_id')))
#         print("name " + " : " + str(data.get('name')))
#         print("alias " + " : " + str(data.get('alias')))
#         print("created_at " + " : " + str(data.get('created_at')))
#         print("active " + " : " + str(data.get('active')))
#         print("verified " + " : " + str(data.get('verified')))
#         print("shared " + " : " + str(data.get('shared')))
#         print("locale " + " : " + str(data.get('locale')))
#         print("timezone " + " : " + str(data.get('timezone')))
#         print("last_login_at " + " : " + str(data.get('last_login_at')))
#         print("email " + " : " + str(data.get('email')))
#         print("phone " + " : " + str(data.get('phone')))
#         print("signature " + " : " + str(data.get('signature')))
#         print("organization_id " + " : " + str(data.get('organization_id')))
#         print("tags " + " : " + str(data.get('tags')))
#         print("suspended " + " : " + str(data.get('suspended')))
#         print("role " + " : " + str(data.get('role')))
#         print("-" * 40)
#     for index_ticket, ticket_item in enumerate(ticket_data):
#         print("Ticket Record " + str(index_ticket + 1))
#         print("-" * 40)
#         print("_id " + " : " + str(ticket_item.get('_id')))
#         print("url " + " : " + str(ticket_item.get('url')))
#         print("external_id " + " : " + str(ticket_item.get('external_id')))
#         print("created_at " + " : " + str(ticket_item.get('created_at')))
#         print("type " + " : " + str(ticket_item.get('type')))
#         print("subject " + " : " + str(ticket_item.get('subject')))
#         print("description " + " : " + str(ticket_item.get('description')))
#         print("priority " + " : " + str(ticket_item.get('priority')))
#         print("status " + " : " + str(ticket_item.get('status')))
#         print("submitter_id " + " : " + str(ticket_item.get('submitter_id')))
#         print("assignee_id " + " : " + str(ticket_item.get('assignee_id')))
#         print("organization_id " + " : " + str(ticket_item.get('organization_id')))
#         print("tags " + " : " + str(ticket_item.get('tags')))
#         print("has_incidents " + " : " + str(ticket_item.get('has_incidents')))
#         print("due_at " + " : " + str(ticket_item.get('due_at')))
#         print("via " + " : " + str(ticket_item.get('via')))
#         print("-" * 40)
#     for index_org, organization_item in enumerate(organization_data):
#         print("Organization Record " + str(index_org + 1))
#         print("-" * 40)
#         print("_id " + " : " + str(organization_item.get('_id')))
#         print("url " + " : " + str(organization_item.get('url')))
#         print("external_id " + " : " + str(organization_item.get('external_id')))
#         print("name " + " : " + str(organization_item.get('name')))
#         print("domain_names " + " : " + str(organization_item.get('domain_names')))
#         print("created_at " + " : " + str(organization_item.get('created_at')))
#         print("details " + " : " + str(organization_item.get('details')))
#         print("shared_tickets " + " : " + str(organization_item.get('shared_tickets')))
#         print("tags " + " : " + str(organization_item.get('tags')))
#         print("-" * 40)
#     print("End")
