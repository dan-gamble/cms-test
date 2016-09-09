import jinja2

from django import template
from django_jinja import library

from ..models import Footer, FooterLinkGroup

register = template.Library()


@library.global_function
def get_footer_link_groups():
    return FooterLinkGroup.objects.prefetch_related("children").all()


@library.global_function
@jinja2.contextfunction
def get_footer_content():
    try:
        return Footer.objects.all()[:1][0]
    except IndexError:
        return None
