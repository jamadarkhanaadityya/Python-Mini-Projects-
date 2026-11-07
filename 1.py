# Program to read a file and handle errors

try:
    # Open the file in read mode
    file = open("sample.txt", "r")

    # Read and print the file line by line
    for line in file:
        print(line, end="")

    # Close the file
    file.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")