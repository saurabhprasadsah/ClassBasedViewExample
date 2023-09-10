from django.views import View
from django.shortcuts import render,HttpResponseRedirect
from .models import Employee
# from django.core.paginator import Paginator
from django.views.generic.base import TemplateView,RedirectView
from .forms import EmplyeeForm



# def homepage(Request):
#     data = Employee.objects.all().order_by("-id")
#     paginator = Paginator(data, 1)  # Show 25 contacts per page.
#     page_number = Request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     return render(Request, "index.html", {"data": page_obj})


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


#function based view
# def deletePage(Request,id):
#     try:
#         data= Employee.objects.get(id=id).delete()
#     except:
#         pass
#     return HttpResponseRedirect("/")  



#class Based EmployeeDeletePage
class EmployeeDeletePage(RedirectView):
    url="/"
    def get_redirect_url(self, *args, **kwargs):
        id = kwargs['id']
        try:
               Employee.objects.get(id=id).delete()
        except:
               pass
        return super().get_redirect_url(*args, **kwargs)


# def updatePage(Request,id):
#     try:
#         data= Employee.objects.get(id=id)
#         if(Request.method=="POST"):
#             ef= EmplyeeForm(Request.POST)
#             if(ef.is_valid()):
#                 data = Employee()
#                 data.name= ef.cleaned_data['name']
#                 data.email=ef.cleaned_data['email']
#                 data.phone=ef.cleaned_data['phone']
#                 data.dsg=ef.cleaned_data['dsg']
#                 data.salary=ef.cleaned_data['salary']
#                 data.city =ef.cleaned_data['city']
#                 data.state =ef.cleaned_data['state']
#                 data.save()
#                 return(HttpResponseRedirect('/'))
#         else:   
#             ef= EmplyeeForm(instance=data)
#             return render(Request,"updates.html",{'data':data,'form':ef})
#     except:
#          pass 
#     return HttpResponseRedirect("/") 
# 
# 
# def updatePage(Request,id):
#     try:
#         data = Employee.objects.get(id=id)
#         if(Request.method=="POST"):
#             ef = EmplyeeForm(Request.POST)
#             if(ef.is_valid()):
#                 data.name = ef.cleaned_data['name']
#                 data.email = ef.cleaned_data['email']
#                 data.phone = ef.cleaned_data['phone']
#                 data.dsg = ef.cleaned_data['dsg']
#                 data.salary = ef.cleaned_data['salary']
#                 data.city = ef.cleaned_data['city']
#                 data.state = ef.cleaned_data['state']
#                 data.save()
#                 return HttpResponseRedirect("/")
#         else:
#             ef = EmplyeeForm(instance=data)
#             return render(Request,"update.html",{'form':ef})
#     except:
#          pass
#     return HttpResponseRedirect("/")


class EmployeeUpdateClassView(View):
    template_name = "update.html"
    def get(self,Request,id):
        self.data = Employee.objects.get(id=id)
        ef = EmplyeeForm(instance=self.data)
        return render(Request,"update.html",{'form':ef})
    
    def post(self,Request):
        ef = EmplyeeForm(Request.POST)
        if(ef.is_valid()):
            self.data.name = ef.cleaned_data['name']
            self.data.email = ef.cleaned_data['email']
            self.data.phone = ef.cleaned_data['phone']
            self.data.dsg = ef.cleaned_data['dsg']
            self.data.salary = ef.cleaned_data['salary']
            self.data.city = ef.cleaned_data['city']
            self.data.state = ef.cleaned_data['state']
            self.data.save()
            return HttpResponseRedirect("/")
        else:
            return render(Request,"add.html",{'form':ef})




















