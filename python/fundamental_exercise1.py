'''
try:
    f = open("demofile.txt")
    f.write("Lorum lpsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()
'''

myorder = "I have a {carname}, it\'s {colorname}."
print(myorder.format(carname = "Porsche", colorname = "red"))
