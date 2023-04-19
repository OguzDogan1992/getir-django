from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.contrib import messages

# Create your views here.

def index(request):
    kategoriler = Kategori.objects.all()

    context = {
        'kategoriler': kategoriler,
    }
    return render(request, 'index.html', context)

def products(request):
    kategoriler = Kategori.objects.all()
    urunler = Urun.objects.all()
    search = ''
    sepetim = ''
    if request.user.is_authenticated:
        sepetim = Sepet.objects.filter(owner = request.user, odendiMi = False)
    if request.GET.get('search'):
        search = request.GET.get('search')
        urunler = Urun.objects.filter(kategori__isim__icontains = search)

    if request.method == 'POST':
        if request.user.is_authenticated:
            urunId =request.POST['urunId']
            urunum = Urun.objects.get(id = urunId)
            yeniadet = request.POST['yeniadet']
            if Sepet.objects.filter(owner = request.user, urun = urunum, odendiMi = False).exists():
                sepet = Sepet.objects.get(owner = request.user, urun = urunum, odendiMi = False)
                sepet.adet += int(yeniadet)
                sepet.toplamFiyat = sepet.urun.fiyat * sepet.adet
                sepet.save()
                messages.success(request, 'Sepete Eklendi')
                return redirect('products')
            else:
                sepet = Sepet.objects.create(
                    owner = request.user,
                    urun = urunum,
                    adet = yeniadet,
                    toplamFiyat = int(yeniadet) * urunum.fiyat
                )

                sepet.save()
                messages.success(request, 'Sepete Eklendi')
                return redirect('products')


        else:
            messages.warning(request, 'Lütfen giriş yapınız.')
            return redirect('products')
    
    toplam = 0
    for i in sepetim:
        toplam += i.toplamFiyat
    context = {
        'kategoriler': kategoriler,
        'urunler': urunler,
        'search': search,
        'sepetim': sepetim,
        'toplam': toplam,
    }
    return render(request, 'products.html', context)

def productsDetail(request, urunId):
    urun = Urun.objects.get(id = urunId)

    context = {
        'urun': urun,
    }
    return render(request, 'products-detail.html', context)

def basket(request):
    user = request.user
    sepetim = Sepet.objects.filter(owner =user, odendiMi = False)
    
    if request.method == 'POST':
        if 'sil' in request.POST:
            urunId = request.POST['urunId']
            silinen = Sepet.objects.get(id = urunId)
            silinen.delete()
            messages.success(request, 'Ürün sepetten kaldırıldı')
            return redirect('basket')
        if 'guncelle' in request.POST:
            urunId = request.POST['urunId']
            sepet = Sepet.objects.get(id = urunId)
            yeniAdet = request.POST['yeniAdet']
            sepet.adet = yeniAdet
            sepet.toplamFiyat = sepet.urun.fiyat * int(yeniAdet)
            sepet.save()
            messages.success(request, 'Sepet güncellendi.')
            return redirect('basket')
    toplam = 0
    for i in sepetim:
        toplam += i.toplamFiyat
    context = {
        'sepetim': sepetim,
        'toplam': toplam
    }
    return render(request, 'basket.html', context)