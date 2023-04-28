def pattern():
    a = int(input ("enter the number of rows: "))
    b = a-3
    for k in range(b, 0, -1):
        for f in range(0,5):
            print (" ")
        for j in range(0,k):
            print (" ")
        for h in range(0, 2* (b-k) +1):
            print ("*")
    print ("\r")

    c = a-2
    for k in range(c, 0, -1):
        for f in range(0,2):
            print (" ")
        for j in range(0,k):
            print (" ")
        for h in range(0, (2* (c-k)+1)+2):
            print ("*")
        print ("\r")

    d = a-1
    for k in range(d, 0, -1):
        for f in range(0,1):
            print (" ")
        for j in range(0,k):
            print (" ")
        for h in range(0, (2* (d-k) +1) +3):
            print ("*")
        print ("\r")

    e = a-0
    for k in range(e, 0, -1):
        for j in range(0,k):
            print (" ")
        for h in range(0, (2* (e-k) +1) +4):
            print ("*")
        print ("\r")

    for k in range(0,a):
        for j in range(0,a+1):
            print (" ")
        for h in range(0,3):
            print ("*")
        print ("\r")
pattern()