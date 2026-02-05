my_dict = {
    "name": "Ravi naganuri",
    "address" : "Yelimunnli",
    "taluk" : "hukkeri",
    "Dist" : "Belagavi"
}
print(my_dict.values())
print(my_dict.keys())
print(my_dict.pop("Dist"))
print(my_dict)
print(my_dict.items())
print(my_dict.get("name"))
my_dict.update({"age":22}) #it will update the key and value
print(my_dict)
my_dict["state"] = "Karnatak" # adding new key and value
print(my_dict)
# print(my_dict["state"])# it will shows the key error
# print(my_dict.get("state","none other than")) #it will shows none other than, it not allows the code 
del my_dict["state"] # it will delete the key and value
print(my_dict)
print(len(my_dict)) # it will shows the length of the dictionary
