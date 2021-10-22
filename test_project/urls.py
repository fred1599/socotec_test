from django.contrib import admin

from django.urls import path
from django.urls import include
from django.urls import reverse_lazy

from django.views.generic.base import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url=reverse_lazy("admin:index"))),
    path("admin/", admin.site.urls),
    path("movie/", include("movie.urls")),
]
