# Duplicates are not allowed
# Immutable
#Indexing is not allowed
# they do not have defined order
set1={10,True,'Jenny',0.3,34.34,43,1.1}
set2={1,2,3,4,5}
set1.add(6) #To add element into the set
print(set1)
set1.discard(6) #To remove elemnt from the set
set1.remove(10) #both are same discard and remove
print(set1)
a=set1.pop()
print(a) #we can get random poped item
set1.clear() # To clear all data
print(set1)
set1={10,'Jenny',0.3,34,43,2}
set2={1,2,3,4,5}
print(set1.union(set2))  # set1 | set2 (union representation)=|
set1.update(set2) #To update set1 = set1 U set2
print(set1)
print(set1.intersection(set2)) # set1 & set2 (intersection representation)=&
set1.intersection_update(set2) # To update set1=set1 & set2
print(set1.difference(set2))# set1-set2 (difference representation)= -
set1.difference_update(set2) # To update set1=set1-set2
print(set1.symmetric_difference(set2)) # set1^set2 (symmetric difference)=^
set1.symmetric_difference_update(set2)  # To update set1=set1 ^ set2
#Disjoint sets== No common elements
a={1,2,3,4,5}
b={6,7}
print(a.isdisjoint(b))
# subset== all elements in set2 should contain in set1  --set2 is subset of set1'<='
a={1,2,3,4,5}
b={2,3}
print(b.issubset(a)) # also represented as '<='
#superset= set1 contain all elements of set2 --set1 is super set of set2
print(a.issuperset(b))

