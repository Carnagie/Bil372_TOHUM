from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request ,*args, **kwargs):
	print(request)
	data_dict = {
	"user_name":"bahad",
	"label": ["adana","izmir","ankara","muğla","kırıkkale","şanlı urfa","antalya","ığdır","tekirdağ","kars"]
	}
	return render(request, "index.html", data_dict)

def contact_view(request ,*args, **kwargs):
	return render(request, "index.html", {})