from django.http import JsonResponse, HttpResponse


class JsonResponseMixin(object):
    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        return context