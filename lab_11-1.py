# Author: MOG 2/15/21

my_file = open("alma_mater.txt")
contents = my_file.readlines() 
for x in contents:
    print(x)
my_file.close()
