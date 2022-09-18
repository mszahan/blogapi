from urllib import request
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #read-only permission to any requests
        # If a request contains HTTP verbs included in SAFE_METHODS–a tuple containing GET,......
        # OPTIONS, and HEAD–then it is a read-only request and permission is granted.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Otherwise the request is for a write of some kind
        # if the author is not right then the following code will return false
        #writing permission to only the author of the post
        return obj.author == request.user
