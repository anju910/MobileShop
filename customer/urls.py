from django.urls import path
from customer import views


urlpatterns=[
    path("accounts/signin",views.SignInView.as_view(),name="signin"),
    path("accounts/signup",views.RegistrationView.as_view(),name="signup"),
    path("home",views.CustomerHome.as_view(),name="customerhome"),
    path("products/<int:pk>", views.ProductDetail.as_view(), name="productdetail"),
    path("products/addtocart/<int:id>",views.AddCartView.as_view(),name="addtocart"),
    path("products/carts", views.ViewCart.as_view(), name="cartdetails"),
    path("products/carts/remove/<int:c_id>", views.CartRemove.as_view(), name="remove"),
    path("products/placeorder/<int:c_id>/<int:p_id>",views.OrderView.as_view(),name="placeorder"),
    path("products/orders", views.MyOrders.as_view(), name="myorder"),
    path("products/order/<int:pk>", views.OrderDetail.as_view(), name="orderdetail"),
    path("products/order/remove/<int:o_id>", views.OrderRemove.as_view(), name="orderremove"),
    path("products/find",views.MobileFilterView.as_view(),name="findmobiles"),
    path("accounts/signout",views.SignOutView.as_view(),name="signout"),
]