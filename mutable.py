shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list)) # same id as the one without the cookies
print(another_list)

a = b = c = d = e = f = another_list
print(a)

print("Adding Cream")
b.append("cream")
print(c)
print(d)


