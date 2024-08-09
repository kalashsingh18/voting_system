from django.contrib import admin
from django.urls import path,include
from login_apis import urls
from.import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.create_unique_id,name="create_candidates"),
    path("/do_votes",views.do_vote,name="do_votes"),
    path("/create",views.create_unique_id,name="create_id"),
    path("/extract",views.select_election,name="decode"),
]