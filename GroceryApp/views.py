from django.shortcuts import render,redirect
from GroceryApp.models import CategoryDB,ProductDB
from Frontend.models import ContactDB
from django.core.files.storage.filesystem import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,"index.html")

def categoryPage(request):
    return render(request,"AddCategory.html")

def saveCategory(reg):
    if reg.method == "POST":
        cn = reg.POST.get("name")
        des = reg.POST.get("description")
        img = reg.FILES["image"]
        obj = CategoryDB(CategoryName=cn,Description=des,CategoryImage=img)
        obj.save()
        messages.success(reg,"category saved successfully")
        return redirect(categoryPage)

def displayCategories(reg):
    data = CategoryDB.objects.all()
    return render(reg,"displayCategory.html",{'data':data})

def editcategory(reg,dataid):
    data = CategoryDB.objects.get(id=dataid)
    return render(reg,"editCategory.html",{'data':data})

def updateCategory(reg,dataid):
    if reg.method == "POST":
        cn = reg.POST.get("name")
        des = reg.POST.get("description")
        try:
            img = reg.FILES["image"]
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=dataid).CategoryImage
        CategoryDB.objects.filter(id=dataid).update(CategoryName=cn,Description=des,CategoryImage=file)
        messages.success(reg, "category update successfully")
        return redirect(displayCategories)

def deleteCategory(reg,dataid):
    data = CategoryDB.objects.filter(id=dataid)
    data.delete()
    messages.success(reg, "category delete successfully")
    return redirect(displayCategories)

def addProduct(reg):
    data = CategoryDB.objects.all()
    return render(reg,"AddProduct.html",{'data':data})

def saveProduct(reg):
    if reg.method == "POST":
        pn = reg.POST.get("pname")
        cn = reg.POST.get("cname")
        des = reg.POST.get("description")
        pr = reg.POST.get("price")
        img = reg.FILES["pimage"]
        obj = ProductDB(ProductName=pn,CategoryName=cn,Description=des,Price=pr,ProductImage=img)
        obj.save()
        messages.success(reg, "Product saved successfully")
        return redirect(addProduct)

def displayproduct(reg):
    pro = ProductDB.objects.all()
    return render(reg,"displayProduct.html",{'pro':pro})

def editProduct(reg,dataid):
    data = ProductDB.objects.get(id=dataid)
    pro = ProductDB.objects.all()
    return render(reg,"editproduct.html",{'data':data,'pro':pro})

def updateProduct(reg,dataid):
    if reg.method == "POST":
        pn = reg.POST.get("pname")
        cn = reg.POST.get("cname")
        des = reg.POST.get("description")
        pr = reg.POST.get("price")
        try:
            img = reg.FILES["pimage"]
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = ProductDB.objects.get(id=dataid).ProductImage
        ProductDB.objects.filter(id=dataid).update(ProductName=pn,CategoryName=cn,Description=des,Price=pr,ProductImage=file)
        messages.success(reg, "Product update successfully")
        return redirect(displayproduct)

def deleteProduct(reg,dataid):
    data = ProductDB.objects.filter(id=dataid)
    data.delete()
    messages.success(reg, "Product delete successfully")
    return redirect(displayproduct)

def adminlogin(reg):
    return render(reg,"loginPage.html")

def adminLoginPage(request):
    if request.method == "POST":
        na = request.POST.get("name")
        pwd = request.POST.get("password")
        if User.objects.filter(username__contains=na).exists():
            user = authenticate(username=na,password=pwd)
            if user is not None:
                login(request,user)
                request.session['username'] = na
                request.session['password'] = pwd
                return redirect(index)
            else:
                messages.error(request, "Invalid username or password")
                return redirect(adminlogin)
        else:
            return redirect(adminlogin)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout successfully")
    return redirect(adminlogin)

def displayContact(reg):
    data = ContactDB.objects.all()
    return render(reg,"displayContact.html",{'data':data})

def deleteContact(reg,dataid):
    data = ContactDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displayContact)