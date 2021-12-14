import json

from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

from .encoder import JSONLDEncoder
from .registry import registry


def nl(xs):
    return mark_safe('\n'.join(map(conditional_escape, xs)))


def ld_for_site(site, request=None):
    return nl(map(ld_print_entity, registry.get_entities(site, request)))


def ld_for_object(obj, request=None):
    return nl(map(ld_print_entity, obj.ld_entity_list(request)))


def ld_print_entity(entity):
    json_out = json.dumps(entity, cls=JSONLDEncoder, sort_keys=True)
    return mark_safe('<script type="application/ld+json">{}</script>'.format(
        json_out))
