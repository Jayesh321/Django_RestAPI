from django.conf.urls import url
from django.urls import path, include
#from testapp.views import Article_list, Article_Detail
# from testapp.views import ArticleAPIView, ArticleDetail
#from testapp.views import GenricAPIView

# REST Framework Viewsets & Routers:
from testapp.views import ArticleViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet, basename = 'article')




urlpatterns = [

    # REST Framework Function Based API Views 
    # url('article/', Article_list),
    # url('detail/(?P<pk>\d+)/',Article_Detail),

    # REST Framework api_view() Decorator
    # url('article/', Article_list),
    # url('detail/(?P<pk>\d+)/',Article_Detail),
    
    # REST Class Based API Views
    # url('article/', ArticleAPIView.as_view()),
    # url('detail/(?P<id>\d+)/',ArticleDetail.as_view()),

    # REST Generic Views & Mixins
    #url('generic/article/(?P<id>\d+)/', GenricAPIView.as_view()),

    # REST Framework Viewsets & Routers:
    url('viewset/',include(router.urls))
    


]
