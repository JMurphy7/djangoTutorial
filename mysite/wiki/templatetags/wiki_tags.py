from django import template
import markdown

register = template.Library()

@register.filter
def markup(text):
    f = markdown.markdown(text)
    print(f)
    return f
