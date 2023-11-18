from parser.views import DawnloadView, MarksListView, ModelsDetailedListView
from django.contrib import admin
from django.urls import path


urlpatterns = [   
    path('mark/<int:pk>/', ModelsDetailedListView.as_view(), name="detail"),
    path("update_autoru_catalog", DawnloadView.as_view(), name='update_catalog'),
    path("", MarksListView.as_view(), name='landing-page'),
    path('admin/', admin.site.urls),
]
