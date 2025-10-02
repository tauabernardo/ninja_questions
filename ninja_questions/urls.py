from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI



api = NinjaAPI()

@api.get("/questions")
def get_questions(request):
    return 1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', include('cadastro.urls')),
]
