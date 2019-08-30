# API Structure
-----------------
# FOODS
-----------------
GET /api/v1/ingredients?search=&name=&manufacturer=
- Searching is done only by "name" attribute.
  
RESPONSE 200
```
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
GET api/v1/ingredients/54363

RESPONSE 200
```
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
GET api/v1/recipes

RESPONSE 200
```
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
POST api/v1/recipes
```
{
    "recipe_ids": [33] // Has to be a list, can contain as many ids as you want.
}
```
RESPONSE 200
```
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
GET api/v1/recipes/85

RESPONSE 200
```
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
# USERS
-----------------
POST api/users/register
```
{
    "username": "test",
    "email": "test@gmail.com",
    "password": "test"
}
```
RESPONSE STATUS 201
```
{
    "username": "test",
    "email": "test@gmail.com"
}
```
-----------------

POST api/users/login
```
{
    "username": "test",
    "password": "test"
}
```
RESPONSE 200
```
{
    "refresh": "refreshtoken",
    "access": "accesstoken"
}
```
-----------------
POST api/users/login/refresh
```
{
    "refresh": "refreshtoken"
}
```
RESPONSE 200
```
{
    "access": "accesstoken"
}
```
-----------------
GET api/users/profile

RESPONSE 200
```
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
POST api/users/profile #Update profile
```
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
RESPONSE 200
```
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
GET api/users

RESPONSE 200
```
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
}
```
-----------------
GET api/users/<id>

RESPONSE 200
```
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
