

try:
 
    file = open("sample.txt", "r")

    
    for line in file:
        print(line, end="")

    file.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
