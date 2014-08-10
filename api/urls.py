from django.conf.urls import patterns, url
from api import views

urlpatterns = patterns('',
    url(r'^comments/$', views.CommentList.as_view(), name="comment-list"),
    url(r'^comments/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view(), name="comment-detail"),

    url(r'^posts/$', views.PostList.as_view(), name="post-list"),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name="post-detail"),
    url(r'^posts/(?P<pk>[0-9]+)/comments/$', views.PostCommentList.as_view(), name="postcomment-list"),

    url(r'^users/$', views.UserList.as_view(), name="user-list"),
    url(r'^users/(?P<username>[a-zA-Z0-9]+)/$', views.UserDetail.as_view(), name="user-detail"),
    url(r'^users/(?P<username>[a-zA-Z0-9]+)/posts/$', views.UserPostList.as_view(), name="user-detail"),
)
