""" URLs used by the faqs app """
from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
                       url(
                           r"^categories/$",
                           views.FaqCategoryListView.as_view(),
                           name="category_list"
                       ),
                       url(
                           r"^categories/(?P<category_title>[\w-]+)/$",
                           views.FaqCategoryView.as_view(),
                           name="category"
                       ),
                       url(
                           r"^$",
                           views.FaqListView.as_view(),
                           name="faq_list"
                       ),
                       url(
                           r"^(?P<faq_title>[\w-]+)/$",
                           views.FaqView.as_view(),
                           name="faq"
                       ),
)
