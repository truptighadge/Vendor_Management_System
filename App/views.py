from django.shortcuts import render
from . models import Vendor_Model,Purchase_Order_Model
from .serializers import Vendor_Serializer,Purchase_Order_Serializer,Vendor_Serializer_performance_metrics,Update_Acknowledgement_Serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveAPIView,RetrieveUpdateAPIView
		
# Create a new vendor and List all Vendors
class Vendor_Profiles (ListCreateAPIView):
	queryset=Vendor_Model.objects.all()
	serializer_class=Vendor_Serializer

# Retrieve a specific vendors details,Update a vendors details,Delete a vendor
class Vendor_Details (RetrieveUpdateDestroyAPIView):
	queryset=Vendor_Model.objects.all()
	serializer_class=Vendor_Serializer


# Retrieve a vendors performance metrics
class Vender_Performance_Metrics(RetrieveAPIView):
	queryset=Vendor_Model.objects.all()
	serializer_class=Vendor_Serializer_performance_metrics


# Create a purchase order and List all purchase orders
class Purchase_Orders(ListCreateAPIView):
	queryset=Purchase_Order_Model.objects.all()
	serializer_class=Purchase_Order_Serializer

# Retrieve details of a specific purchase order,Update a purchase order,Delete a purchase order
class Purchase_Order_Details(RetrieveUpdateDestroyAPIView):
	queryset=Purchase_Order_Model.objects.all()
	serializer_class=Purchase_Order_Serializer


# For Vendors to acknowledge purchase order 
class Update_Acknowledgement(RetrieveUpdateAPIView):
	queryset=Purchase_Order_Model.objects.all()
	serializer_class=Update_Acknowledgement_Serializer
