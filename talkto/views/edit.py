from django.http import HttpResponseRedirect
from django.views import generic


class TalkToWriteView(generic.CreateView):
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        resp = form.api()
        ok = str(resp.status_code).startswith('20')
        return HttpResponseRedirect(self.success_url) if ok else self.render_to_response(context={'form': form},
                                                                                         status=resp.status_code)
