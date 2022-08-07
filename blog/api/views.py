from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializer import PostSerializer
from api.models import Post
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# list the post blog
class ViewList(APIView):
    def get(self, request):
        blog = Post.objects.all()
        serialzer = PostSerializer(blog, many=True)
        return Response({'status':200, 'payload': serialzer.data})

