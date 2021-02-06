from django.conf.urls import url
from basic_app.views import other,relative

# TEMPLATE TAGGING
app_name='basic_app'

urlpatterns=[
    url(regex=r'^other/$',view=other,name='other'),
    url(regex=r'^relative/$',view=relative,name='relative')
]