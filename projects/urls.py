from django.conf.urls import url

from .views import ProjectList, ProjectDetail

urlpatterns = [

    url(r'^$', ProjectList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', ProjectDetail.as_view(), name='detail'),

]
