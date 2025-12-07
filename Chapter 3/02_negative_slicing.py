name = "Harry"

print(name[0:3])

print(name[-4:-1])  # negative slicing from index -4 to -1 (excluding -1
print(name[1:4])

print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5]) 

print(name[0:3:2])
#string reverse
print(name[::-1])  # reverse the string using negative slicing
print(name[-1::-1])  # same as above
