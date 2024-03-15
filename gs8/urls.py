
from django.contrib import admin
from django.urls import path
from Curd_application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.addandshow,name='addandshow'),
    path('delete/<int:id>/',views.delete_data,name='deletedata'),
    path("<int:id>/", views.update_data, name="updatedata")
]
