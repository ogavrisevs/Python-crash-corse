msg="hello python"
print (msg)
print(msg.title())

# f-strings == format string
full_text= f"This is : {msg}"
print("String \n with \n new \n lines.")
print("Lets escape simgle quotes ('this') and double quotes (\"that\")")

int1 = 2
print (f" This is : {int1} of type : {type(int1)}")
float1 = 3.14
print (f" This is : {float1} of type : {type(float1)}")

# multiple assigment
a1, a2 ,a3 = 1, 2, 3
print (f"{a1},{a2},{a3}")

# underscore in numbers 
big_number = 3.141_592_653_589_793_238_462_643_383_279_502_884_197
print(big_number)