from django.urls import path

from owner import views

urlpatterns=[
    path('mobiles/home',views.OwnerView.as_view(),name="home"),
    path('brands/add',views.brand_create,name="addbrands"),
    path('brands/view',views.view_brand,name="viewbrands"),
    path('brands/detail/<int:id>',views.detail_brand,name="detailbrands"),
    path('brands/remove/<int:id>',views.remove_brand,name="removebrands"),
    path('brands/change/<int:id>',views.update_brand,name="changebrands"),
    path('mobiles/add',views.mobile_create,name="addmobiles"),
    path('mobiles/',views.mobile_list,name="listmobiles"),
    path('mobiles/change/<int:id>',views.mobile_update,name="changemobiles"),
    path('mobiles/detail/<int:id>', views.mobile_detail, name="detailmobiles"),
    path('mobiles/remove/<int:id>',views.mobile_remove,name="removemobiles"),
    path("mobiles/order/detail/<int:pk>", views.OrderDetail.as_view(), name="orderdetails"),
    path("mobiles/order/update/<int:id>", views.OrderUpdateView.as_view(), name="orderupdate"),

]