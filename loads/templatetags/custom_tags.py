from django import template

register = template.Library()
#For bootstrap columns
@register.filter
def as_bootstrap_column(field, col_width=12):
    return f'<div class="col-md-{col_width}"><div class="form-group">{field}</div></div>'