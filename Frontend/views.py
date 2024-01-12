from django.shortcuts import render,redirect
from GroceryApp.models import CategoryDB,ProductDB
from Frontend.models import ContactDB,SignUPDB,CartDB,OrderDB
from django.contrib import messages

# Create your views here.
def homePage(request):
    data = CategoryDB.objects.all()
    count = CartDB.objects.filter(UserName=request.session['UserName']).count()
    return render(request,"home.html",{'data':data,'count':count})

def productsPage(request):
    pro = ProductDB.objects.all()
    count = CartDB.objects.filter(UserName=request.session['UserName']).count()
    return render(request,"products.html",{'pro':pro,'count':count})

def single_product(request,proid):

    data = ProductDB.objects.get(id=proid)
    count = CartDB.objects.filter(UserName=request.session['UserName']).count()
    return render(request,"single_product.html",{'data':data,'count':count})

def productFiltered(request,cat_name):
    data = ProductDB.objects.filter(CategoryName=cat_name)
    count = CartDB.objects.filter(UserName=request.session['UserName']).count()
    return render(request,"product_filtered.html",{'data':data,'count':count})

def aboutPage(reg):
    count = CartDB.objects.filter(UserName=reg.session['UserName']).count()
    return render(reg,"aboutUs.html",{'count':count})

def contactPage(reg):
    count = CartDB.objects.filter(UserName=reg.session['UserName']).count()
    return render(reg,"contact.html",{'count':count})

def servicePage(reg):
    count = CartDB.objects.filter(UserName=reg.session['UserName']).count()
    return render(reg,"services.html",{'count':count})

def saveContactPage(reg):
    if reg.method == "POST":
        na = reg.POST.get("name")
        em = reg.POST.get("email")
        mes = reg.POST.get("message")
        obj = ContactDB(Name=na,Email=em,Message=mes)
        obj.save()
        return redirect(contactPage)

def signUpPage(reg):
    return render(reg,"Signup.html")

def saveSignup(reg):
    if reg.method == "POST":
        na = reg.POST.get("name")
        mo = reg.POST.get("mobile")
        em = reg.POST.get("email")
        us = reg.POST.get("username")
        pa = reg.POST.get("password")
        obj = SignUPDB(Name=na,Mobile=mo,Email=em,UserName=us,Password=pa)
        obj.save()
        return redirect(signUpPage)

def UserLogin(request):
    if request.method == "POST":
        un = request.POST.get("username")
        pwd = request.POST.get("password")
        if SignUPDB.objects.filter(UserName=un,Password=pwd).exists():
            request.session['UserName'] = un
            request.session['Password'] = pwd
            messages.success(request, "Login Sucessfully")
            return redirect(homePage)
        else:
            messages.error(request, "Invalid username or password")
            return redirect(signUpPage)
    return redirect(signUpPage)

def UserLogout(request):
    del request.session['UserName']
    del request.session['Password']
    messages.success(request, "Logout Sucessfully")
    return redirect(UserLogin)

def cartPage(request):
    data = CartDB.objects.filter(UserName=request.session['UserName'])
    total_price = 0
    count = CartDB.objects.filter(UserName=request.session['UserName']).count()
    for i in data:
        total_price = total_price +i.TotalPrice
    return render(request,"cart.html",{'data':data,'total_price':total_price,'count':count})

def saveCartPage(reg):
    if reg.method == "POST":
        un = reg.POST.get("user")
        pn = reg.POST.get("product")
        qty = reg.POST.get("qty")
        pr = reg.POST.get("price")
        tl = reg.POST.get("total")
        obj = CartDB(UserName=un,ProductName=pn,Quntity=qty,Price=pr,TotalPrice=tl)
        obj.save()
        return redirect(cartPage)

def removeItem(reg,dataid):
    data = CartDB.objects.filter(id=dataid)
    data.delete()
    return redirect(cartPage)

def checkout(request):
    data = CartDB.objects.filter(UserName=request.session['UserName'])
    count = CartDB.objects.filter(UserName=request.session['UserName']).count()
    total_price = 0
    for i in data:
        total_price = total_price + i.TotalPrice
    return render(request,"checkout.html",{'data':data,'total_price':total_price,'count':count})

def saveOrder(request):
    if request.method == "POST":
        fn = request.POST.get("fname")
        ln = request.POST.get("lname")
        un = request.POST.get("username")
        em = request.POST.get("email")
        ad = request.POST.get("address")
        cu = request.POST.get("country")
        st = request.POST.get("state")
        pi = request.POST.get("pin")
        pa = request.POST.get("paymentMethod")
        nac = request.POST.get("nameoncard")
        cr = request.POST.get("credit")
        ex = request.POST.get("expiry")
        cv = request.POST.get("cvv")
        object = OrderDB(FirstName=fn,LastName=ln,UserName=un,Email=em,Address=ad,
                         Country=cu,State=st,Pin=pi,Payment=pa,NameOnCard=nac,CardNumber=cr,Expiration=ex,CVV=cv)

        object.save()
        data = CartDB.objects.all()
        data.delete()
        messages.success(request, "Ordered successfully ")

        return redirect(homePage)




