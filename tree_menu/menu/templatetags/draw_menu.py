from pathlib import Path

from django import template

from ..models import Paragraph

BASE_DIR = Path(__file__).resolve().parent.parent


register = template.Library()


@register.inclusion_tag(f'{BASE_DIR}/templates/draw_menu.html')
def draw_menu(menu):
    paragraphs = Paragraph.objects.filter(menu_title=menu)
    return {'paragraphs': paragraphs}
