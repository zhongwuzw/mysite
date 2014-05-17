#-*-coding:utf-8-*
from django.contrib import admin
from books.models import Publisher,Author,Book
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email',)
    search_fields = ('first_name','last_name',)#可以在管理页面进行字段的查询

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','publication_date',)
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)
# Register your models here.Let admin page manage the databases.zhongwu
admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)#自定义类来在管理页中进行信息的展示
admin.site.register(Book,BookAdmin)
