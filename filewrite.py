#f = open("test.txt", "x")
try:
    f = open("tet.txt", "w")
except:
    f = open("tet.txt", "x")
f.write("hey")
f.close()