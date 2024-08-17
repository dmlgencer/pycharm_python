greeting = "Hello"
name = "Michael"

message = greeting + " " + name
print(message)  # Hello Michael

message1 = "{} {} Welcome!".format(greeting, name)
print(message1)  # Hello Michael Welcome!

message2 = f"{greeting} {name} Welcome!"
print(message2)  # Hello Michael Welcome!
