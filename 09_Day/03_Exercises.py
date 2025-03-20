
#1.
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# Check for 'skills' key and print middle skill if exists
if 'skills' in person:
    skills = person['skills']
    if len(skills) > 2:
        middle_skill = skills[len(skills) // 2]
        print(f"Middle skill: {middle_skill}")

    # Check if Python is in skills
    if 'Python' in skills:
        print("The person has Python skill.")

    # Check the job title based on skills
    if set(['JavaScript', 'React']) == set(skills[:2]):
        print("He is a front end developer.")
    elif set(['Node', 'Python', 'MongoDB']) == set(skills[2:]):
        print("He is a backend developer.")
    elif set(['React', 'Node', 'MongoDB']) == set(skills[1:]):
        print("He is a fullstack developer.")
    else:
        print("Unknown title.")

# Check marriage and country status
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")