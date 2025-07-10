from collections import defaultdict
st=["eat","tea","tan","ate","nat","bat"]
hash=defaultdict(list)
for x in st:
    sor="".join(sorted(x))
    hash[sor].append(x)
for y in hash.values():
    print(y)

