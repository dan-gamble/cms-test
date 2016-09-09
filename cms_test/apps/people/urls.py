from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^teams/$", views.TeamListView.as_view(), name='team_list'),
    url(r"^team/(?P<team_title>[a-z-]+)/$", views.TeamView.as_view(), name='team'),
    url(r"^$", views.PersonListView.as_view(), name="person_list"),
    url(r"^(?P<person_title>[a-z-]+)/$", views.PersonView.as_view(), name='person')
]
