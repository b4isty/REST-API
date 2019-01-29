from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from .serializers import StatusSerializer
from status.models import Status


class StatusListSearchAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)


class StatusAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request,*args, **kwargs):
        return self.create(request, *args, **kwargs)


# class StatusCreateAPIView(generics.CreateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class StatusDetailAPIView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    # lookup_field = 'id'  # 'slug


# class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin,generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     # lookup_field = 'id'  # 'slug
#
#
#     def put(self, requests, *args, **kwargs):
#         return self.update(requests, *args, **kwargs)
#
#     def delete(self, requests, *args, **kwargs):
#         return self.destroy(requests, *args, **kwargs)

    # def get_object(self, *args, **kwargs):
    #     kwargs = self.kwargs
    #     kw_id = kwargs.get('id')
    #     return Status.objects.get(id=kw_id)


class StatusUpdateAPIView(generics.UpdateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusDeleteAPIView(generics.DestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

# class StatusCreateAPIView(generics.CreateView):
#     queryset = Status.objects.all()
#     serializer_class = StatusForm
