from django.shortcuts import render
from .models import Company
from.serializers import CompanySerilizer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

def adddetails(request):
    companyModel =  Company()
    if request.method == "POST":
        companyModel.company_name = request.POST["company_name"]
        companyModel.company_phone = request.POST['company_phone']
        companyModel.company_email = request.POST['company_email']
        companyModel.industry = request.POST['industry']
        companyModel.company_gst = request.POST['company_gst']
        companyModel.company_pancard = request.POST['company_pancard']
        companyModel.company_website = request.POST['company_website']
        companyModel.address_line1 = request.POST['address_line1']
        companyModel.street = request.POST['street']
        companyModel.area_building = request.POST['area_building']
        companyModel.landmark = request.POST['landmark']
        companyModel.city = request.POST['city']
        companyModel.state = request.POST['state']
        companyModel.pincode = request.POST['pincode']
        companyModel.country = request.POST['country']

        companyModel.par_company_name = request.POST['par_company_name']
        companyModel.par_industry = request.POST['par_industry']
        companyModel.par_company_gst = request.POST['par_company_gst']
        companyModel.par_company_pancard = request.POST['par_company_pancard']
        companyModel.par_company_phone = request.POST['par_company_phone']
        companyModel.par_company_email = request.POST['par_company_email']
        companyModel.par_company_website = request.POST['par_company_website']
        companyModel.par_address_line1 = request.POST['par_address_line1']
        companyModel.par_street = request.POST['par_street']
        companyModel.par_area_building = request.POST['par_area_building']
        companyModel.par_landmark = request.POST['par_landmark']
        companyModel.par_city = request.POST['par_city']
        companyModel.par_state = request.POST['par_state']
        companyModel.par_pincode = request.POST['par_pincode']
        companyModel.mark_parent = request.POST['mark_parent']

        companyModel.save()
        return render(request,"form.html",)
    return render(request,"form.html")

@api_view(['GET', 'POST'])
def detaildata(request):
    if request.method == "GET":
        queryset = Company.objects.all()
        serialzer = CompanySerilizer(queryset,many=True)
        return Response(serialzer.data)
    return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)