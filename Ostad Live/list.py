fruits = ['apple','mango','cherry']
print(fruits)

#Append(object)
fruits.append('orange')
print(f"Append is orange: {fruits}")

#insert(index,object)
fruits.insert(0,'banana')
print(f"Insert is banana on 1st inndex: {fruits}")

#list.extend(another list)=>(list+another list)
fruits1 = ['orange','banana','apple']
fruits2 = ['mango','cherry']
fruits1.extend(fruits2)
print(f"fruits1 Extend in fruits2: {fruits1}")

#remove
fruits.remove( 'apple')
print("Apple is remove: ",fruits)

#pop
fruits.pop()
print("Pop is: ",fruits)

#clear
fruits.clear()
print("Clear is: ",fruits)

#sort/len/reverse
marks = [50,40,30,60,10]
marks.sort()
print("Sort is: ",marks)
print("Length is: ",len(marks))
marks.reverse()
print("Reverse is: ",marks)
