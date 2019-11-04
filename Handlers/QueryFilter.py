import os
from ReadJson import json_read
from Helpers.Helpers import filter_by_other_keys, filter_by_status, filer_by_tags

# the base path for the particular directory
base_dir = r"C:\Users\ChampWk38\Desktop\JSONFilter\JsonStore"

# making the paths for the JSON stores
organization_path = os.path.join(base_dir, 'organizations.json')
user_path = os.path.join(base_dir, 'users.json')
tickets_path = os.path.join(base_dir, 'tickets.json')

# Loading the JSON data as a python dictionary
user_data_json_array = json_read(user_path)
ticket_data_json_array = json_read(tickets_path)
organization_data_json_array = json_read(organization_path)


# responsible for filtering the users.
def get_user(keyword, value):
    filterd_data = ""
    filtered_array = []
    ticket_data_array = []
    organization_data_array = []
    binary_list = ['active', 'verified', 'shared', 'suspended']
    if keyword == 'tags':
        # print("tags")
        filterd_data = filer_by_tags(user_data_json_array, keyword, value)
        # print(filterd_data)
    elif keyword in binary_list:
        filterd_data = filter_by_status(user_data_json_array, keyword, value)
        # print(filterd_data)
    else:
        filterd_data = filter_by_other_keys(user_data_json_array, keyword, value)
        # print(filterd_data)
        # exit()
    if filterd_data != 0:
        result_obj = {'tickets': [], 'orgz': []}
        try:
            for items in filterd_data:
                # print(items)
                ticket_data_assignee = filter_by_other_keys(ticket_data_array, 'assignee_id',
                                                            items.get('_id'))
                ticket_data_submitter = filter_by_other_keys(ticket_data_json_array, 'submitter_id',
                                                             items.get('_id'))
                orgdata = filter_by_other_keys(organization_data_json_array, '_id', items.get('organization_id'))

                if len(ticket_data_assignee) != 0:
                    result_obj['tickets'].append(ticket_data_assignee[0])
                    ticket_data_array.append(ticket_data_assignee[0])

                if len(ticket_data_submitter) != 0:
                    # tickets.append(ticket_data_submitter[0])
                    result_obj['tickets'].append(ticket_data_submitter[0])
                    ticket_data_array.append(ticket_data_submitter[0])

                if len(orgdata) != 0:
                    result_obj['orgz'].append(orgdata[0])
                    organization_data_array.append(orgdata[0])
                else:
                    pass
                items['ticket_records'] = result_obj['tickets']
                items['organization_records'] = result_obj['orgz']

                # print(items)

                filtered_array.append(items)
            return filtered_array
        except Exception as e:
            print("error occurred in user filtering")
            print(e)
            return []
    else:
        return []


# responsible for filering organizations
def get_organization(keyword, value):
    filted_array = ''
    ticket_array = []
    user_array = []
    filtered_array = []

    if keyword == 'domain_names' or keyword == 'tags':
        filted_array = filer_by_tags(organization_data_json_array, keyword, value)
    elif keyword == 'shared_tickets':
        filted_array = filter_by_status(organization_data_json_array, keyword, value)
    else:
        filted_array = filter_by_other_keys(organization_data_json_array, keyword, value)

    # print(filted_array)
    if len(filted_array) != 0:
        result_obj = {'users': [], 'tickets': []}
        try:
            for data in filted_array:
                ticket_data = filter_by_other_keys(ticket_data_json_array, 'organization_id', data.get('_id'))
                if len(ticket_data) != 0:
                    result_obj['tickets'].append(ticket_data[0])
                    ticket_array.append(ticket_data[0])

                user_data = filter_by_other_keys(user_data_json_array, 'organization_id', data.get('_id'))
                if len(user_data) != 0:
                    result_obj['users'].append(user_data[0])
                    user_array.append(user_data[0])

                data['user_records'] = result_obj['users']
                data['ticket_records'] = result_obj['tickets']
                filtered_array.append(data)
            # print(ticket_array)
            # print(user_array)
            return filtered_array
        except Exception as e:
            print("error occurred in organization")
            print(e)
            return []
    else:
        return []


# responsible for filtering tikets
def get_tickets(keyword, value):
    user_array = []
    filted_array = ''
    filtered_array = []
    organization_array = []
    if keyword == 'has_incidents':
        filted_array = filter_by_status(ticket_data_json_array, keyword, value)
        # print(filted_array)
    elif keyword == 'tags':
        filted_array = filer_by_tags(ticket_data_json_array, keyword, value)
        # print(filted_array)
    else:
        # print('came')
        filted_array = filter_by_other_keys(ticket_data_json_array, keyword, value)

    if len(filted_array) != 0:
        try:
            result_obj = {'orgz': [], 'users': []}
            for data in filted_array:
                user_data_submitter = filter_by_other_keys(user_data_json_array, '_id', data.get('submitter_id'))
                user_data_assignee = filter_by_other_keys(user_data_json_array, '_id', data.get('assignee_id'))
                organizarion_data = filter_by_other_keys(organization_data_json_array, '_id', data.get('organization_id'))

                if len(user_data_submitter) != 0:
                    result_obj['users'].append(user_data_submitter[0])
                    user_array.append(user_data_submitter[0])

                if len(user_data_assignee) != 0:
                    result_obj['users'].append(user_data_assignee[0])
                    user_array.append(user_data_assignee[0])

                if len(organizarion_data) != 0:
                    result_obj['orgz'].append(organizarion_data[0])
                    organization_array.append(organizarion_data[0])

                data['organization_records'] = result_obj['orgz']
                data['user_records'] = result_obj['users']
                filtered_array.append(data)

            return filtered_array
        except Exception as e:
            print(e)
            return []
    else:
        return []


# taking the keys of the json object.
def get_searchable_keys():
    user_keys = []
    ticket_keys = []
    organization_keys = []

    for key in user_data_json_array[0]:
        user_keys.append(key)

    for key in ticket_data_json_array[0]:
        ticket_keys.append(key)

    for key in organization_data_json_array[0]:
        organization_keys.append(key)

    return user_keys, ticket_keys, organization_keys
