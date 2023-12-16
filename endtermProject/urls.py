# endtermProject/urls.py
from django.contrib import admin
from django.urls import path, include
from myapp.views import MyTokenObtainPairView  # Добавлен импорт

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Добавлен путь для получения токена
]
