# Author: MOG 2/15/21

my_file = open("alma_mater.txt")
contents = my_file.readlines() 
for x in range(len(contents)):
    print(contents[len(contents) - x - 1])
my_file.close()
