l=[1,2,3,4,5]

# s=len(l)
# print(s)

# temp=l[0]

# l[0]=l[s-1]
# l[s-1]=temp
# print(l)

def swap(list,x,y):
  list[x],list[y]=list[y],list[x]
  return list

l=[1,34,56,33,44]
x,y=3,1

print(swap(l,x-1,y-1))



