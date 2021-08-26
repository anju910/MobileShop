from django.shortcuts import render,redirect
from .forms import MobileCreationForm,BrandCreationForm,BrandSearchForm,OrderUpdateForm
from .models import Brand,Mobile
from django.contrib import messages
from django.views.generic import TemplateView,DetailView,UpdateView
from customer.models import Orders
from django.urls import reverse_lazy

# Create your views here.
class OwnerView(TemplateView):
    template_name = "owner/home.html"
    context={}
    def get(self, request, *args, **kwargs):
        orders=Orders.objects.filter(status="order_placed")
        self.context["orders"]=orders
        dorders = Orders.objects.filter(status="deliverd")
        self.context["dorders"] = dorders
        order_placed_count=Orders.objects.filter(status="order_placed").count()
        self.context["order_placed_count"]=order_placed_count
        order_deliverd_count=Orders.objects.filter(status="deliverd").count()
        self.context["order_deliverd_count"]=order_deliverd_count
        return render(request,self.template_name,self.context)
def brand_create(request):
    context={}
    form=BrandCreationForm()
    context["form"]=form
    if request.method=="POST":
        form=BrandCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # print("created!!")
            messages.success(request,"Brand Added Successfully!!")
            return redirect("addbrands")
        else:
            messages.error(request,"Failed!!")
            context["form"]=form
            return render(request, 'owner/brand_create.html', context)

    return render(request,'owner/brand_create.html',context)

def view_brand(request):
    brands=Brand.objects.all()
    context={}
    context["brands"]=brands
    form=BrandSearchForm()
    context["form"]=form

    if request.method=="POST":
        form=BrandSearchForm(request.POST)
        if form.is_valid():
            brand_name=form.cleaned_data["brand_name"]
            brand=Brand.objects.filter(brand_name__contains=brand_name)
            context["brands"]=brand
            return render(request,"owner/brand_list.html",context)

    return render(request,'owner/brand_list.html',context)

def detail_brand(request,id):
    brand=Brand.objects.get(id=id)
    context={}
    context["brand"]=brand
    return render(request,"owner/brand_detail.html",context)

def remove_brand(request,id):
    brand=Brand.objects.get(id=id)
    brand.delete()
    return redirect("viewbrands")

def update_brand(request,id):
    brand=Brand.objects.get(id=id)
    form=BrandCreationForm(instance=brand)
    context={}
    context['form']=form

    if request.method=="POST":
        form=BrandCreationForm(instance=brand,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewbrands")
    return render(request,"owner/brand_change.html",context)




def mobile_create(request):
    context={}
    form =MobileCreationForm()
    context["form"]=form
    if request.method=="POST":
        form=MobileCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Mobile Created")
            return redirect("addmobiles")
        else:
            messages.error(request,"Mobile Creation Failed")
            context["form"]=form
            return render(request,"owner/mobile_create.html",context)


    return render(request,"owner/mobile_create.html",context)


def mobile_list(request):
    mobiles=Mobile.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"owner/mobile_list.html",context)

def mobile_update(request,id):
    mobile=Mobile.objects.get(id=id)
    form=MobileCreationForm(instance=mobile)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=MobileCreationForm(request.POST,files=request.FILES,instance=mobile)
        if form.is_valid():
            form.save()
            return redirect("listmobiles")
        else:
            context["form"] = form
            return render(request,"owner/mobile_edit.html",context)
    return render(request,"owner/mobile_edit.html",context)

def mobile_detail(request,id):
    mobile=Mobile.objects.get(id=id)
    context={}
    context["mobile"]=mobile
    return render(request,"owner/mobile_detail.html",context)



def mobile_remove(request,id):
    mobile=Mobile.objects.get(id=id)
    mobile.delete()
    return redirect("listmobiles")

class OrderDetail(DetailView):
    template_name = "owner/order_detail.html"
    model = Orders
    context_object_name = "order"
    pk_url_kwarg = 'pk'

class OrderUpdateView(UpdateView):
    model = Orders
    form_class = OrderUpdateForm
    template_name = "owner/update.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("home")
