test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}

def add_setting(dictionary, item):
    key, value = (x.lower() for x in item)
    if key in dictionary:
        return f'Setting \'{key}\' already exists! Cannot add a new setting with this name.'
    else:
        dictionary[key] = value
        return f'Setting \'{key}\' added with value \'{value}\' successfully!'
    
def update_setting(dictionary, item):
    key, value = (x.lower() for x in item)
    if key in dictionary:
        dictionary[key] = value
        return f'Setting \'{key}\' updated to \'{value}\' successfully!'
    else:
        return f'Setting \'{key}\' does not exist! Cannot update a non-existing setting.'
    
def delete_setting(dictionary, key):
    key = key.lower()
    if key in dictionary:
        dictionary.pop(key)
        return f'Setting \'{key}\' deleted successfully!'
    else:
        return 'Setting not found!'

def view_settings(dict):
    print(dict)
    if not dict:
        return 'No settings available.'
    else:
        settings_str = "Current User Settings:\n"
        for key, value in dict.items():
            settings_str += f'{key.title()}: {value}\n'
    return settings_str

print(view_settings(test_settings))
print(add_setting(test_settings,('id', '10')))

# print(delete_setting('Id'))
# print(update_setting('theme', 'dark'))
print(view_settings(test_settings))
