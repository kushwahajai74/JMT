from django.shortcuts import redirect, render
from .models import cards, carousel,product,contacts,data,about

# Create your views here.

def index(request):
    obj=carousel.objects.all()
    cardsData=cards.objects.all()
    datas=data.objects.values('Stock_Category').distinct()
    context={ 'obj':obj,'data':datas,'cards' : cardsData}
    return render(request,'index1.html',context)


def contact(request):
    datas=data.objects.values('Stock_Category').distinct()
    context={ 'data':datas}
    return render(request,'contact.html',context)


def aboutus(request):
    aboutData = about.objects.all()
    datas=data.objects.values('Stock_Category').distinct()
    context={ 'data':datas, 'about':aboutData}
    return render(request, "aboutus.html", context)


def product1(request,id):
    datas=data.objects.values('Stock_Category').distinct()
    products=data.objects.filter(id=id)
    context={"products":products, 'data':datas}
    
    return render(request,'product1.html',context)

def saveEnquiry(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        query=request.POST['query']

        en=contacts(name=name,phone=phone,email=email, query=query)
        en.save()

    return render(request, "contact.html")


def brand(request,category):
    products=data.objects.filter(Stock_Category=category)
    products=products.exclude(Image_Link=None)
    datas=data.objects.values('Stock_Category').distinct()
    return render(request,'brands.html',{"products":products,'data':datas})




