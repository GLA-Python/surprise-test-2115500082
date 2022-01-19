n=list(map(int,input().split()))
t=abs(n[0]-n[1])
for i in range(2,len(n)):
    if abs(n[i]-n[i-1])>t:
       t= abs(n[i]-n[i-1])
    else:
       print("False")
       break
else:
    print("True")
