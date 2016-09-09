from cms.admin import PageBaseAdmin, SearchMetaBaseAdmin
from django.contrib import admin

from .models import Person, Team


@admin.register(Person)
class PersonAdmin(SearchMetaBaseAdmin):

    prepopulated_fields = {"url_title": ("first_name", "last_name",)}
    filter_horizontal = ("teams",)

    fieldsets = (
        (None, {
            "fields": (
                "page",
            )
        }),
        ('Name information', {
            'fields': (
                "title",
                "first_name",
                "middle_name",
                "last_name",
                "url_title",
            )
        }),
        ('Additional information', {
            'fields': (
                "photo",
                "job_title",
                "bio",
                "teams",
                "order",
            )
        }),
        ('Contact details', {
            'fields': (
                "email",
                "linkedin_username",
                "skype_username",
                "twitter_username",
            )
        }),
        SearchMetaBaseAdmin.PUBLICATION_FIELDS,
        SearchMetaBaseAdmin.SEO_FIELDS,
    )


@admin.register(Team)
class TeamAdmin(PageBaseAdmin):

    prepopulated_fields = {
        "slug": ("title",)
    }

    fieldsets = (
        PageBaseAdmin.TITLE_FIELDS,
        ("Content", {
            "fields": ("content_primary",),
        }),
        PageBaseAdmin.PUBLICATION_FIELDS,
        PageBaseAdmin.NAVIGATION_FIELDS,
        PageBaseAdmin.SEO_FIELDS,
    )
