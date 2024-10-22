calls = 0

def count_calls():
    global calls
    calls +=1

def string_info (string):
    count_calls()
    tuple_ = (len(string), string.upper(), string.lower())
    return tuple_

def is_contains (string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search_lower = []
    for i in list_to_search:
        list_to_search_lower.append(i.lower())
    if string in list_to_search_lower:
        return True
    else:
        return False

print(string_info('Orange'))
print(string_info('Fruit pie'))
print(is_contains('Apple',['ban', 'apply', 'APPLE']))
print(is_contains('frUIts', ['fruit', '123456', 'FRUITs']))
print(calls)
