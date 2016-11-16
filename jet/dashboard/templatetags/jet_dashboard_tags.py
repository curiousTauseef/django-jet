from __future__ import unicode_literals
from django import template
from django.core.urlresolvers import resolve
from jet.dashboard.utils import get_current_dashboard

register = template.Library()


@register.assignment_tag(takes_context=True)
def get_dashboard(context, location):
    dashboard_cls = get_current_dashboard(location)

    resolver = resolve(context['request'].path)
    app_label = resolver.kwargs.get('app_label')

    return dashboard_cls(context, app_label=app_label)


@register.filter()
def format_change_message(log_entry):

    # Django 1.9+
    if hasattr(log_entry, "get_change_message"):
        return log_entry.get_change_message()
    else:
        return log_entry.change_message
