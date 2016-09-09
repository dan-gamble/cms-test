from cms.apps.media.models import ImageRefField
from cms.apps.pages.models import ContentBase, Page, PageBase
from cms.models import HtmlField, SearchMetaBase
from django.db import models


class Team(PageBase):

    content_primary = HtmlField(
        "primary content",
        blank=True
    )

    def __unicode__(self):
        return self.__str__()


class People(ContentBase):

    # The heading that the admin places this content under.
    classifier = "apps"

    # The urlconf used to power this content's views.
    urlconf = "{{ project_name }}.apps.people.urls"

    standfirst = models.TextField(
        blank=True,
        null=True
    )

    per_page = models.IntegerField(
        "people per page",
        default=5,
        blank=True,
        null=True
    )

    def __unicode__(self):
        return self.page.title


class Person(SearchMetaBase):

    page = models.ForeignKey(
        Page
    )

    title = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )

    first_name = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )

    middle_name = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )

    job_title = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )

    teams = models.ManyToManyField(
        Team,
        null=True,
        blank=True
    )

    photo = ImageRefField(
        blank=True,
        null=True
    )

    bio = HtmlField(
        blank=True,
        null=True
    )

    url_title = models.CharField(
        "URL title",
        max_length=256,
        unique=True
    )

    email = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    linkedin_username = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    skype_username = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    twitter_username = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ('order',)
        verbose_name_plural = "people"

    def __unicode__(self):
        return u"{} {}".format(
            self.first_name,
            self.last_name
        )

    def get_absolute_url(self):
        return self.page.reverse('person', kwargs={
            'person_title': self.url_title,
        })
