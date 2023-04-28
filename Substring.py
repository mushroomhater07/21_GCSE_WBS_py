myString = input("FREDA SMITH")
subString = input(" ")
testString = ""
found = False

for index in range(0, len(myString)-len(subString)-1):
    for test in range (0,len(subString)):
        testString = testString + myString[index + test]
#    print(testString)

    if testString == subString:
        found = True
        position = index
    testString = ""




if found == True:
    print ("It was found at index ", position)
else:
    print ("Sorry. Not found.")