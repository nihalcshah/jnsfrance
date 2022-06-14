from django.shortcuts import render

def HomeView(request):
    return render(request, 'home.html', context)

def termsPage(request):
	context = {}
	return render(request, 'quiz/terms.html', context)
def userPage(request):
	context = {}
	return render(request, 'quiz/user.html', context)