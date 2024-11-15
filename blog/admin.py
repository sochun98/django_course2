from django.contrib import admin
from blog.models import Blog


# admin.site.register(Blog)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "user",
        "view",
    )
    