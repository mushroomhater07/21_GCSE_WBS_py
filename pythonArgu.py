import sys


def back():
    print ("back called")
print(sys.argv[1]);
locals()[sys.argv[1]]()
#exec(code , run_global)
