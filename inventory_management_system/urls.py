"""inventory_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path

from inventory_management_system import views, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home', views.index_view, name="Home"),
    path('addproduct', views.input_product_view, name="addproduct"),
    path('expenses', views.expenses_view, name="expenses"),
    path('customer/bill', views.bill_view, name="bill"),
    path('customer', views.customer_view, name="customer"),
    # path('login', views.login_view, name="login"),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
