from django.shortcuts import render
from . import models

def home_page(request):
    banner = models.Banner.objects.last()
    blogs = models.Blogs.objects.order_by('-id')[:9]
    ourdata = models.OurData.objects.last()
    context = {
        "banner": banner,
        "blogs": blogs,
        "ourdata": ourdata,
    }
    return render(request, 'index.html', context=context)

def blog_list(request):
    category = models.Category.objects.all()
    blogs = models.Blogs.objects.all()

    context = {
        "blogs": blogs,
        "category": category,
    }
    return render(request, 'blog.html', context=context)

def blog_filter(request, category_id):
    blogs = models.Blogs.objects.filter(category=category_id)
    category = models.Category.objects.all()
    context = {
        "blogs": blogs,
        "category": category,
    }
    return render(request, 'blog_filter.html', context=context)


def blog_detail(request, id):
    blog = models.Blogs.objects.get(id=id)
    related_blog = models.Blogs.objects.filter(category=blog.category).order_by('-id').exclude(id=blog.id)[:2]
    context = {
        "blog": blog,
        "related_blog": related_blog,
    }
    return render(request, 'blog_detail.html' , context=context)


def contacts(request):
    ourdata = models.OurData.objects.last()
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        models.Contacts.objects.create(name=name, phone=phone, message=message)
    context = {
        "ourdata": ourdata,
    }
    return render(request, 'contact.html', context=context)

