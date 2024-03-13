var={10,50.5,'viki','joshi',True,10}
print(var)

#add.
var.add('Vaibhav')
print(var)

#update..
var.update(['Bhimtal',25])
print(var)

#delete..
var.pop()
print(var)

#remove..
var.remove(25)
print(var)

#clear..
var.clear()
print(var)

var1={5,True,78.55,'tanakpur'}
var2={5,False,56.65,'Bhimtal',True}

#union..
print(var1.union(var2))
print(var1|var2)

#intersection..
print(var1.intersection(var2))
print(var1&var2)

#difference..
print(var1.difference(var2))
print(var1-var2)

print(var1.symmetric_difference(var2))