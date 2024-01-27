from rest_framework.request import Request
from rest_framework.generics import ListAPIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters
from django.http import HttpResponse



def dynamic_view(request, part):
    try:
        with open(f"././{part}", "rb") as file:
            return HttpResponse(file.read(), content_type="image/jpeg")
    except FileNotFoundError:
        return HttpResponse("Rasm topilmadi", status=404) 
    

class CategoryAPIView(APIView):
    def get(self, request: Request):
            category = Category.objects.all().values()
            return Response(data=category)
    
class LanguageAPIView(APIView):
    def get(self, request):
        languages = Langulages.objects.all()
        serializer = LanguageApiSerializer(languages, many=True)
        return Response(serializer.data)
    

class CaruselAPIView(APIView):
    def get(self, request: Request):
            carusel = Carusel.objects.all().values()
            return Response(data=carusel)
    
class BlogAPIView(APIView):
    def get(self, request: Request):
            blog = Blog.objects.all().values()
            return Response(data=blog)
    
class SiteCategoryAPIView(APIView):
    def get(self, request: Request):
            site_category = Site_Category.objects.all().values()
            return Response(data=site_category)
    
class BlgoCategoryAPIView(APIView):
    def get(self, request: Request):
            blog_category = Blog_Category.objects.all().values()
            return Response(data=blog_category)
    
class languageAPIView(APIView):
    def get(self, request: Request):
            langulages = Langulages.objects.all().values()
            return Response(data={"languages": langulages})
    
class MaintitleAPIView(APIView):
    def get(self, request: Request):
            maintitle = MainTitles.objects.all().values()
            return Response(data={"maintitle": maintitle})
    
class TitleAPIView(APIView):
    def get(self, request: Request):
            titles = Titles.objects.all().values()
            return Response(data={"title": titles})
    
class ContentAPIView(APIView):
    def get(self, request: Request):
            content = Content.objects.all().values()
            return Response(data={"content": content})
    

class LanguageListView(ListAPIView):
    queryset = Langulages.objects.all()
    serializer_class = LanguageSerializer()
    filter_backends = [filters.SearchFilter]
    search_fields = ['category_type__slug']

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            return Langulages.objects.filter(category_type__slug=category_slug)
        else:
            return Langulages.objects.all()


class MainTitlesListView(ListAPIView):
    queryset = MainTitles.objects.all()
    serializer_class = MainTitlesSerializer
    filter_maintitles = [filters.SearchFilter]
    search_fields = ['language_type__slug']

    def get_queryset(self):
        language_slug = self.kwargs.get('language_slug')
        if language_slug:
            return MainTitles.objects.filter(language_type__slug=language_slug)
        else:
            return MainTitles.objects.all()


class TitleListView(ListAPIView):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    filter_titless = [filters.SearchFilter]
    search_fields = ['maintitle_type__slug']

    def get_queryset(self):
        maintitle_slug = self.kwargs.get('maintitles_slug')
        if maintitle_slug:
            return Titles.objects.filter(maintitle_type__slug=maintitle_slug)
        else:
            return Titles.objects.all()
        
class ContentListView(ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_content = [filters.SearchFilter]
    search_fields = ['title_type__slug']

    def get_queryset(self):
        title_slug = self.kwargs.get('titles_slug')
        if title_slug:
            return Content.objects.filter(title_type__slug=title_slug)
        else:
            return Content.objects.all()
        
class BlogListView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_blog = [filters.SearchFilter]
    search_fields = ['category_type__slug']

    def get_queryset(self):
        blog_category_slug = self.kwargs.get('blog_categorys_slug')
        if blog_category_slug:
            return Blog.objects.filter(category_type__slug=blog_category_slug)
        else:
            return Blog.objects.all()
        
class SiteListView(ListAPIView):
    queryset = Foydali_Saytlar.objects.all()
    serializer_class = SiteSerializer
    filter_site = [filters.SearchFilter]
    search_fields = ['category_type__slug']

    def get_queryset(self):
        site_category_slug = self.kwargs.get('site_category_slug')
        if site_category_slug:
            return Foydali_Saytlar.objects.filter(category_type__slug=site_category_slug)
        else:
            return Foydali_Saytlar.objects.all()