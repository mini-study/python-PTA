a,b=input().split()
a,b=int(a),int(b)
su=0;su=int(su)
while a<=b:
    su=a*a+1/a+su
    a+=1
print("sum = %.6f"%(su))
