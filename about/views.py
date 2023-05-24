from django.views.generic import TemplateView
from contest.models import Contest

class Description(TemplateView):
    template_name = 'about/description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_proposals'] = Contest.objects.count()
        return context
