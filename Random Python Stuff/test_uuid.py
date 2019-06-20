# Python3 code to generate 
# id using uuid4() 

import uuid 

test = set()

for i in range(1, 999999999999999999999):
    id = uuid.uuid4() 

    try:
        test.add(id)
    except:
        print('The following id:' + str(id) + ' was found. Failed uniqueness test.')
        break

    if i % 1000000 == 0:
        print('Still running, at ' + str(i))


# Id generated using uuid4() 
print ('Game Over.')
