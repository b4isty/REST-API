import json
from ..models import Post
from .mixins import CSRFExemptMixin
from django.views.generic import View
from myapi.mixins import HttpResponseMixin
from ..forms import PostForm
from .utils import is_json

class PostListCreateAPIVIEW(HttpResponseMixin, CSRFExemptMixin, View):

    queryset = None

    def get_queryset(self):
        qs = Post.objects.all()
        self.queryset = qs
        return qs

    def get_object(self, id=None):
        if id is None:
            return None
        else:
            qs = self.get_queryset().filter(id=id)
            if qs.count() == 1:
                print("$$$$$$$$$",qs)
                return qs.first()
            return None

    def get(self, request, *args, **kwargs):
        print("********",type(request.body))
        data = json.loads(request.body)
        passed_id = data.get("id", None)
        if passed_id is not None:
            obj = self.get_object(id=passed_id)
            print("OBJ", obj)
            if obj is None:
                error_message = json.dumps({"message": "Object not found"})
                return self.render_to_response(error_message, status=404)
            json_data = obj.serialize()
            return self.render_to_response(json_data)
        else:
            qs = self.get_queryset()
            json_data = qs.serialize()
            return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        is_valid = is_json(request.body)
        if not is_valid:
            error_message = json.dumps({"message" : "Not valid json"})
            return self.render_to_response(error_message, status=400)

        data = json.loads(request.body)
        form = PostForm(data)
        if form.is_valid():
            form.save()
            data = json.dumps({"message": "New Object Created"})
            return self.render_to_response(data, status=201)
        elif form.errors:
            data = json.dumps({form.errors})
            return self.render_to_response(data, status=400)
        error_message = json.dumps({"message": "Not allowed"})
        return self.render_to_response(error_message, status=400)

    def put(self,request, *args, **kwargs):
        is_valid = is_json(request.body)
        if not is_valid:
            error_message = json.dumps({"message": "Not valid json"})
            return self.render_to_response(error_message, status=400)
        passed_data = json.loads(request.body)
        passed_id = passed_data.get("id", None)
        if not passed_id:
            error_message = json.dumps({"message":"This is a required field to update an item"})
            return self.render_to_response(error_message, status=400)

        obj = self.get_object(id=passed_id)
        if obj is None:
            error_message = json.dumps({"message": "Object not found"})
            return self.render_to_response(error_message, status=404)

        data = json.loads(obj.serialize())
        for key, value in passed_data.items():
            data[key] = value
        form = PostForm(data, instance=obj)
        if form.is_valid():
            form.save()
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data, status=201)
        elif form.errors:
            data = json.dumps({form.errors})
            return self.render_to_response(data, status=400)
        error_message = json.dumps({"message": "form is not valid"})
        return self.render_to_response(error_message, status=400)

    def delete(self, requests, *args, **kwargs):
        is_valid = is_json(requests.body)
        if not is_valid:
            error_message = json.dumps({"message": "Not valid json"})
            return self.render_to_response(error_message, status=400)
        passed_data = json.loads(requests.body)
        passed_id = passed_data.get("id", None)
        if not passed_id:
            error_data = json.dumps({"id": "This is a required field to delete an item"})
            return self.render_to_response(error_data, status=400)
        obj = self.get_object(id=passed_id)
        if obj is None:
            error_message = json.dumps({"message": "Object not found"})
            return self.render_to_response(error_message, status=404)

        deleted_, item = obj.delete()
        print(deleted_, item)
        if deleted_ == 1:
            json_data = json.dumps({"message": "Successfully Deleted"})
            return self.render_to_response(json_data, status=200)
        json_data = json.dumps({"message": "Not deleted"})
        return self.render_to_response(json_data, status=400)















