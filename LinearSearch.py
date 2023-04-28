names = ['Sophia','Emma','Olivia','Ava','Mia','Isabella','Riley','Aria','Zoe','Charlotte','Lily','Layla','Amelia','Emily','Madelyn','Aubrey','Adalyn','Madison','Chloe','Harper','Abigail','Aaliyah','Avery','Evelyn','Kaylee','Ella','Ellie','Scarlett','Arianna','Hailey','Nora','Addison','Brooklyn','Hannah','Mila','Leah','Elizabeth','Sarah','Eliana','Mackenzie','Peyton','Maria','Grace','Adeline','Elena','Anna','Victoria','Camilla','Lillian','Natalie','Jackson','Aiden','Lucas','Liam','Noah','Ethan','Mason','Caden','Oliver','Elijah','Grayson','Jacob','Michael','Benjamin','Carter','James','Jayden','Logan','Alexander','Caleb','Ryan','Luke','Daniel','Jack','William','Owen','Gabriel','Matthew','Connor','Jayce','Isaac','Sebastian','Henry','Muhammad','Cameron','Wyatt','Dylan','Nathan','Nicholas','Julian','Eli','Levi','Isaiah','Landon','David','Christian','Andrew','Brayden','John','Lincoln']

find = input("what name ")
found = False
index = 0

while found != True and index < len(names):
    if find == names[index]:
        print("found it")
    index += 1
print (index)