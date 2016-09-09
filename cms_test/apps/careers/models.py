import watson
from cms.apps.pages.models import ContentBase
from cms.models import HtmlField, SearchMetaBase
from django.db import models


class Careers(ContentBase):

    # The heading that the admin places this content under.
    classifier = "apps"

    # The urlconf used to power this content's views.
    urlconf = "{{ project_name }}.apps.careers.urls"

    standfirst = models.TextField(
        blank=True,
        null=True
    )

    per_page = models.IntegerField(
        "careers per page",
        default=5,
        blank=True,
        null=True
    )

    def __unicode__(self):
        return self.page.title


class Career(SearchMetaBase):

    page = models.ForeignKey(
        Careers
    )

    title = models.CharField(
        max_length=256,
    )

    slug = models.CharField(
        max_length=256,
        unique=True
    )

    location = models.CharField(
        max_length=256,
        blank=True,
        null=True
    )

    summary = models.TextField(
        blank=True,
        null=True
    )

    description = HtmlField()

    email_address = models.EmailField()

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.page.page.reverse('career', kwargs={
            'slug': self.slug,
        })

watson.register(Career)
