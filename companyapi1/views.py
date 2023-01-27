from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("home page requested")
    friends = ["swap", "ravi", "uttam"]
    return JsonResponse(friends, safe=False)