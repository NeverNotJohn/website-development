# EXCEPTIONS!!!!!!!!!!!!!! 

try:
    f = open('simp.txt', 'w')
    f.write("test wruierasd a")
except IOError: # does not even need an error type
    print("error could not find file or read data")
else:
    print("SUCCESS")
    f.close()
finally:
    print("This will actually go :D") #this will always execute

f = open('simp.txt', 'r')
print(f.read())
f.close()

# will handle errors and continue
print("Hello world!")