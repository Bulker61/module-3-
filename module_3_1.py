calls = 0
def count_calls():
    global calls
    calls += 1
    return calls
def string_info(string):
    count_calls()
    tuple = (len(string),string.upper(),string.lower())
    return tuple

def is_contains(string , is_contains):
    count_calls()
    for i in range(len(is_contains)):
        if string.lower() == is_contains[i].lower():
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)