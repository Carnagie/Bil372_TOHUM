from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request ,*args, **kwargs):
	print(request)
	data_dict = {
	"user_name":"bahad",
	"user_data_example": [1, 2, 3, 4]
	}
	return render(request, "index.html", data_dict)

def contact_view(request ,*args, **kwargs):
	return render(request, "index.html", {})