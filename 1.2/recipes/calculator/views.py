from django.shortcuts import render
from django.core.cache import cache

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def omlet_recipe(request):
    persons = request.GET.get('servings', '1')
    mult = int(persons)
    # recipe_dict = DATA.get('omlet')
    # recipe_dict.update((key, value * int(persons)) for key, value in recipe_dict.items())
    name = 'Oмлет'
    context = {
        'recipe': {
            'яйца, шт': 2 * mult,
            'молоко, л': 0.1 * mult,
            'соль, ч.л.': 0.5 * mult,
        }, # recipe_dict,
        'name' : name,
        'servings': persons,
    }
    return render(request, 'calculator/index.html', context)


def pasta_recipe(request):
    persons = request.GET.get('servings', '1')
    mult = int(persons)
    # recipe_dict = DATA.get('pasta')
    # recipe_dict.update((key, value * int(persons)) for key, value in recipe_dict.items())
    name = 'Паста'
    context = {
        'recipe': {
            'макароны, кг': 0.3 * mult,
            'сыр, кг': 0.05 * mult,
        },     # recipe_dict,
        'name': name,
        'servings': persons,
    }
    return render(request, 'calculator/index.html', context)


def sandwich_recipe(request):
    persons = request.GET.get('servings', '1')
    mult = int(persons)
    # recipe_dict = DATA.get('buter')
    # recipe_dict.update((key, value * int(persons)) for key, value in recipe_dict.items())
    name = 'Бутерброд'
    context = {
        'recipe': {
            'хлеб, ломтик': 1 * mult,
            'колбаса, ломтик': 1 * mult,
            'сыр, ломтик': 1 * mult,
            'помидор, ломтик': 1 * mult,
        }, # recipe_dict,
        'name': name,
        'servings': persons,
    }
    return render(request, 'calculator/index.html', context)