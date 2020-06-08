# bookstore_project/urls.py


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # User management
    path('accounts/', include('allauth.urls')),

    # Django admin
    path('admin/', admin.site.urls),

    # Local apps
    path('', include('pages.urls')),
    path('accounts/', include('users.urls')),
    path('books/', include('books.urls')),
]
