import requests
import json

link = "https://fakestoreapi.com/"

# Выводим продукты, которые стоят мене 20
print("Продукты по цене менее 20")
response = requests.get(f"{link}/products").json()
filtered_items = [item for item in response if int(item["price"]) < 20]
for item in filtered_items:
    print(f"{item['title']} по цене {item['price']}")

# Выводим все категории
print('='*30, end='\n\n')
print("Все категории")
print("\n".join(requests.get(link + "/products/categories").json()) + '\n')

# Выводим все проудкты с конкретной категорией
print('='*30, end='\n\n')
print("Все продукты с категорией  'jewelery'")
response = requests.get(link + "/products/category/jewelery").json()
for product in response:
    print(product['title'])
print('='*30, end='\n\n')

# Выводим список всех пользователей со всеми значениями
print("Вывести всех пользователей")
response = requests.get(f"{link}/users").json()
for user in response:
    for key, value in user.items():
        print(f"{key}: {value}")
    print('-'*15)

# Добавляем пользователя
print('='*30, end='\n\n')
print("Добавляем пользователя со своим именем")
new_user = {
                "email":'goldfarbm@mail.ru',
                "username":'mishanyya',
                "password":'SupePa$$w0rd',
                "name":{
                    "firstname":'Mikhail',
                    "lastname":'Goldfarb'
                },
                "address":{
                    "city":'Chelyabinsk',
                    "street":'Molodogvardeycev',
                    "number":41,
                    "zipcode":'777-666',
                    "geolocation":{
                        "lat":'-100',
                        "long":'50'
                    }
                },
            }
res = requests.post(link + "/users", json=new_user)

print("Код ответа: "+ str(res.status_code))