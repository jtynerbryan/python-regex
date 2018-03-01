import re

names_file = open('names.txt', encoding="utf-8")
data = names_file.read()
names_file.close()

# use match for begining of string, search for anywhere in string
last_name = r"Love"
first_name = r"Kenneth"
print(re.match(last_name, data))
print(re.search(first_name, data))

# + for 1-infinite occurences, ? for 0-1 occurences, * for 0-infinite occurences, {num} for how many occurences
print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))

print(re.findall(r'\w*, \w+', data))








# If you don't know the size of a file, it's better to read it a chunk at a time and close it automatically. The following snippet does that:

# with open("some_file.txt") as open_file:
#    data = open_file.read()

# The with causes the file to automatically close once the action inside of it finishes. And the action inside, the .read(), will finish when there are no more bytes to read from the file.
