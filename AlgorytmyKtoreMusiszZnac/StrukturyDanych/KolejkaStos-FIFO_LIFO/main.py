wi1 = {
"name" : "Clean room A",
"prev" : None,
"next" : None
}

wi2 = {
"name" : "Clean room B",
"prev" : None,
"next" : None
}

wi3 = {
"name" : "Clean room C",
"prev" : None,
"next" : None
}

def add_item_begin(my_collection, new_item):
    new_item["next"] = my_collection
    new_item["prev"] = None
    
    if my_collection:
        my_collection["prev"] = new_item
    my_collection = new_item
    return my_collection


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
    
work = None
work = add_item_end(work, wi1)
work = add_item_end(work, wi2)
work = add_item_end(work, wi3)

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
    
    return my_collection, item

work, item = del_item_begin(work)

print(item['name'])

print(work)

wi4 = {
"name" : "Clean room D",
"prev" : None,
"next" : None
}

work = add_item_end(work, wi4)

item = work
while item:
    print(item["name"])
    item = item["next"]

work, item = del_item_begin(work)

print(item['name'])

item = work
while item:
    print(item["name"])
    item = item["next"]

wi5 = {
"name" : "Clean room E",
"prev" : None,
"next" : None
}

work = add_item_begin(work, wi5)

work, item = del_item_begin(work)

print(item['name'])