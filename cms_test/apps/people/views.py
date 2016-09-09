from django.views.generic import DetailView, ListView

from .models import Person, Team


class PersonListView(ListView):
    model = Person

    def get_paginate_by(self, queryset):
        """Returns the number of jobs to show per page."""
        return self.request.pages.current.content.per_page


class PersonView(DetailView):
    model = Person
    slug_field = 'url_title'
    slug_url_kwarg = 'person_title'


class TeamListView(ListView):
    model = Team


class TeamView(DetailView):
    model = Team
    slug_field = 'url_title'
    slug_url_kwarg = 'team_title'
