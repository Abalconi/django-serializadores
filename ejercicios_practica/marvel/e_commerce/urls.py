from django.urls import path, include
from e_commerce.marvel_views import *


urlpatterns = [
    path('get-comics/', get_comics),
    path('purchased-item/', purchased_item),
    path('e-commerce/api/', include('e_commerce.api.urls')),
]
