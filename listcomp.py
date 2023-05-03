# my_list = [1, 2, 3]
# # List comprehensions always start with the operation, then the logic to iterate, additonal operations like if conditions
# double = [item * 2 for item in my_list]

# print(double)

# users = [{'name': 'Christine', 'age': 23}, {'name': 'Tru', 'age': 35}, {'name': 'Adia', 'age': 12}]

# #you can add multiple parameters for the logic
# user_name = [user['name'] for user in users if user['age'] > 30]

# print(user_name)

user_groups = [
    [
        {'name': 'Christine', 'age': 23},
        {'name': 'Tru', 'age': 35}
    ],
    [
        {'name': 'Adia', 'age': 12},
        {'name': 'Joy', 'age': 37}
    ]
]

user_name = [person['name'] for group in user_groups for person in group if person['age'] > 30]

print(user_name)



