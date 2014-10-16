""" Admin settings for the faqs app """
from django.contrib import admin

from cms.admin import SearchMetaBaseAdmin, PageBaseAdmin

from .models import Faq, Category


@admin.register(Faq)
class FaqAdmin(SearchMetaBaseAdmin):
    """ Admin settings for the Faq model """
    prepopulated_fields = {"url_title": ("question",)}
    filter_horizontal = ("categories",)

    fieldsets = (
        (None, {
            "fields": (
                "page",
                "question",
                "url_title",
                "answer",
                "categories",
                "order",
            )
        }),
        SearchMetaBaseAdmin.PUBLICATION_FIELDS,
        SearchMetaBaseAdmin.SEO_FIELDS,
    )


@admin.register(Category)
class CategoryAdmin(PageBaseAdmin):
    """ Admin settings for the FAQ Category model. """

    prepopulated_fields = {"url_title": ("title",)}

    fieldsets = (
        PageBaseAdmin.TITLE_FIELDS,
        ("Content", {
            "fields": ("content_primary",),
        }),
        PageBaseAdmin.PUBLICATION_FIELDS,
        PageBaseAdmin.NAVIGATION_FIELDS,
        PageBaseAdmin.SEO_FIELDS,
    )

