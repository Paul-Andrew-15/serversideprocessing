from django.shortcuts import render

# Create your views here.
def areacalculation(request):
    context = {}
    context["area"] = "0"
    context["b"] = "0"
    context["h"] = "0"
    if request.method == "POST":
        b = request.POST.get("base","0")
        h = request.POST.get("height","0")
        area = ((int(b) * int(h))/2)
        context["area"] = area
        context["b"] = b
        context["h"] = h
    return render(request,"mathapp/area.html",context)