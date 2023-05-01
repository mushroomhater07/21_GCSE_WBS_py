myString = "FREDA SMITH"
testString = ""
found = False

for index in range(0, len(myString) -2):
    
    for test in range (0,3):
        testString = testString + myString[index + test]
    print(testString)
	
    if testString == "RED":
        found = True
        position = index

    testString = ""

if found == True:
        print ("It was found at index ", position)
else:
        print ("Sorry. Not found.")
