from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models

"""  # Pagination manual coding
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

