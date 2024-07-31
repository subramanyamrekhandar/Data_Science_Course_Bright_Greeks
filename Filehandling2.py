# open funtion
# close funtion
# read funtion
# write funtion



# 1. r - read mode
# 2. w - write mode
# 3. a - append mode

# #open funtion
# f = open ("example.txt", "mode")

# # close funtion
# f.close()
# # read funtion
# f = open ("example.txt", "r")
# print(f.read())

#write funtion
# f = open ("datascinece.txt", "w")
# print(f.write())

# f = open ("example.txt", "a")
# print(f.write())


# f = open("example.txt", "w")
# f.write("Hello, world!")
# f.write("data science!")

# f = open("example.txt", "r")
# print(f.read(6))

# f = open("example.txt", "a")
# f.writelines("append mode append append")


# implementing CURD Applition 

# 1. create file with intial content

def create_file():
    with open("example.txt", "w")  as file:
        file.write("apple, 10, 20\n")
        file.write("banana, 40, 50\n")
        file.write("orange, 80, 90\n")

# read and print the file content
def read_file():
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)

# update the content on the file
def update_file(item, New_digit):
    lines = []

    with open("example.txt", "r") as file:
        lines = file.readlines()
        print(lines) # get the data

    with open("example.txt", "w") as file:
        for line in lines:
            x = line.strip().split(",")

            if x[0] == item:
                file.write(f"{x[0]},{New_digit},{x[2]}\n")

            else:
                file.write(line)
                

# cal the main funtion        
create_file()
read_file()
update_file("banana", 100)  # update the apple price to 100
read_file()  # print the updated file content










