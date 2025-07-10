def cou(i):
    count=0
    while i>=1:
        if i%10==0:
            count+=1
        i=i//10
    return count
N=10000000
i=1
z=0
while i<N+1:
    z=z+cou(i)
    i+=1
print(z)