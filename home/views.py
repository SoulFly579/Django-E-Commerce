from django.shortcuts import render
from home.models import Setting,ContactFormu,ContactFormMessage
from product.models import Product, Category
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:4]
    category = Category.objects.all()
    dayproducts = Product.objects.all()[:4]
    lastproducts = Product.objects.all().order_by('-id')[:4]
    randomproducts = Product.objects.all().order_by('?')[:4]
    

    context = {'setting':setting,
                'page': 'home',
                'category': category,
                'sliderdata':sliderdata,
                'dayproducts':dayproducts,
                'lastproducts':lastproducts,
                'randomproducts': randomproducts
                }
    return render(request, 'index.html',context)

def hakkimizda(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting':setting,
                'category': category,}
    return render(request, 'hakkimizda.html',context)

def referanslar(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting':setting,
                'category': category,}
    return render(request, 'referanslar.html',context)

def iletisim(request):

    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,'Mesajınız başarılı bir şekilde gönderilmiştir. Teşekkür Ederiz.')
            return HttpsResponseRedirect('/iletisim')
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = { 'setting':setting,
                'form':form,
                'category': category,}
    return render(request, 'iletisim.html',context)

def category_products(request,id,slug):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    category_data = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    context = { 'setting':setting,
                'products':products,
                'category': category,
                'category_data':category_data,
                }
    return render(request,'products.html', context)