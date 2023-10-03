from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .forms import TanishqForm
from .models import Tanishq
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class TanishqView(View):
    def get(Self,request):
        form=TanishqForm()
        template_name='crudapp/tanishqform.html'
        context={'form':form}
        return render(request,template_name,context)
    def post(self,request):
        form=TanishqForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display_url')
        return HttpResponse('<h2>Data Invalid </h2>')


@method_decorator(login_required, name='dispatch')
class OrderDisplay(View):
    def get(self, request):
        data=Tanishq.objects.all()
        template_name='crudapp/orderlist.html'
        context={'data':data}
        return render(request,template_name,context)
        

class EditOrder(View):
    def get(self, request, pk):
        obj=Tanishq.objects.get(cid=pk)
        form=TanishqForm(instance=obj)
        template_name='crudapp/tanishqform.html'
        context={'form':form}
        return render(request,template_name,context)
    def post(self,request,pk):
        obj=Tanishq.objects.get(cid=pk)
        form=TanishqForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('display_url')
        return HttpResponse("<h1>Inavalid Data</h1>")

class DeleteOrder(View):
    def get(self, request, pk):
        obj=Tanishq.objects.get(cid=pk)
        template_name='crudapp/delete.html'
        context={'data':obj}
        return render(request,template_name,context)    
    def post(self,request,pk):
        obj=Tanishq.objects.get(cid=pk)
        obj.delete()
        return redirect('display_url')


