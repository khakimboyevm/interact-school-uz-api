from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


urlpatterns = [
    path("categories/", CategoryAPIView.as_view(), name="category"),
    path("languages/", LanguageAPIView.as_view(), name="language"),
    path("blog/", BlogAPIView.as_view(), name="blog"),
    path("blog-categories/", BlgoCategoryAPIView.as_view(), name="blog-category"),
    path("image/<str:part>/", dynamic_view, name="dynamic"),
    path("site-categories/", SiteCategoryAPIView.as_view(), name="site-category"),
    path("carusel/", CaruselAPIView.as_view(), name="carusel"),
    path('languages/<slug:category_slug>/', LanguageListView.as_view(), name='language-list'),
    path('maintitles/<slug:language_slug>/', MainTitlesListView.as_view(), name='maintitles-list'),
    path('titles/<slug:maintitles_slug>/', TitleListView.as_view(), name='titles-list'),
    path('contents/<slug:titles_slug>/', ContentListView.as_view(), name='content-list'),
    path('blogs/<slug:blog_categorys_slug>/', BlogListView.as_view(), name='blog-list'),
    path('sites/<slug:site_category_slug>/', SiteListView.as_view(), name='site-list'),
]
