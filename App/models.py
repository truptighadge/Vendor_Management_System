from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Vendor_Model(models.Model):
	name=models.CharField(max_length=200)
	contact_details=models.TextField(max_length=30)
	address=models.TextField(max_length=100)
	vendor_code=models.CharField(max_length=50,unique=True)

	on_time_delivery_rate=models.FloatField(blank=True,default=0)
	quality_rating_avg=models.FloatField(blank=True,default=0)
	average_response_time=models.FloatField(blank=True,default=0)
	fulfillment_rate=models.FloatField(blank=True,default=0)
	def __str__(self):
		return self.name



po_status=[("Pending","Pending"),("Completed","Completed"),("Canceled","Canceled")]
class Purchase_Order_Model(models.Model):
	po_number=models.CharField(max_length=50,unique=True)
	vendor=models.ForeignKey(Vendor_Model,on_delete=models.CASCADE,default=0)
	order_date=models.DateTimeField()
	delivery_date=models.DateTimeField()
	delivered_date=models.DateTimeField(blank=True,null=True) # To calculate on time delivery date
	items=models.JSONField()
	quantity=models.IntegerField()
	status=models.CharField(max_length=100,choices=po_status)
	quality_rating=models.FloatField(blank=True,null=True)
	issue_date=models.DateTimeField(blank=True,null=True) #Keeping the null=True is crucial for fulfillment rate calculation
	acknowledgement_date=models.DateTimeField(null=True)
	def __str__(self):
		return self.po_number


@receiver(post_save, sender=Purchase_Order_Model)
def update_vendor_model(sender, instance, **kwargs):
	vendor_instance = instance.vendor

	# Calculate On-Time Delivery Rate
	if instance.status == 'Completed':
		completed_pos = Purchase_Order_Model.objects.filter(
			vendor=vendor_instance, status='Completed'
		).count()
		on_time_delivery_pos = Purchase_Order_Model.objects.filter(
			vendor=vendor_instance, status='Completed',delivered_date__isnull=False, delivered_date__lte=instance.delivery_date
		).count()

		vendor_instance.on_time_delivery_rate = on_time_delivery_pos / completed_pos

	# Calculate Quality Rating Average
	if instance.status == 'Completed' and instance.quality_rating is not None:
		completed_pos_with_rating = Purchase_Order_Model.objects.filter(
			vendor=vendor_instance, status='Completed', quality_rating__isnull=False
		).count()
		quality_rating_sum = Purchase_Order_Model.objects.filter(
			vendor=vendor_instance, status='Completed', quality_rating__isnull=False
		).aggregate(models.Sum('quality_rating'))['quality_rating__sum']

		vendor_instance.quality_rating_avg = quality_rating_sum / completed_pos_with_rating
	

	# Calculate Average Response Time
	if instance.acknowledgement_date is not None:
		response_times = Purchase_Order_Model.objects.filter(
			vendor=vendor_instance, acknowledgement_date__isnull=False
		).exclude(issue_date__isnull=True).exclude(acknowledgement_date__isnull=True).values_list(
			'acknowledgement_date', 'issue_date'
		)
	
		response_times = [
			(acknowledgement_date - issue_date).total_seconds() / 3600  # Convert seconds to hours
			for acknowledgement_date, issue_date in response_times
		]
		if len(response_times)!=0:
			vendor_instance.average_response_time = sum(response_times) / len(response_times)

	# Calculate Fulfilment Rate
	total_pos = Purchase_Order_Model.objects.filter(vendor=vendor_instance).count()
	fulfilled_pos = Purchase_Order_Model.objects.filter(
		vendor=vendor_instance, status='Completed', issue_date__isnull=True
	).count()

	vendor_instance.fulfillment_rate = fulfilled_pos / total_pos

	# Save the updated Vendor_Model instance
	vendor_instance.save()


	# Create Historical_Performance_Model instance
	historical_performance_instance = Historical_Performance_Model(
		vendor=vendor_instance,
		date=timezone.now(),
		on_time_delivery_rate=vendor_instance.on_time_delivery_rate,
		quality_rating_avg=vendor_instance.quality_rating_avg,
		average_response_time=vendor_instance.average_response_time,
		fulfillment_rate=vendor_instance.fulfillment_rate,
	)
	historical_performance_instance.save()




class Historical_Performance_Model(models.Model):
	vendor=models.ForeignKey(Vendor_Model,on_delete=models.CASCADE,default=0)
	date=models.DateTimeField()
	on_time_delivery_rate=models.FloatField()
	quality_rating_avg=models.FloatField()
	average_response_time=models.FloatField()
	fulfillment_rate=models.FloatField()





