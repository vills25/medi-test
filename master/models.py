from django.db import models
from .utils.generate_unique_id import custom_filename

# Create your models here.

class BaseClass(models.Model):
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now =True)
    
    class Meta:
        abstract =True

class CounterTable(BaseClass):
    last_staff_id = models.IntegerField(default=0)

    def __str__(self):
        return f"Total staff : {self.last_staff_id}"

class Features(BaseClass):
    features = models.CharField(max_length=500)

    def __str__(self):
        return f"Features : {self.features}"
                
class doctor(BaseClass):
    DIR_NAME = 'doctors-profile'
    FILENAME_WORD = 'dp'
    profile = models.ImageField(upload_to=custom_filename, default='default_images\doctor-profile.png')
    name = models.CharField(max_length= 255)
    degree = models.CharField(max_length=50)
    contact = models.CharField(max_length=255)
    total_patient = models.IntegerField(default=0)
    summary = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.name
    
class ReportType(BaseClass):
    name = models.CharField(max_length=255)
    report_charge = models.FloatField()

    def __str__(self):
        return self.name

class Patient(BaseClass):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    doctor_id = models.ForeignKey(doctor, on_delete=models.CASCADE)
    report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE)
    paid_payment = models.FloatField()
    payment_status = models.CharField(max_length=255, default='pending')
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.mobile}"    