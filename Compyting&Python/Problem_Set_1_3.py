s = 'qajhglqfodxsnhrrtu'

groups = []
current_longest = ''
previous_char = ''
for i in s:
    if previous_char and i < previous_char:
        groups.append(current_longest)
        current_longest = i
    else:
        current_longest += i
    previous_char = i
    print groups
if groups == []:
    count = current_longest
else:
    count = max(groups, key=len)
print('Longest substring in alphabetical order is: ' + str(count))