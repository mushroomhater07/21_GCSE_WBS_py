import os;
#python map()
import numpy;
# import tkinter;
# from tkinter import tk, tkinter;
# from tkinter import filedialog;
print(len(os.listdir()))
list1 =[[""]* len(os.listdir()) for i in range(2)]
for idx, x in enumerate(os.listdir()):
    if (os.path.isfile(x)):
        list1[0][idx] = x
        list1[1][idx] = os.stat(x).st_size
input1 = int(input("1. file size duplicate , 2. file name duplicate"))
match input1:
    case 1:
        deleteablelist = list1;
        for i in range(len(list1[0])):
            temp = list1[1][i];
            deleteablelist[1][i] = ""
            if temp in deleteablelist[1]:
                try:
                    temp.index("~$")
                except:
                    print(i ,": " ,list1[0][i])  
                else:
                    print("")
        print("program finished")
        print()
        count = 0; input2 =11
        deletelist = [] *len(list1)
        while(input2 > 0):
            input2 = int(input("input the number you want to delete"))
            deletelist[count] = input2;
            count +=1
        for x in range(len(deletelist)):
            if os.path.exists(temp):
                os.remove(temp)
            else:
                print("doesnt exist")

        # if [0][1] not in list[0]:
        #     if   "":
        #     print("dead")
        # else:
        #     print("alive")
