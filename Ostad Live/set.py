country = {"Bangladesh","india","china","china"}
print(country)
#add
country.add("Nepal")
print("Add napal is:", country)

#update
country.update(['A','B'])
print("Update is: ",country)
#remove
country.remove("india")
print("Remove india is: ",country)
#pop
country.pop()
print("Pop is: ",country)
#clear
country.clear()
print("Clear is: ",country)
#Union
c1={"BD","Pak","Canada","CTG"}
c2={"DK","CTG","NK"}
print("Union is: ",c1.union(c2))
#intersection
print("Intersection is: ",c1.intersection(c2))
#difference
print("Difference: ",c1.difference(c2))
