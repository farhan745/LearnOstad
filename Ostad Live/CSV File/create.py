import csv

#Created
'''
data = [
    ["Name","Salary","Designation","Department","location"],
    ["Alice",85000,"Software Engineer", "IT","New York"],
    ["Charlie",70000,"Data Scientist", "Data","San Francisco"],
    ["Bob",60000,"System Administrator", "IT","Chicago"],
    ["David",95000,"Product Manager", "Product","Boston"],
    ["Eve",72000,"UX Designer", "Design","Los Angeles"],
]
with open ("new.csv","w") as file:
    csv_file=csv.writer(file)

    csv_file.writerows(data)
    print("created")
'''
data = []
with open('new.csv','r') as file:
    content=csv.reader(file)
    for row in content:
        data.append(row)
print(data)
