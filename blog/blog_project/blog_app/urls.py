from django.conf.urls import url

from . import views

urlpatterns=[url(r'^$',views.BlogListView.as_view(),name='post_list'),
             url(r'^post/(?P<pk>\d+)/$',views.BlogDetailView.as_view(),name="post_detail")]
