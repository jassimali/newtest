arr = [-1,-1,3,4,2,-1,-1] 
k = 0
x=set(arr)
hash={}
for ch in x:
    co=0
    while co<len(arr):
        if ch-arr[co]==k:
            hash[ch]=arr[co]
        co+=1
for key,valuss in hash.items():
    print(f"({key},{valuss})")