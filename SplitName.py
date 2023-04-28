fullName = "Freda Smith"
firstName = ""
lastName = ""
for index = 0 to fullName.length -1
    if fullName (index) == " " then
        position = index
    endif
next index
for index = 0 to position-1
    firstName = firstName + fullName (index)
next index
for index = position + 1 to fullName.length -1
    lastName = lastName + fullName (index)

print(" ",firstName)
print(" ",lastName)