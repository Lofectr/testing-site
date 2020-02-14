from django.shortcuts import render

def createRefForTesting(request):
	return render(request, 'createRefForTesting.html')