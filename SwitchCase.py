# Write your code here :-)
def f(x):
    match x:
        case 'a':
            return 1
        case 'b':
            return 2
        case _:
            return 0   # 0 is the default case if x is not found
enter = input("a or b: ")
fgjn = foo(enter)
print(fgjn)
