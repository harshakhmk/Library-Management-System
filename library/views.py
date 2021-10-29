from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def my_books(request):
    return render(
        request,
        "mybooks.html",
        {"books": Books.objects.filter(created_by_user_id=request.user)},
    )


def newbook(request):
    if request.method == "GET":
        book_form = BookForm()
        return render(
            request,
            "newbook.html",
            {"form": book_form, "category": Category.objects.all()},
        )
    else:
        book_form = BookForm(request.POST or None)
        if book_form.is_valid:
            book_obj = book_form.save(commit=False)

            category_obj, created = Category.objects.get_or_create(
                category=book_obj.category
            )

            book_obj.created_by_user_id = request.user
            book_obj.category_id = category_obj
            book_obj.save()
            return redirect("mybooks")
        else:
            return redirect("newbook")


def home(request):
    if request.user.is_authenticated == False:
        return render(request, "unauth.html")

    book_list = Books.objects.all()
    categories = Category.objects.all()
    category = request.GET.get("category")
    if category is not None:
        book_list = book_list.filter(category=category)
        print(book_list.count())

    page = request.GET.get("page", 1)
    paginator = Paginator(book_list, 10)

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, "home.html", {"books": books, "categories": categories})
