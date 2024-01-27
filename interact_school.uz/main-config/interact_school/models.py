from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

class Langulages(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(blank=True)
    description = models.CharField(max_length=4096, blank=True, null=True)
    category_type = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Langulages, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

class MainTitles(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    language_type = models.ForeignKey(Langulages, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(MainTitles, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Titles(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    maintitle_type = models.ForeignKey(MainTitles, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Titles, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
    
class Content(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(unique=True, blank=True)
    title_type = models.ForeignKey(Titles, on_delete=models.CASCADE)
    content_text = RichTextField()


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Content, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


# _____________________________________________________


class Blog_Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Blog_Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

class Site_Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Site_Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Carusel(models.Model):
    name = models.CharField(max_length=70)
    any_url = models.URLField(blank=True)
    image = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.name
    
class Blog (models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(unique=True, blank=True)
    category_type = models.ForeignKey(Blog_Category, on_delete=models.CASCADE)
    author = models.CharField(max_length=70, blank=True)
    about = models.CharField(max_length=140)
    image = models.URLField()
    blog_content = RichTextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  
        super(Blog, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
    
class Foydali_Saytlar (models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(unique=True, blank=True)
    category_type = models.ForeignKey(Site_Category, on_delete=models.CASCADE)
    about = models.CharField(max_length=140)
    image = models.URLField()
    description = models.CharField(max_length=4096)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Foydali_Saytlar, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name