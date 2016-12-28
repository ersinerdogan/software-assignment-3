from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.http import Http404,HttpResponse
from django.shortcuts import render
from tags.models import Tag
from .models import Bloggg
from .forms import BlogggForm
def show_blog(request):
    if request.method=="POST":
        form = BlogggForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.owner = request.user
            entry.save()
            form.save_m2m()
    elif request.method == "GET":
        form = BlogggForm()


    return render(request, "bloggg.html", {"entries": Bloggg.objects.filter(owner=request.user.id), "tags": Tag.objects.all(), "form":form})

def get_blog(request, entry_id):
    try:
        entry = Bloggg.objects.get(id=entry_id)
        if request.user.id != entry.owner.id:
            raise PermissionDenied
        return render(request, "detailed_bloggg.html", {"entry":entry})
    except Bloggg.DoesNotExist:
        raise Http404("We dont have any")
