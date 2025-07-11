#Method--1
phone_no={'chandu':00,
          'bujji':11,
          'bangaram':56,
          'bujji':98  # duplicates will take take latest value
}
# #Method--2
# phone_no=dict({'chandu':00,
#           'bujji':11,
#           'bangaram':56,
#           'bujji':98  # duplicates will take take latest value
# })
# #Method--3
# phone_no=dict([('chandu',00),('bujji',11),('bangaram',56),('bujji',98)])

print(phone_no)
print(phone_no['bujji'])
phone_no['bujji']=34567
print(phone_no)
phone_no['madam']={34567,7654,4567}  # To add new
print(phone_no)
phone_no['chandu']={'chandu_home':78158,'chandu_clg':7658765} # To give like a list
print(phone_no)
print(phone_no['chandu']['chandu_home'])
print(phone_no.get('chandu'))
# To delete
 # To clear phone_no.clear()
phone_no.pop('bujji')
# phone_no.popitem()    To delete the last one added
del phone_no['chandu']
print(phone_no)
# To print only values or keys
print(phone_no.keys())
print(phone_no.values())
print(phone_no.items()) # In the form of list containing tuples
for i in phone_no:
    print(i)     # this will give only keys
    print(phone_no[i])  # To access using loop
for i in phone_no.items(): # To acess them directly
    print(i)