import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from cfeapi.mixins import JsonResponseMixin
from .models import Updates
from django.core.serializers import serialize


def json_example_view(request):
    # URI -- for REST API
    data = {
        "count": 100,
        "content": "Some new content"
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(data)


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 100,
            "content": "Some new content"
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 100,
            "content": "Some new content"
        }
        return self.render_to_response(data)


class SerializedDetailView(View):
    def get(self,request, *args, **kwargs):
        obj = Updates.objects.get(id=1)
        json_data = obj.serialize()
        # data = serialize("json", [obj, ], fields=("user", "content"))
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Updates.objects.all()
        # data = serialize("json", qs, fields=("user", "content"))
        json_data = Updates.objects.all().serialize()
        return HttpResponse(json_data, content_type='application/json')
