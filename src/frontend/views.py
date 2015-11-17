from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from frontend.models import Tree

def home(request):
    return render(request, "frontend/home.html")

def map(request):
    return render(request, "frontend/map.html",
    {
        "trees": Tree.objects.all()
    })

# @TODO: remove exempt find way to post with csrf token.
@csrf_exempt
def create(request):
    if request.method =='POST':
        tree = Tree(
            name = request.POST["name"],
            latitude = request.POST["location[latitude]"],
            longitude = request.POST["location[longitude]"],
            memory = request.POST["memory"]
        )
        tree.save()
        return render(request, "frontend/map.html")
    else:
        return render(request, "frontend/create.html")

def info(request):
    return render(request, "frontend/info.html")
