import os

command = ""
filename = ""
check = 0

while command != "exit":
    command = input("\nWhat would you like to do [directory, list, open <filename>, return, exit] \n")
    
    if command == "directory":
        directory = input("\nWhere would you like to go: \n")
        files = os.listdir(directory)
        
    elif command == "list":
        print("")
        print(directory, "contents...\n-------------")
        for item in files:
            print(item)
        print("-------------")
        
    elif command[0:4] == "open":
        
        filename = command[5:]
        check = 0
        
        for item in files:
            if item == filename:
                check = 1
                
        if len(filename) < 5:
            directory = directory + "/" + filename
            files = os.listdir(directory)
            print("New directory is:", directory)
        
        elif filename[-5] != '.' and filename[-4] != '.' and check ==1:
            directory = directory + "/" + filename
            files = os.listdir(directory)
            print("\nNew directory is:", directory)
        
        elif filename[-4:] == ".txt" and check ==1:
            print("")
            print(filename, "contents...\n-------------")
            opened_file = open(directory + "/" + filename,'r')
            print(opened_file.read(),"\n-------------")
            
        elif check == 1:
            print("Unsupported filetype '", filename[-4:], "' opening default program...")
            os.startfile(directory + "/" + filename)

        else:
            print("File not found. (Hint: capitalization matters!")

    elif command == "return":
        while directory[-1] != '/':
            directory = directory[:-1]
            
        directory = directory[:-1]
        files = os.listdir(directory)
        print("\nNew directory is:", directory)
        
    elif command == "exit":
        print("\nExiting...")
        opened_file.close()
        
    else:
        print("Command not recognized, try again.")
