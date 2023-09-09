from typing import Any
from django.shortcuts import render,HttpResponseRedirect
from .models import Employee
from django.core.paginator import Paginator
from django.views.generic.base import TemplateView,RedirectView
from .forms import EmplyeeForm


#class view template
class EmployeeClassView(TemplateView):
    template_name="index.html"
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        data = Employee.objects.all().order_by("id")
        context={'data':data}
        return context
    

#class based postview
class EmployeePostclassView(TemplateView):
    template_name="add.html"
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        ef = EmplyeeForm()
        context= {'form':ef}
        return context

    def post(self,Request):
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
            return(HttpResponseRedirect('/'))
        else:
            return render(Request,"add.html",{'form':ef})




#function based view
# def deletePage(Request,id):
#     try:
#         data= Employee.objects.get(id=id).delete()
#     except:
#         pass
#     return HttpResponseRedirect("/")    


class EmployeeDeletePage(RedirectView):
    url="/"
    def get_redirect_url(self, *args, **kwargs):
        id = kwargs['id']
        Employee.objects.get(id=id).delete()
        return super().get_redirect_url(*args, **kwargs)








# def homepage(Request):
#     data = Employee.objects.all().order_by("-id")
#     paginator = Paginator(data, 1)  # Show 25 contacts per page.
#     page_number = Request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     return render(Request, "index.html", {"data": page_obj})

#Using django-forms to post the request!
#but this is function based views
# def addPage(Request):
#     if(Request.method=="POST"):
#         ef= EmplyeeForm(Request.POST)
#         if(ef.is_valid()):
#             e = Employee()
#             e.name= ef.cleaned_data['name']
#             e.email=ef.cleaned_data['email']
#             e.phone=ef.cleaned_data['phone']
#             e.dsg=ef.cleaned_data['dsg']
#             e.salary=ef.cleaned_data['salary']
#             e.city =ef.cleaned_data['city']
#             e.state =ef.cleaned_data['state']
#             e.save()
#             # return render(HttpResponseRedirect(Request,"editPage.html"))
#             return(HttpResponseRedirect('/')) # redirct to the page
#         else:
#             return render(Request,"add.html",{'form':ef})

#     else:     
#         ef = EmplyeeForm()
        # return render(Request,"add.html",{'form':ef})


# class EmployeeaddPage(TemplateView):
#         template_name="add.html"





# def editPage(Request):
#     return render(Request,'edit.html')




