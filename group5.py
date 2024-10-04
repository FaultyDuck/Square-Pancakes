i = input('')
spli = i.split(',')
a = ''
sorted_list = sorted(spli)
for f in sorted_list:
    a += f + ','
print(a[:-1])