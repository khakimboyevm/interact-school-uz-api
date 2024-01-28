from rest_framework import serializers
from .models import Langulages, MainTitles, Titles, Content, Blog, Foydali_Saytlar, Category

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Langulages
        fields = ['id', 'name', 'slug', 'image', 'category_type']

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'name', 'slug', 'title_type', 'content_text', ]


class TitlesSerializer(serializers.ModelSerializer):
    content = ContentSerializer(many=True, read_only=True,  source='content_set')
    class Meta:
        model = Titles
        fields = ['id', 'name', 'slug', 'maintitle_type', 'content']

class MainTitlesSerializer(serializers.ModelSerializer):
    titles = TitlesSerializer(many=True, read_only=True,  source='titles_set')
    class Meta:
        model = MainTitles
        fields = ['id', 'name', 'slug', 'language_type', "titles"]



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'name', 'slug', 'category_type', 'author', 'about', 'image', 'blog_content']

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foydali_Saytlar
        fields = ['id', 'name', 'slug', 'category_type','about', 'image', 'description']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class LanguageApiSerializer(serializers.ModelSerializer):
    category_type = CategorySerializer()

    class Meta:
        model = Langulages
        fields = ['id', 'name', 'slug', 'image', 'category_type']