from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'campaigns/lobby.html')

def info(request, id):
	return render(request, 'campaigns/campaignDesc.html')

def manage(request, id):
	return render(request, 'campaigns/campaignManage.html')