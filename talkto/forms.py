from django import forms

from .utils import querydict_to_dict


class TalkToModelForm(forms.ModelForm):
    def api(self):

        data = querydict_to_dict(self.data)

        return self.instance.save(data)

    def _save_m2m(self):
        pass

    def _post_clean(self):
        pass
