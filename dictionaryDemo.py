d={124:"akshay",890:"milin",997:"hamza",545:"rishil"}

print(d)
d[124]="Uday"
print(d)
d1=d.copy()
print(d1)
print(d.get(997))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(545))
print(d)
print(d.popitem())                              #by default deletes last value 
print(d)
d2={345:"shivam",678:"nirmal",789:"jay"}
d.update(d2)
print(d)

for i in d:
    print(i," : ",d[i])
