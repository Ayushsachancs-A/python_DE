with open("logs.txt", "r") as file:
    content = file.read()
    print(content)


# Reading line by line Good for large files
with open("logs.txt", "r") as file:
    for line in file:
        print(line.strip())


# write a file
with open("logs.txt", "w") as file:
    file.write("end of file\n")
    file.write("now finally ended\n")

#large file line by line
with open("logs.txt", "r") as file:
    for line in file:
        if "ERROR" in line:
            print(line.strip())


c=0
#assignment : read a file and count the number of error and write in a new file
with open("logs.txt","r") as file:
    for line in file:
        if "ERROR" in line:
            with open("error_log.txt","a") as file:
                file.write(line)
            c+=1
print(c)




    



