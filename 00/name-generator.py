import random

genders = ['male', 'female']
male_names = ['Bob', 'Stefan', 'Steve']
female_names = ['Anna', 'Kate']
surnames = ['Kowalsi', 'Nowak', 'Smith', 'Muller']


gender = random.choice(genders)

if gender is 'male':
    name = random.choice(male_names)
else:
    name = random.choice(female_names)

surname = random.choice(surnames)

def create_email_address(name, surname):
    hosts = ['wp.pl', 'gmail.com', 'yahoo.com']
    return name.lower() + surname.lower() + str(random.randrange(0, 100)) + '@' + random.choice(hosts)


print ("Gender: ", gender)
print ("Name: ", name)
print ("Surname: ", surname)
print ("Email address: ", create_email_address(name, surname))
