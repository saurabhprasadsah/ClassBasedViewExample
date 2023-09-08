from django.shortcuts import render
from .models import Employee
from django.core.paginator import Paginator


def homepage(Request):
    data = Employee.objects.all().order_by("-id")
    paginator = Paginator(data, 3)  # Show 25 contacts per page.
    page_number = Request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(Request, "index.html", {"data": page_obj})

