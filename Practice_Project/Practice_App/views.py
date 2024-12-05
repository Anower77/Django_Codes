from django.shortcuts import render

# Create your views here.


def meal_section(request):
    meals = [
        {
            "strMeal": "BeaverTails",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
            "idMeal": "52928",
            "mealDes": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut consequatur praesentium temporibus sapiente sint delectus veritatis. Consequatur porro commodi adipisci"
        },
        {
            "strMeal": "Breakfast Potatoes",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
            "idMeal": "52965",
            "mealDes": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut consequatur praesentium temporibus sapiente sint delectus veritatis. Consequatur porro commodi adipisci"
        },
        {
            "strMeal": "Canadian Butter Tarts",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
            "idMeal": "52923",
            "mealDes": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut consequatur praesentium temporibus sapiente sint delectus veritatis. Consequatur porro commodi adipisci"
        },
        {
            "strMeal": "Montreal Smoked Meat",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
            "idMeal": "52927",
            "mealDes": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut consequatur praesentium temporibus sapiente sint delectus veritatis. Consequatur porro commodi adipisci"
        },
        {
            "strMeal": "Nanaimo Bars",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
            "idMeal": "52924",
            "mealDes": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut consequatur praesentium temporibus sapiente sint delectus veritatis. Consequatur porro commodi adipisci"
        },
        {
            "strMeal": "Pate Chinois",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
            "idMeal": "52930",
            "mealDes": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut consequatur praesentium temporibus sapiente sint delectus veritatis. Consequatur porro commodi adipisci"
        },
        {
            "strMeal": "Pouding chomeur",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
            "idMeal": "52932",
            "mealDes": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut consequatur praesentium temporibus sapiente sint delectus veritatis. Consequatur porro commodi adipisci"
        },
        {
            "strMeal": "Poutine",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
            "idMeal": "52804",
            "mealDes": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut consequatur praesentium temporibus sapiente sint delectus veritatis. Consequatur porro commodi adipisci"
        },
        {
            "strMeal": "Rappie Pie",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
            "idMeal": "52933",
            "mealDes": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut consequatur praesentium temporibus sapiente sint delectus veritatis. Consequatur porro commodi adipisci"
        },
        {
            "strMeal": "Split Pea Soup",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
            "idMeal": "52925",
            "mealDes": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aut consequatur praesentium temporibus sapiente sint delectus veritatis. Consequatur porro commodi adipisci"
        }
    ]
    return render(request, 'index.html', {'meals': meals})

def index(request):
    return render(request, 'index.html')

