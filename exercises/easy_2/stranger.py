def greetings(name_components, occupation_description):
    if len(name_components) < 2:
        print('Error: name component list should have at least 2 elements')
        return None

    if ('title' not in occupation_description or
        'occupation' not in occupation_description) :
        print('Error: occupation description must contain'
              'title and occupation values')
        return None

    full_name = ' '.join(name_components)
    full_occupation = f"{occupation_description['title']} \
{occupation_description['occupation']}"

    full_greeting = f"Hello, {full_name}! Nice to have a {full_occupation} around."
    return full_greeting

greeting = greetings(
    ["Justas",],
    {"title": "Senior", "occupation": "Frontend Engineer"},
)
print(greeting) # Hello, John Q Doe! Nice to have a Master Plumber around.