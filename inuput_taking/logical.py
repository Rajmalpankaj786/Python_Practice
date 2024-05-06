#find odd , even and even-odd

a,b = map(int, input().split())
if(a%2==0 and b%2==0):
    print("Even")
elif(a%2 != 0 and b%2 != 0):
    print("Odd")
else:
    print("Even-Odd")