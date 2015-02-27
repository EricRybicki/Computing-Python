s = raw_input("Enter S")
count = 0
possibilities = {"b", "o"}
for character in s:
    if character in possibilities:
        count += 1
print('Number of vowels: ' + str(count))


sentence = 'Mary had a little lamb'
>>> sentence.count('a')