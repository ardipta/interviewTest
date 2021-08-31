from django.contrib import admin

# Register your models here.
from .models import UserInfo


class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = UserInfo

    list_display = ['id', 'name', 'age', 'gender', 'details', 'created_at']
    list_display_links = ['id', 'name']
    list_filter = ('name',)
    search_fields = ('name', 'details')
    list_per_page = 5


admin.site.register(UserInfo, UserAdmin)
