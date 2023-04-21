from django import template

register = template.Library()

@register.filter
def has_filter(applied_filters, filter_value):
    return any(filter_val == filter_value for _, filter_val in applied_filters)
