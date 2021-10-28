from django.contrib import admin
from .models import HomePage

# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'button_text',
    )


# Register your models here.
admin.site.register(HomePage, HomeAdmin)