# API Structure
-----------------
## FOODS
-----------------
### Ingredients
**URL** : `/api/v1/ingredients`

**METHOD** : `GET`

**DATA**
```json
{
    "search": "search by name",
    "name": "exact filtering",
    "manufacturer": "exact filtering"
}
```

**RESPONSE CODE** : `200 OK`

**RESPONSE DATA**
```json
{
    "links": {
        "next": "http://127.0.0.1:8000/api/v1/ingredients?page=2&search=stripe",
        "previous": null
    },
    "count": 96,
    "total_pages": 5,
    "results": [
        {
            "url": "http://127.0.0.1:8000/api/v1/ingredients/1375",
            "name": "benton's, original fudge striped shortbread cookies",
            "description": null,
            "manufacturer": "aldi-benner company"
        },
        {
            "url": "http://127.0.0.1:8000/api/v1/ingredients/5668",
            "name": "food club, fun stripes, peanut butter & strawberry jelly",
            "description": null,
            "manufacturer": "topco associates, inc."
        }
    ]
}
```
-----------------
### Ingredient details
**URL** : `/api/v1/ingredients/<id>`

**METHOD** : `GET`

**RESPONSE CODE** : `200 OK`

**RESPONSE DATA**
```json
{
    "url": "http://127.0.0.1:8000/api/v1/ingredients/54363",
    "name": "snak club, salted mixed nuts",
    "description": null,
    "manufacturer": "snack world, llc",
    "nutrients": [
        {
            "name": "protein",
            "description": null,
            "value": "4.30",
            "unit": "g"
        },
        {
            "name": "total lipid (fat)",
            "description": null,
            "value": "18.90",
            "unit": "g"
        },
        {
            "name": "carbohydrate, by difference",
            "description": null,
            "value": "72.80",
            "unit": "g"
        }
    ]
}
```
-----------------
### Recipes
**URL** : `/api/v1/recipes`

**METHOD** : `GET`

**RESPONSE CODE** : `200 OK`

**RESPONSE DATA**
```json
{
    "links": {
        "next": "http://127.0.0.1:8000/api/v1/recipes?page=2",
        "previous": null
    },
    "count": 2344,
    "total_pages": 118,
    "results": [
        {
            "url": "http://127.0.0.1:8000/api/v1/recipes/909",
            "name": "Grilled artichokes with parsley and garlic",
            "instructions": "1) Bring a lass ...",
            "preparation_time": 2820,
            "number_of_servings": 6,
            "source": "http://www.foodnetwork.co.uk/recipes/grilled-artichokes-parsley-and-garlic-0.html",
            "image_url": "http://www.fnstatic.co.uk/images/content/recipe/grilled-artichokes-with-parsley-and-garlic_1.jpg "
        }
        {
            "url": "http://127.0.0.1:8000/api/v1/recipes/36",
            "name": "Slow-Cooker Swedish Meatballs",
            "instructions": "Serves: 10 ... 4 Television Food Network, G.P. All rights reserved.",
            "preparation_time": 2100,
            "number_of_servings": 12,
            "source": "http://www.foodnetwork.co.uk/recipes/slow-cooker-swedish-meatballs.html",
            "image_url": "http://www.fnstatic.co.uk/images/content/recipe/slow-cooker-swedish-meatballs.jpeg "
        }
    ]
}
```
-----------------
### Recipes by ingredients
**URL** : `/api/v1/recipes`

**METHOD** : `POST`

**DATA**
```json
{
    "ingredient_ids": [33] // Has to be a list, can contain as many ids as you want.
}
```

**RESPONSE CODE** : `200 OK`

**RESPONSE DATA**
```json
{
    "links": {
        "next": "http://127.0.0.1:8000/api/v1/recipes?page=2",
        "previous": null
    },
    "count": 2344,
    "total_pages": 118,
    "results": [
        {
            "url": "http://127.0.0.1:8000/api/v1/recipes/909",
            "name": "Grilled artichokes with parsley and garlic",
            "instructions": "1) Bring a lass ...",
            "preparation_time": 2820,
            "number_of_servings": 6,
            "source": "http://www.foodnetwork.co.uk/recipes/grilled-artichokes-parsley-and-garlic-0.html",
            "image_url": "http://www.fnstatic.co.uk/images/content/recipe/grilled-artichokes-with-parsley-and-garlic_1.jpg "
        }
        {
            "url": "http://127.0.0.1:8000/api/v1/recipes/36",
            "name": "Slow-Cooker Swedish Meatballs",
            "instructions": "Serves: 10 ... 4 Television Food Network, G.P. All rights reserved.",
            "preparation_time": 2100,
            "number_of_servings": 12,
            "source": "http://www.foodnetwork.co.uk/recipes/slow-cooker-swedish-meatballs.html",
            "image_url": "http://www.fnstatic.co.uk/images/content/recipe/slow-cooker-swedish-meatballs.jpeg "
        }
    ]
}
```
-----------------
### Recipe details
**URL** : `/api/v1/recipes/<id>`

**METHOD** : `GET`

**RESPONSE CODE** : `200 OK`

**RESPONSE DATA**
```json
{
    "url": "http://127.0.0.1:8000/api/v1/recipes/85",
    "name": "Marinated Beef Stir Fry with Noodles",
    "instructions": "For the Marinade ...",
    "preparation_time": null,
    "number_of_servings": 2,
    "source": "http://www.foodnetwork.co.uk/recipes/marinated-beef-stir-fry-with-noodles.html",
    "image_url": "http://www.fnstatic.co.uk/images/content/recipe/marinated-beef-stir-fry-with-noodles.jpeg ",
    "ingredients": [
        {
            "ingredient": {
                "url": "http://127.0.0.1:8000/api/v1/ingredients/19854",
                "name": "juice",
                "description": null,
                "manufacturer": "weis markets, inc.",
                "nutrients": []
            },
            "quantity": "1",
            "unit": "piece"
        },
        {
            "ingredient": {
                "url": "http://127.0.0.1:8000/api/v1/ingredients/1383",
                "name": "sauce",
                "description": null,
                "manufacturer": "allied old english, inc.",
                "nutrients": []
            },
            "quantity": "by taste",
            "unit": "g"
        }
    ]
}
```
-----------------
## USERS
-----------------
### Register
**URL** : `/api/users/register`

**METHOD** : `POST`

**DATA**
```json
{
    "username": "test",
    "email": "test@gmail.com",
    "password": "test"
}
```

**RESPONSE CODE** : `200 OK`

**RESPONSE DATA**
```json
{
    "username": "test",
    "email": "test@gmail.com"
}
```
-----------------
### Login
**URL** : `/api/users/login`

**METHOD** : `POST`

**DATA**
```json
{
    "username": "test",
    "password": "test"
}
```

**RESPONSE CODE** : `200 OK`

**RESPONSE DATA**
```
{
    "refresh": "refreshtoken",
    "access": "accesstoken"
}
```
-----------------
### Refresh
**URL** : `/api/users/login/refresh`

**METHOD** : `POST`

**DATA**
```json
{
    "refresh": "refreshtoken"
}
```

**RESPONSE CODE** : `200 OK`

**RESPONSE DATA**
```
{
    "access": "accesstoken"
}
```
-----------------
### Profile
**URL** : `/api/users/profile`

**METHOD** : `GET`

**RESPONSE CODE** : `200 OK`

**RESPONSE DATA**
```json
{
    "title": null,
    "dob": null,
    "address": null,
    "country": null,
    "city": null,
    "zipcode": null,
    "user": {
        "url": "http://127.0.0.1:8000/api/users/4",
        "username": "klemen",
        "email": "",
        "first_name": "",
        "last_name": ""
    }
}
```
-----------------
### Profile update
**URL** : `/api/users/profile`

**METHOD** : `POST`

**DATA**
```json
{
    "url": "http://127.0.0.1:8000/api/users/4",
    "username": "klemen",
    "email": "",
    "first_name": "Klemen",
    "last_name": "Kubelj",
    "profile": {
        "title": "asd",
        "dob": null,
        "address": "Bukovica, 55",
        "country": "Slovenia",
        "city": "Vodice",
        "zipcode": "1217"
    }
}
```

**RESPONSE CODE** : `200 OK`

**RESPONSE DATA**
```json
{
    "url": "http://127.0.0.1:8000/api/users/4",
    "username": "klemen",
    "email": "",
    "first_name": "Klemen",
    "last_name": "Kubelj",
    "profile": {
        "title": "asd",
        "dob": null,
        "address": "Bukovica, 55",
        "country": "Slovenia",
        "city": "Vodice",
        "zipcode": "1217"
    }
}
```
-----------------
### Users list
**URL** : `/api/users`

**METHOD** : `GET`

**RESPONSE CODE** : `200 OK`

**RESPONSE DATA**
```json
{
    "count": 15,
    "next": null,
    "previous": null,
    "results": [
        {
            "url": "http://127.0.0.1:8000/api/users/19",
            "username": "novinovi",
            "email": "klemen.kubelj@gmail.com",
            "first_name": "Klemen",
            "last_name": "Kubelj",
            "profile": {
                "title": "",
                "dob": null,
                "address": "Bukovica, 55",
                "country": "Slovenia",
                "city": "Vodice",
                "zipcode": "1217"
            }
        },
        {
            "url": "http://127.0.0.1:8000/api/users/20",
            "username": "newuser2",
            "email": "klemen.kubelj@gmail.com",
            "first_name": "Klemen",
            "last_name": "Kubelj",
            "profile": {
                "title": "",
                "dob": null,
                "address": "Bukovica, 55",
                "country": "Slovenia",
                "city": "Vodice",
                "zipcode": "1217"
            }
        }
    ]
}
```
-----------------
### User details
**URL** : `/api/users/<id>`

**METHOD** : `GET`

**RESPONSE CODE** : `200 OK`

**RESPONSE DATA**
```json
{
    "url": "http://127.0.0.1:8000/api/users/2",
    "username": "miha",
    "email": "asdas@gmail.com",
    "first_name": "",
    "last_name": "",
    "profile": {
        "title": "",
        "dob": null,
        "address": "",
        "country": "",
        "city": "",
        "zipcode": ""
    }
}
```
-----------------
### User inventories list
**URL** : `/api/users/profile/inventories`

**METHOD** : `GET`

**RESPONSE CODE** : `200 OK`

**RESPONSE DATA**
```json
[
    {
        "url": "http://localhost:8000/api/users/profile/inventories/5",
        "name": "Moj inventory 1234563",
        "desc": "This inventory is automatically created 123"
    },
    {
        "url": "http://localhost:8000/api/users/profile/inventories/6",
        "name": "Moj drug inventory",
        "desc": "Nek drug inventori"
    }
]
```
-----------------
### User inventories details and update
**URL** : `/api/users/profile/inventories/<id>`

**METHOD** : `GET`

**RESPONSE CODE** : `200 OK`

**RESPONSE DATA**
```json
{
    "url": "http://localhost:8000/api/users/profile/inventories/5",
    "name": "Moj inventory 1234563",
    "desc": "This inventory is automatically created 123",
    "ingredients": [
        {
            "id": 9,
            "ingredient": {
                "url": "http://localhost:8000/api/v1/ingredients/25",
                "name": "original barbecue sauce",
                "description": null,
                "manufacturer": "fresh & easy",
                "nutrients": []
            },
            "quantity": "by taste",
            "unit": "misic"
        },
        {
            "id": 8,
            "ingredient": {
                "url": "http://localhost:8000/api/v1/ingredients/23",
                "name": "hot & spicy barbecue sauce",
                "description": null,
                "manufacturer": "fresh & easy",
                "nutrients": []
            },
            "quantity": "by taste",
            "unit": "test"
        }
    ]
}
```

**METHOD** : `PUT`

**DATA**
```json
{
    "name": "This is an updated inventory name",
    "desc": "This is an updated inventory desc",
}
```

**RESPONSE CODE** : `200 OK`

**RESPONSE DATA**
```json
{
    "url": "http://localhost:8000/api/users/profile/inventories/5",
    "name": "Moj inventory 1234563",
    "desc": "This inventory is automatically created 123",
    "ingredients": [...]
}
```

**METHOD** : `POST` **Insert new ingredient to inventory**

**DATA**
```json
{
    "ingredient_id": "24",
    "quantity": 100,
    "unit": "g"
}
```

**RESPONSE CODE** : `201 CREATED`

**RESPONSE DATA**
```json
{
    "id": 12,
    "inventory_id": 5,
    "ingredient_id": 24,
    "quantity": 100,
    "unit": "g"
}
```

**METHOD** : `DELETE` **Delete an inventory**

**RESPONSE CODE** : `204 NO CONTENT`
-----------------
### User inventories ingredients
**URL** : `/api/users/profile/inventories/<inventory_id>/ingredient/<id>`

**METHOD** : `GET`

**RESPONSE CODE** : `200 OK`

**RESPONSE DATA**
```json
{
    "id": 2,
    "inventory_id": 5,
    "ingredient_id": 21,
    "quantity": "56",
    "unit": "g"
}
```

**METHOD** : `PUT` **Change ingredient amount/unit in a inventory***

**DATA**
```json
{
    "quantity": 100,
    "unit": "g"
}
```

**RESPONSE CODE** : `200 OK`

**RESPONSE DATA**
```json
{
    "id": 2,
    "inventory_id": 5,
    "ingredient_id": 21,
    "quantity": "120",
    "unit": "g"
}
```

**METHOD** : `DELETE` **Delete an ingredient from inventory**

**RESPONSE CODE** : `204 NO CONTENT`
-----------------
