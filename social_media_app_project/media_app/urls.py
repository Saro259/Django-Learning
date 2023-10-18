from django.urls import path
from media_app.views import index_view
urlpatterns = [
    path('', index_view, name='index_view'),
]