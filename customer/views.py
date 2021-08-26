from django.shortcuts import render,redirect
from customer import forms
from django.contrib.auth import authenticate,login,logout
from django.views.generic import TemplateView,ListView,DetailView,DeleteView,CreateView
from django.contrib.auth.models import User
from owner.models import Mobile
from customer.models import Cart,Orders
from django.contrib import messages
from.decorators import signin_required
from django.utils.decorators import method_decorator
from .filters import MobileFilter
# Create your views here.
class RegistrationView(TemplateView):
    form_class=forms.RegistrationForm
    template_name = "registration.html"
    model=User
    context={}

    def get(self, request, *args, **kwargs):
        form=self.form_class
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
                form.save()
                return redirect("signin")

class SignInView(TemplateView):
    template_name = "login.html"
    form_class=forms.LoginForm
    cotext={}
    def get(self, request, *args, **kwargs):
        form=self.form_class
        self.cotext["form"]=form
        return render(request,self.template_name,self.cotext)

    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("customerhome")


@method_decorator(signin_required,name="dispatch")
class CustomerHome(ListView):
    template_name = "customerhomepage.html"
    model = Mobile
    context_object_name = "mobiles"

@method_decorator(signin_required,name="dispatch")
class ProductDetail(DetailView):
    template_name = "product_detail.html"
    model = Mobile
    context_object_name = "mobile"
    pk_url_kwarg = 'pk'


@method_decorator(signin_required,name="dispatch")
class AddCartView(TemplateView):
    model=Cart
    def get(self, request, *args, **kwargs):
        product_id=kwargs["id"]
        product=Mobile.objects.get(id=product_id)
        user=request.user
        cart=Cart(product=product,user=user)
        cart.save()
        messages.success(request,"Added to cart")
        return redirect("customerhome")

@method_decorator(signin_required,name="dispatch")
class ViewCart(ListView):
    model = Cart
    template_name = "cart_detail.html"
    context_object_name = "items"

    def get_queryset(self):
        queryset=self.model.objects.filter(user=self.request.user,status="in_cart")
        return queryset

@method_decorator(signin_required,name="dispatch")
class CartRemove(DeleteView):
    model = Cart
    def get(self, request, *args, **kwargs):
        cart_id=kwargs["c_id"]
        cart=Cart.objects.get(id=cart_id)
        cart.delete()
        return redirect("cartdetails")

@method_decorator(signin_required,name="dispatch")
class OrderView(CreateView):
    template_name = "order_place.html"
    form_class = forms.OrderForm
    model = Orders
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            cart_id=kwargs["c_id"]
            product_id=kwargs["p_id"]
            cart=Cart.objects.get(id=cart_id)
            product=Mobile.objects.get(id=product_id)
            order.product=product
            order.user=request.user
            order.save()
            cart.status="order_placed"
            cart.save()
            return redirect("customerhome")

@method_decorator(signin_required,name="dispatch")
class MyOrders(ListView):
    template_name = "myorders.html"
    context_object_name = "orders"
    model = Orders
    def get_queryset(self):
        queryset=self.model.objects.filter(user=self.request.user)
        return queryset
@method_decorator(signin_required,name="dispatch")
class OrderRemove(DeleteView):
    model = Orders
    def get(self, request, *args, **kwargs):
        order_id=kwargs["o_id"]
        order=Orders.objects.get(id=order_id)
        order.delete()
        return redirect("myorder")

@method_decorator(signin_required,name="dispatch")
class OrderDetail(DetailView):
    template_name = "order_detail.html"
    model = Orders
    context_object_name = "order"
    pk_url_kwarg = 'pk'


@method_decorator(signin_required,name="dispatch")
class SignOutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("signin")

class MobileFilterView(TemplateView):
    template_name = "search.html"
    def get(self, request, *args, **kwargs):
        form=MobileFilter(request.GET,queryset=Mobile.objects.all())
        return render(request,self.template_name,{"filter":form})