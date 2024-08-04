from django.contrib import admin
from django.urls import path,include
from login_apis import urls
from.import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.create_candidates.as_view(),name="create_candidates"),
]