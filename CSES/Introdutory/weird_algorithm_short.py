n=int(input())
s= ''
while(n!=1):
    if n%2==0:
        s+=' ' + str(int(n))
        n/=2
    else:
        s+=' ' + str(int(n))
        n = n*3 +1
print(s+ ' 1')