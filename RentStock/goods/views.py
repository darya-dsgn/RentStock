from django.shortcuts import render


def catalog(request):
    return render(request, 'goods/catalog.html')


#def catalogod(request):
    #return render(request, 'goods/catalogod.html')


#def catalogteh(request):
    #return render(request, 'goods/catalogteh.html')


def product(request):
    return render(request, 'goods/product.html')