try:
    from rest_framework import status
    from rest_framework.response import Response
    from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, UpdateAPIView
except ImportError:
    install = 'pip3 install django-talkto[rest]'
    raise ImportError(f"Error importing Django Rest Framework module, try install it using {install}")

from django.conf import settings

if 'rest_framework' not in settings.INSTALLED_APPS:
    raise ValueError("'rest_framework' not in INSTALLED_APPS")


class TalkToAPIView(CreateAPIView, ListAPIView, UpdateAPIView):

    def __init__(self):
        super(TalkToAPIView, self).__init__()

    def get_queryset(self):
        pass

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            # check if many is required
            if isinstance(data, list):
                kwargs["many"] = True

        return super(ListAPIView, self).get_serializer(*args, **kwargs)

    def put(self, request, *args, **kwargs):
        assert self.model is not None, (
                "'%s' should either include a `model` attribute"
                % self.__class__.__name__
        )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=self.get_success_headers(serializer.data))

    def post(self, request, *args, **kwargs):
        assert self.model is not None, (
                "'%s' should either include a `model` attribute"
                % self.__class__.__name__
        )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=self.get_success_headers(serializer.data))

    def get(self, request, *args, **kwargs):
        assert self.model is not None, (
                "'%s' should either include a `model` attribute"
                % self.__class__.__name__
        )
        params = request.GET
        if params:
            resp = self.model.api.get(**params)
        else:
            resp = self.model.api.get()
        serializer = self.get_serializer(data=resp.json(), many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK,
                        headers=self.get_success_headers(serializer.data))
