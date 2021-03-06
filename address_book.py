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

# find email addresses using sets
print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))

# find all occurences of a specifc word using \b (boundaries) count and IGNORECASE (shorthand='I')
print(re.findall(r'\b[trehous]{9}\b', data, re.I))

# find email addresses not ending in .gov
print(re.findall(r'\b@[\w\d.]*[^gov\t]+', data, re.I))

# Use VERBOSE(shorthand='X') flag for multi-line strings
print(re.findall(r'''
    \b[-\w]+,
    \s
    [-\w ]+
    [^\t\n]
''', data, re.X))

# use () to create groups
print(re.findall(r'''
     ^([-\w ]*, \s[-\w ]+)\t # names
     ([-\w\d.+]+@[-\w\d.]+)\t # emails
     (\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # phones
     ([\w\s]+,\s[\w\s.]+)\t? # job and company
     (@[\w\d]+)?$ # Twitter
''', data, re.X|re.M))

# using .compile()
line = re.compile(r'''
     ^(?P<name>(?P<last>[-\w ]*), \s(?P<first>[-\w ]+))\t # names
     (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # emails
     (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # phones
     (?P<job>[\w\s]+,\s[\w\s.]+)\t? # job and company
     (?P<twitter>@[\w\d]+)?$ # Twitter
''', re.X|re.M)

print(line.search(data).groupdict())

# using .find_iter() kind of like .findall

for match in line.finditer(data):
    print('{first} {last} <{email}>'.format(**match.groupdict()))

# If you don't know the size of a file, it's better to read it a chunk at a time and close it automatically. The following snippet does that:

# with open("some_file.txt") as open_file:
#    data = open_file.read()

# The with causes the file to automatically close once the action inside of it finishes. And the action inside, the .read(), will finish when there are no more bytes to read from the file.
