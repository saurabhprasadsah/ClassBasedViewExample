from django.shortcuts import render,HttpResponseRedirect
from .models import Employee
from django.core.paginator import Paginator
from django.views.generic.base import TemplateView
from .forms import EmplyeeForm


#class view template
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

#Using django-forms to post the request
def addPage(Request):
    if(Request.method=="POST"):
        ef= EmplyeeForm(Request.POST)
        if(ef.is_valid()):
            e = Employee()
            e.name= ef.cleaned_data['name']
            e.email=ef.cleaned_data['email']
            e.phone=ef.cleaned_data['phone']
            e.dsg=ef.cleaned_data['dsg']
            e.salary=ef.cleaned_data['salary']
            e.city =ef.cleaned_data['city']
            e.state =ef.cleaned_data['state']
            e.save()
            # return render(HttpResponseRedirect(Request,"editPage.html"))
            return(HttpResponseRedirect('/')) # redirct to the page
        else:
            pass
    else:     
        ef = EmplyeeForm()
        return render(Request,"add.html",{'form':ef})


def editPage(Request):
    return render(Request,'edit.html')




