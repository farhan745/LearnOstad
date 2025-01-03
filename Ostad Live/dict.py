bill={
    "name":"bill gates",
    "age":70,
    "country":"USA",
    "gender":"Male"
}
print(bill)
for i in bill.values():
    print(i)

#update
bill.update({
    "age":72,
    "country":"India"
})
print("Update: ",bill)
#clear
bill.clear()
print("Clear: ",bill)
#----------------------
