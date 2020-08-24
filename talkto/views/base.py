from django import views


class TalkToListView(views.generic.ListView):
    def __init__(self):
        super(TalkToListView, self).__init__()
        self.resp = self.model.api.all()
        self.object_list = self.resp.json() if self.resp.status_code == 200 else {}

    def get(self, request, *args, **kwargs):
        context = {'status_code': self.resp.status_code, 'object_list': self.object_list}

        return self.render_to_response(context)


class TalkToDetailView(views.generic.DetailView):
    def __init__(self):
        super(TalkToDetailView, self).__init__()
        self.api = self.model.api

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        slug = self.kwargs.get('slug')

        if pk:
            resp = self.api.get(id=pk)
        elif slug:
            slug_field = self.get_slug_field()
            resp = self.api.get(**{slug_field: slug})
        else:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )

        return resp

    def get(self, request, *args, **kwargs):
        context = {'status_code': self.get_object().status_code}
        data = self.get_object().json()[0] if self.get_object().status_code == 200 else {}
        context['object'] = data

        return self.render_to_response(context)
