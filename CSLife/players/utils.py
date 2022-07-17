from django.db.models import Count
from django.core.cache import cache

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        ]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        teams = cache.get('teams')
        if not teams:
            teams = Team.objects.annotate(Count('player'))
            cache.set('teams', teams, 60)

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['teams'] = teams
        if 'team_selected' not in context:
            context['team_selected'] = 0

        return context
