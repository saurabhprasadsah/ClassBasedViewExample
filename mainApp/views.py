from django.shortcuts import render
from .models import Employee
from django.core.paginator import Paginator
from django.views.generic.base import TemplateView
from .forms import EmplyeeForm


class DisplayClassView(TemplateView):
    template_name="index.html"
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        data = Employee.objects.all().order_by("-id")
        context={'data':data}
        return context


# def homepage(Request):
#     data = Employee.objects.all().order_by("-id")
#     paginator = Paginator(data, 1)  # Show 25 contacts per page.
#     page_number = Request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     return render(Request, "index.html", {"data": page_obj})



def addPage(Request):
    ef = EmplyeeForm()
    return render(Request,"add.html",{'form':ef})





