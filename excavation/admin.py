from django.contrib import admin
from excavation.models import *


class AreaAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
    prepopulated_fields = {'slug': ('name',)}  # added to auto-populate the slug with the same name fi


class TrenchAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'area', 'editor', ]
    list_filter = ['area', 'editor', ]
    search_fields = ['name', ]
    prepopulated_fields = {'slug': ('name',)}  # added to auto-populate the slug with the same name field


class BuildingAdmin(admin.ModelAdmin):
    autocomplete_fields = ['area', ]
    prepopulated_fields = {'slug': ('name',)}  # added to auto-populate the slug with the same name field


class FindAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # added to auto-populate the slug with the same name fi


class FindingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # added to auto-populate the slug with the same name fi


class IndexAdmin(admin.ModelAdmin):
    pass


class AboutAdmin(admin.ModelAdmin):
    pass


class ContactAdmin(admin.ModelAdmin):
    pass


class TopographyAdmin(admin.ModelAdmin):
    pass


class HistoryAdmin(admin.ModelAdmin):
    pass

class MonumentAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
    prepopulated_fields = {'slug': ('name',)}  # added to auto-populate the slug with the same name fi


admin.site.register(HomePage, IndexAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Topography, TopographyAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Monument, HistoryAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Trench, TrenchAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Find, FindAdmin)
admin.site.register(Finding, FindingAdmin)
