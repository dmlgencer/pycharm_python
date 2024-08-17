message = "Hello World"
print(message)

# if you want to get first char in this message we can use [0]
print(message[0])  # H

# like a java's substring method. First index is inclusive but second index is exclusive.
print(message[0:5])  # Hello

print(message[6:])  # World
print(message[:5])  # Hello

# lower and upper case
print(message.lower())  # hello world
print(message.upper())  # HELLO WORLD

# count: it is sensitive lower and upper case.
print(message.count('Hello'))  # 1
print(message.count('w'))  # 0 (because w is have to be upper)

print(message.find('Universe'))  # -1

# replace method is change the word.
new_message = message.replace('World', 'Universe')
print(new_message)  # Universe
