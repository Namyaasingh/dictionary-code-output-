rec = {"Name" : "Python", "Age":"20","Addr" : "NJ", "Country" :"USA"}
id1 = id(rec)
del rec
print(id1)

rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id2 = id(rec)
print(id2)
print(id1 == id2)
 


 # here id is a function which we wre using to chek the location of any value
 