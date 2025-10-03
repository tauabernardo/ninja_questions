from django.urls import path
from .api import api
from cadastro.views import upload_page


urlpatterns = [
    path('api/', api.urls),
    path('upload/', upload_page, name='upload_page'), 
]