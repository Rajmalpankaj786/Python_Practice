#input: 2 3 , output: "false"
#hint : 2**3 = 8, 3**2 = 9 

a,b = map(int, input().split())
if(a**3>b**2):
    print("false")
else:
    print("true")
