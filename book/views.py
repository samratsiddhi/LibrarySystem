from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .decorator import logincheck


# Create your views here.
@logincheck
def home(request):
    return render(request, "dashboard/home.html")

@logincheck
def category(request):
    if request.method == "GET":
        category = Category.objects.all()
        contents = {
            "categories": category
        }
        
        return render(request, "dashboard/category.html", contents)

@logincheck    
def addCategory(request):
    if request.method == "GET":
        return render(request, "dashboard/create_category.html")
    
    name = request.POST.get("name")
        
    try:
        Category.objects.get(name=name)
        messages.warning(request, "Book already exists")
        return redirect(addCategory)
    except Exception:
        pass 
    
    try:
        Category.objects.create(name = name)
    except Exception:
        messages.warning(request, "Something went wrong")
        return redirect(addCategory)
    
    messages.success(request, "Category added successfully")
    return redirect(category)
    

@logincheck    
def editCategory(request,pk):
    if request.method == "POST":
        instance = Category.objects.get(pk = pk)
        name = request.POST.get('name')
        instance.name = name
        instance.save()   
        messages.success(request, "Category edited successfully")
    
        return redirect(category) 
    try:
        instance = Category.objects.get(pk = pk)
        context = {
                'category' : instance
            }
        return render(request,"dashboard/edit_category.html",context)
    except:
        messages.warning(request, "Something went wrong")
        return redirect(category)

@logincheck
def deleteCategory(request,pk):
    try:
        instance = Category.objects.get(pk = pk)
        instance.delete()
        messages.success(request, "Category deleted successfully")
    except Category.DoesNotExist as e:
        messages.warning(request, "Category does not exist")
    return redirect(category)

@logincheck
def book_list(request):
    books = Book.objects.all()
    contents = {
            "books": books
        }
        
    return render(request, "dashboard/book_list.html", contents)


@logincheck
def addBook(request):
    if request.method == "GET":
        categories = Category.objects.all()
        contents = {
            "categories": categories
        }
        return render(request, "dashboard/create_book.html",contents)
    
    name = request.POST.get("name")
    category_id = request.POST.get("category")
    category = Category.objects.get(pk = category_id )
    
    try:
        Book.objects.get(name=name, category = category)
        messages.warning(request, "Book already exists")
        return redirect(addBook)
    except Exception:
        pass 
    
    try:
        Book.objects.create(name = name, category = category)
        messages.success(request, "Book added successfully")
        return redirect(book_list)
    except Exception:
        messages.warning(request, "Something went wrong")
        return redirect(addCategory)

@logincheck    
def editBook(request,pk):
    if request.method == "POST":
        instance = Book.objects.get(pk = pk)
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        category = Category.objects.get(pk = category_id)
        instance.name = name
        instance.category = category
        instance.save()   
        messages.success(request, "Book edited successfully")
    
        return redirect(book_list) 
    try:
        categories = Category.objects.all()
        instance = Book.objects.get(pk = pk)
        context = {
                'book' : instance,
                'categories' : categories
            }
        return render(request,"dashboard/edit_book.html",context)
    except:
        messages.warning(request, "Something went wrong")
        return redirect(editBook)

@logincheck    
def deleteBook(request,pk):
    try:
        instance = Book.objects.get(pk = pk)
        instance.delete()
        messages.success(request, "Book deleted successfully")
    except Book.DoesNotExist as e:
        messages.warning(request, "Book does not exist")
    return redirect(book_list)
    

    
    
    
        




    
    
    
    