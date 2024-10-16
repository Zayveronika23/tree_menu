from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Paragraph


class ParagraphAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Paragraph, ParagraphAdmin)
