from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

admin.site.register(Category)
admin.site.register(Langulages)
admin.site.register(MainTitles)
admin.site.register(Titles)
admin.site.register(Content, MyModelAdmin)
admin.site.register(Carusel)
admin.site.register(Blog_Category)
admin.site.register(Site_Category)
admin.site.register(Foydali_Saytlar)
admin.site.register(Blog, MyModelAdmin)
