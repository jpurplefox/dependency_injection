from django.urls import include, path

urlpatterns = [
    path('pokemon/', include('pokemon.urls')),
]
