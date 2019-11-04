"""
In here the functions are responsible for filtering data from JSON object. Each and every function requires three parameters

filter_by_tags(json_object, keyword, tags):
        json_object = json data that has read before
        keyword = the key that filtering based on
        tags = the values that can consist that particular key


filterd_by_status(json_object, keyword, value):
    json_object = json data that has read before
    keyword = the key that filtering based on
    tags = the values that can consist that particular key

filter_by_other_keys(json_object, keyword, value):
    json_object = json data that has read before
    keyword = the key that filtering based on
    tags = the values that can consist that particular key

in here mostly the filtering list comprehension have used. It's somewhat faster than the for loops
"""


# the function that responsible for finding data in the JSON base on the tag
def filer_by_tags(json_object, keyword, tags):
    # validating parameters
    if json_object is None or keyword is None or tags is None:
        return []

    if json_object == "" or keyword == "" or tags == "":
        return []

    try:
        tags_items = [item for item in json_object if tags in item.get(keyword)]
        return tags_items
    except Exception as e:
        print('Problem in filtering by tags in Handlers')
        print(e)
        return []


# the function that responsible for finding data based on the true, false values
def filter_by_status(json_object, keyword, value):
    # validating parameters
    if json_object is None or keyword is None or value is None:
        return []

    if json_object == "" or keyword == "" or value == "":
        return []

    if value == 'true':
        value = True
    elif value == 'false':
        value = False
    else:
        print("Unsopported format")
        exit()
    try:
        filtered_items = [item for item in json_object if item.get(keyword) == value]
        # for item in json_object:
        #     if item.get(keyword) == value:
        #         filtered_items.append(item)
        return filtered_items
    except Exception as e:
        print('Problem in filtering by status in Handlers')
        print(e)
        return []


# the function that responsible for finding data based on the other keyword of the JSON file
def filter_by_other_keys(json_object, keyword, value):
    # validating parameters
    if json_object is None or keyword is None or value is None:
        return []

    if json_object == "" or keyword == "" or value == "":
        return []

    try:
        filterd_items = [item for item in json_object if str(item.get(keyword)) == str(value)]
        # print(filterd_items)
        # exit()
        return filterd_items
    except Exception as e:
        print('Problem in filtering by other keys in Handlers')
        print(e)
        return []
