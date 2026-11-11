
data = input("Enter some text: ")

file = open("output.txt", "w")
file.write(data + "\n")
file.close()

file = open("output.txt", "a")
file.write("This is the appended text.\n")
file.close()

file = open("output.txt", "r")
print("\nFinal content of the file:")
print(file.read())
file.close()
