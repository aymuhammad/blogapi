from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializer import PostSerializer
from api.models import Post
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

# list the post blog
class ViewList(APIView):
    def get(self, request):
        blog = Post.objects.all()
        serialzer = PostSerializer(blog, many=True)
        return Response({'status':200, 'payload': serialzer.data})


# to add post and you must have a authentication
class AddPost(APIView):
    queryset = Post.objects.all()
    # permission_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'payload':serializer.errors, 'status':400, 'message':'Something went wrong'})
        serializer.save()
        return Response({'payload':serializer.data, 'status':200, 'message':'Blogpost is Created'})



# post detail class view api
class PostDetails(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        try:
            blog = Post.objects.get(id=pk)
            serializer = PostSerializer(blog)
            return Response({'payload':serializer.data, 'status':200})
        except ObjectDoesNotExist:
            return Response({'status': 404, 'message':'Not Found'})

    
    # to edit a post
    def patch(self,request,pk):
        try:
            blog = Post.objects.get(id=pk)
            serializer=PostSerializer(blog,data=request.data,partial=True)
            if not serializer.is_valid():
                return Response({'payload':serializer.errors,'status':400,'message':'Something went Wrong'})
            serializer.save()
            return Response({'payload':serializer.data,'status':201,'message':'Blog is successfully Updated'})
        except ObjectDoesNotExist:
            return Response({'status': 404, 'message': 'Not Found'})

    
    # to delete a post
    def delete(self,request,pk):
        try:
            blog = Post.objects.get(id=pk)
            blog.delete()
            return Response({'message':'Blog successfully Deleted', 'status':200})
        except ObjectDoesNotExist:
            return Response({'status': 404, 'message': 'Not Found'})