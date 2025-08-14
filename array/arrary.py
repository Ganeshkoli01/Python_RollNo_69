import array as arr 
a=arr.array('i',[1,2,3])
print("the new create array is:", end=" ")
for i in range(0,3):
          print(a[i],end="")

print()
a.insert(1,4)
print(a)

a.append(5)
print(a)

a.remove(1)  
print(a)

a.reverse()
print(a)

a.clear()
print(a)



