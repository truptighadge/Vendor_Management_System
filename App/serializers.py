from rest_framework import serializers

from . models import Vendor_Model,Purchase_Order_Model


class Vendor_Serializer(serializers.ModelSerializer):
	class Meta:
		#fields="__all__"
		fields=["id","vendor_code","name","contact_details","address"]
		model=Vendor_Model
class Vendor_Serializer_performance_metrics(serializers.ModelSerializer):
	class Meta:
		#fields="__all__"
		fields=["on_time_delivery_rate","quality_rating_avg","average_response_time","fulfillment_rate"]
		model=Vendor_Model


class Purchase_Order_Serializer(serializers.ModelSerializer):
	class Meta:
		fields=["id",'po_number','vendor','order_date','delivery_date','items','quantity','status','quality_rating','issue_date','acknowledgement_date','delivered_date']
		model=Purchase_Order_Model


class Update_Acknowledgement_Serializer(serializers.ModelSerializer):
	class Meta:
		fields=['acknowledgement_date']
		model=Purchase_Order_Model



