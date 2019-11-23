l = [{"id": "1", 'name': "ck", 'cost': "1000", 'brand': "sas", 'rating': "5", 'discount': '50%', 'category': 'jeans'},
     {"id": "2", 'name': "jack and jones", 'cost': "2000", 'brand': "bas", 'rating': "3", 'discount': '30%',
      'category': 'shirts'},
     {"id": "3", 'name': "levis", 'cost': "3000", 'brand': "aas", 'rating': "4", 'discount': '80%',
      'category': 'jeans'}]

print("1.Sort by Cost low to high"
      "2.Sort by Cost high to low"
      "3.Sort by Rating"
      "4.Sort by discount low to high"
      "5.Sort by discount high to low")
choice = int(input("Enter the choice"))
if choice == 1:
    mysort = lambda el: el["cost"]
    l.sort(key=mysort)
    print(l)
elif choice == 2:
    mysort = lambda el: el["cost"]
    l.sort(reverse=True, key=mysort)
    print(l)
elif choice == 3:
    mysort = lambda el: el["rating"]
    l.sort(key=mysort)
    print(l)
elif choice == 4:
    mysort = lambda el: el["discount"]
    l.sort(key=mysort)
    print(l)
elif choice == 5:
    mysort = lambda el: el["discount"]
    l.sort(reverse=True, key=mysort)
    print(l)

newobj = filter(lambda el: el["brand"] == "aas", l)
for i in newobj:
    print("{name}:{brand}".format(**i))
newobj1 = filter(lambda el: el["name"] == "ck", l)
for j in newobj1:
    print("{name}:{brand}".format(**j))
newobj2 = filter(lambda el: el["category"] == "jeans", l)
for f in newobj2:
    print("{name}:{brand}".format(**f))
