list0=[]
print(list0)
list1=[23,5.6,'viki',True,45,'vaibhav',23]
print(list1)

#count..
print(list1.count(23))

#type..
print(type(list1))

#index..
print(list1.index(23))
print(list1.index(23,1))

#insert..
list1.insert(2,"vivek")
print(list1)

#delete..
list1.pop(2)
print(list1)

#extend..
list2=[10,9.6,'manshi']
print(list2)
list1.extend(list2)
print(list1)

#copy..
list3=list2.copy()
list2=list1[:]
print(list3)
print(list2)

#sort..
list4=[10,7,98,67,90.8]
list4.sort()
print(list4)
list4.sort(reverse=True)
print(list4)

#reverse..
list4.reverse()
print(list4)

#comprehension..
list5=['aavya','aayu','manshi','viki','aabu']
a=[word for word in list5 if word.startswith('a')]
print(a)

#unpacking..
n1,n2,n3,n4,n5=list5
print(n1)
print(n2)
print(n4)
print(n3)