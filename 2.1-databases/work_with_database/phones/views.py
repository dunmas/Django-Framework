from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_type = request.GET.get('sort', 'name')
    template = 'catalog.html'
    phone_objects = Phone.objects.all()
    phones = [{
        'name': p.name,
        'slug': p.slug,
        'price': p.price,
        'image': p.image,
    } for p in phone_objects]

    if sort_type == 'name':
        phones.sort(key=lambda x: x['name'])
    elif sort_type == 'min_price':
        phones.sort(key=lambda x: x['price'])
    elif sort_type == 'max_price':
        phones.sort(key=lambda x: x['price'], reverse=True)

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, l_slug):
    template = 'product.html'

    phone = Phone.objects.get(slug=l_slug)

    context = {'phone': {
        'name': phone.name,
        'slug': phone.slug,
        'price': phone.price,
        'image': phone.image,
        'release_date': phone.release_date,
        'lte_exists': phone.lte_exists,
    }}
    return render(request, template, context)
