from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=100)
    company_phone = models.CharField(max_length=20)
    company_email = models.CharField(max_length=255)
    industry = models.CharField(max_length=100)
    company_gst = models.CharField(max_length=15)
    company_pancard = models.CharField(max_length=20)
    company_website = models.URLField()
    address_line1 = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    area_building = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    country = models.CharField(max_length=100)

    par_company_name = models.CharField(max_length=100)
    par_industry = models.CharField(max_length=100)
    par_company_gst = models.CharField(max_length=15)
    par_company_pancard = models.CharField(max_length=20)
    par_company_phone = models.CharField(max_length=20)
    par_company_email = models.CharField(max_length=255)
    par_company_website = models.URLField()
    par_address_line1 = models.CharField(max_length=100)
    par_street = models.CharField(max_length=100)
    par_area_building = models.CharField(max_length=100)
    par_landmark = models.CharField(max_length=100)
    par_city = models.CharField(max_length=100)
    par_state = models.CharField(max_length=100)
    par_pincode = models.CharField(max_length=10)
    mark_parent = models.BooleanField(default=False)  # Assuming it's a boolean field

    def __str__(self):
        return self.company_name
