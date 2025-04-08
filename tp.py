strs = ["flower","flow","flight"]

prefix = strs[0]

for item in strs[1:]:
    while not item.startswith(prefix):
        prefix = prefix[:-1]
        
        if not prefix:
            print("")

print(prefix)
         