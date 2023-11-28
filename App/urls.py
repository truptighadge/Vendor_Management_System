from django.urls import path
from App import views
#from . views import Vendor_API_LC,Vendor_API_RUD,Purchase_Order_API_LC,Vender_API_Performance_Metrics


urlpatterns = [
    path('vendors/', views.Vendor_Profiles.as_view()),
    path('vendors/<int:pk>/', views.Vendor_Details.as_view()),
    path('vendors/<int:pk>/performance',views.Vender_Performance_Metrics.as_view()),


    path('purchase_orders/',views.Purchase_Orders.as_view()),
    path('purchase_orders/<int:pk>/',views.Purchase_Order_Details.as_view()),
    path('purchase_orders/<int:pk>/acknowledge',views.Update_Acknowledgement.as_view()),
  
]


