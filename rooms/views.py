# from django.core.paginator import Paginator, EmptyPage
# from django.http import Http404
# from django.urls import reverse
# from django.shortcuts import render # redirect
from django.views.generic import ListView, DetailView
from . import models


class Homeview(ListView):

    """ Homeview Definition with class based view """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ RoomDetail Definition """ 

    model = models.Room




# HomeView - Pagination manual coding 1
"""  
def all_rooms(request):
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    page_count = ceil(models.Room.objects.count() / page_size)
    return render(
        request,
        "rooms/home.html",
        context={
            "rooms": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count),
        },
    )
"""

# HomeView - Pagination manual coding 2
""" 
def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", context={"page": rooms})
    except EmptyPage:
        rooms = paginator.page(1)
        return redirect("/")
"""


# RoomDetail - function based view
""" 
def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        #return redirect(reverse("core:home"))  # main page redirect
        raise Http404()    # Http 404 Errorpage
"""