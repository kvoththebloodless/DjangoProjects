from django.conf.urls import url
from django.urls import path


from . import views

urlpatterns=[url(r'^$',views.BlogListView.as_view(),name='post_list'),
             url(r'^post/(?P<pk>\d+)/$',views.BlogDetailView.as_view(),name="post_detail"),
             url(r'^post/new/$',views.BlogCreateView.as_view(),name="post_new"),
             url(r'^post/(?P<pk>\d+)/edit/$',views.BlogUpdateView.as_view(),name="post_edit"),
             path('post/<int:pk>/delete/',views.BlogDeleteView.as_view(), name='post_delete'),
             ]
