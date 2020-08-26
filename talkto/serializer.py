from .utils import querydict_to_dict

try:
    from rest_framework.serializers import ModelSerializer
except ImportError:
    install = 'pip3 install talkto[rest]'
    raise ImportError(f"Error importing Django Rest Framework module, try install it using {install}")


class TalkToModelSerializer(ModelSerializer):
    def save(self, **kwargs):
        data = querydict_to_dict(dict(self.data))
        return self.Meta.model.save(data)
