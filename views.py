""" Views used by the faqs app """
from django.views.generic import ListView, DetailView

from .models import Faq, Category


class FaqListView(ListView):
    """ A list of all Faqs """
    model = Faq

    def get_paginate_by(self, queryset):
        """Returns the number of faqs to show per page."""
        return self.request.pages.current.content.per_page


class FaqView(DetailView):
    """ An individual Faq """
    model = Faq
    slug_field = 'url_title'
    slug_url_kwarg = 'faq_title'


class FaqCategoryListView(ListView):
    """ A list of all Faq Categories """
    model = Category


class FaqCategoryView(DetailView):
    """ A list of all Faqs per category """
    model = Category
    slug_field = 'url_title'
    slug_url_kwarg = 'category_title'
