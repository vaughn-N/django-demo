from django.contrib import admin

from account.models import Developer


class DeveloperAdmin(admin.ModelAdmin):
    search_fields = ["firstname", "birthdate"]
    list_display = ["firstname", "middlename", "birthdate"]


admin.site.register(Developer, DeveloperAdmin)
