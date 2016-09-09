from cms.admin import SearchMetaBaseAdmin
from django.contrib import admin

from .models import Career


@admin.register(Career)
class CareerAdmin(SearchMetaBaseAdmin):
    prepopulated_fields = {"slug": ("title",)}

    fieldsets = (
        (None, {
            "fields": ("page", "title", "slug", "location", "summary",
                       "description", "email_address", "order")
        }),
        SearchMetaBaseAdmin.PUBLICATION_FIELDS,
        SearchMetaBaseAdmin.SEO_FIELDS,
    )
