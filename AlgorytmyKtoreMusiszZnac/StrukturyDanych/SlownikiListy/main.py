ben = {
  "name" : "Ben",
  "phone" : "123456789",
  "email" : "ben@bencompany.com"
}
jan = {
  "name" : "Jan",
  "phone" : "123456789",
  "email" : "jan@jancompany.com"
}
ann = {
  "name" : "Ann",
  "phone" : "123456789",
  "email" : "ann@anncompany.com"
}

#ben

contact_list = [ben, jan, ann]

#contact_list

all_emails = ''
for c in contact_list:
    all_emails += c["email"] + ";"

print(all_emails)

contact_dict = {}
for c in contact_list:
    contact_dict[c["name"]] = c

print(contact_dict)

print(contact_dict['Ann'])

print(contact_dict["Ann"]["email"])