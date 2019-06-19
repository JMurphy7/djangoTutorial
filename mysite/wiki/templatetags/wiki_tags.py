from django import template
import markdown, re

wikiWordV2 = re.compile(r"\[\[([A-Za-z0-9_]+)\]\]")
register = template.Library()

@register.filter
def markup(text):
    return markdown.markdown(text)    # Allows the use of markdown

@register.filter
def wikify(text):             # Allows text to be made to link to another wiki
    return wikiWordV2.sub(r'''
    <a href="/wiki/\1/">\1</a>
    ''', text)
