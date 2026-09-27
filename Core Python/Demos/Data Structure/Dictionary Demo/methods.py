di ={1:'Python', 2:'Java', 3:'PHP'}
# di.clear()
di2 = di.copy()
print(di.get(4))
print(di.get(4, 'Key not found'))
print(di.items())
print(di.keys())
di.pop(1)
di.popitem()
di.update({4:'C', 5:'R'})
print(di.values())

print(di)