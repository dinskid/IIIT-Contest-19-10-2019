r = ''

li = input().split('_')
r+=li[0]
for e in li[1:]:
	r+=e[0].upper()+e[1:]

print(r)

