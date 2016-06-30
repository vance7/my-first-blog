from django.contrib import admin
from Dblog.blog.models import Tag, Blog, User
# Register your models here.

admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(User)

