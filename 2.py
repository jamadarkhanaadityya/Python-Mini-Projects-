# Program to write, append, and read a file

# Take input from the user
data = input("Enter some text: ")

# Write the input to output.txt
file = open("output.txt", "w")
file.write(data + "\n")
file.close()

# Append additional data
file = open("output.txt", "a")
file.write("This is the appended text.\n")
file.close()

# Read and display the final content
file = open("output.txt", "r")
print("\nFinal content of the file:")
print(file.read())
file.close()