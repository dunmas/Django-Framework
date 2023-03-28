from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def dish_returner(request, dish):
    context = dict()

    if dish not in DATA:
        return render(request, 'calculator/index.html', context)

    dish_count = int(request.GET.get("servings", 1))
    context['recipe'] = dict()

    for ingredient in DATA[dish]:
        context['recipe'][ingredient] = DATA[dish][ingredient] * dish_count

    return render(request, 'calculator/index.html', context)
