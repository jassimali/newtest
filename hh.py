s="aabacbebebe"
k=3
max_len=0
i=j=0

hash={}
while i<len(s):
  if s[i] in hash:
    hash[s[i]]=1
  else:
    if k==0:
      j+=1
      i=j
      hash.clear()
    else:
      hash[s[i]]=1
      i+=1
      k-=1
    max_len=max(max_len,sum(hash.values()))
print(max_len)
