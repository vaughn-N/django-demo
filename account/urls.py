from django.urls import path

# from .views import home_view
from . import views as v
#name="account"

urlpatterns = [
    path('dev/', v.home_view, name="index"),
    path('entry/', v.entry_view, name="entry"),
    path('modelentry/', v.model_entry_view, name="modelentry"),
    path('htmxget/', v.htmxget, name="htmxget"),
]
