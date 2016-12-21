from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.http import Http404,HttpResponse
from django.shortcuts import render
from tags.models import Tag
from .models import Bloggg
def show_blog(request):
    if request.method=="POST":
        entry = Bloggg.objects.create(title=request.POST.get("entry_title"), parag=request.POST.get("entry_parag"), owner=request.user)
        entry.tags.add(*request.POST.getlist("tag_names"))

    return render(request, "bloggg.html", {"entries": Bloggg.objects.filter(owner=request.user.id), "tags": Tag.objects.all()})

def get_blog(request, entry_id):
    try:
        entry = Bloggg.objects.get(id=entry_id)
        if request.user.id != entry.owner.id:
            raise PermissionDenied
        return render(request, "detailed_bloggg.html", {"entry":entry})
    except Bloggg.DoesNotExist:
        raise Http404("We dont have any")
