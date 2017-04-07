from contact import views
from django.conf.urls import url,include


urlpatterns = [
    # new url definition
    url(r'^contact/$', views.contact, name='contact'),
    ]