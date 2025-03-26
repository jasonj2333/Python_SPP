wi1 = {
    "name" : "A Standup Cloud Team",
    "start_hour" : 8,
    "duration_min" : 15,
    "prev" : None,
    "next" : None
}

wi2 = {
    "name" : "B Architecture Board",
    "start_hour" : 9,
    "duration_min" : 60,
    "prev" : None,
    "next" : None
}

wi3 = {
    "name" : "C Cloud Training",
    "start_hour" : 12,
    "duration_min" : 120,
    "prev" : None,
    "next" : None
}

wi1["next"] = wi2
wi2["prev"] = wi1
wi2["next"] = wi3
wi3["prev"] = wi2

work = wi1

def add_item_begin(my_collection, new_item):
    new_item["next"] = my_collection
    new_item["prev"] = None
    
    if my_collection:
        my_collection["prev"] = new_item

    my_collection = new_item
    return my_collection

wi4 = {
    "name" : "___ Manager meeting",
    "start_hour" : 7,
    "duration_min" : 15,
    "prev" : None,
    "next" : None
}

work = add_item_begin(work, wi4)

def add_item_end(my_collection, new_item):

    if my_collection == None:
        my_collection = new_item
        new_item["next"] = None
        new_item["prev"] = None
        return my_collection
    else:
        item = my_collection
        while item["next"]:
            item = item["next"]

        item["next"] = new_item
        new_item["next"] = None
        new_item["prev"] = item
        return my_collection


wi5 = {
    "name" : "D Compliance Check",
    "start_hour" : 15,
    "duration_min" : 15,
    "prev" : None,
    "next" : None
}

work = add_item_end(work, wi5)

item = work
while item:
    print(item["name"])
    item = item["next"]

def del_item_begin(my_collection):
    # item is the element that should be removed
    item = my_collection
    # execute only if the collection was not empty
    if item:
        # my collection should point to the next element
        my_collection = item['next']
        # if the collection is not empty, it's first element property 'prev' should point to None
        if my_collection:
            my_collection['prev'] = None
    
    return my_collection


work = del_item_begin(work)

print('--- After deletion of the first element ---')
item = work
while item:
    print(item["name"])
    item = item["next"]

def del_item_end(my_collection):
    # if the collection is not empty
    if my_collection:
        # go to the last element
        item = my_collection
        while item["next"]:
            item = item["next"]

        # the last element will be removed and this will be a new last element
        new_last_item = item['prev']
        # if such new last element exists, we need to assign to the prev property value of None
        if new_last_item:
            new_last_item['next'] = None
        else:  
            # but if the new last element is None, it means that we are removing the last element from the list
            # so now, the collection is empty
            my_collection = None
    
    return my_collection


work = del_item_end(work)

print('--- After deletion of the last element ---')
item = work
while item:
    print(item["name"])
    item = item["next"]