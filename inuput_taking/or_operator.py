# a,b,c,d
#input : 1 2 4 3  
#output : yes
# if any of following expression is true then yes otherwise no
# 1>2 false
# 4>3 true

a , b , c, d = map(int, input().split())
if(a>b or c>d):
    print("Yes")
else: 
    print("No")
