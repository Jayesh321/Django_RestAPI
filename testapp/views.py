from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from testapp.models import Article
from testapp.serializers import ArticleSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

#REST Framework Modal Viewsets this class is using Viewsets & Routers url only:
from rest_framework import mixins
from rest_framework import viewsets

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

#REST Framework Generic Viewsets this class is using Viewsets & Routers url only:
from rest_framework import mixins
from rest_framework import viewsets

class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                                    mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = Article.objects.all()   
    serializer_class = ArticleSerializer

# REST Framework Viewsets & Routers:
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404

# class ArticleViewSet(viewsets.ViewSet):
#     def list(self, request):
#         article = Article.objects.all()
#         seralizers = ArticleSerializer(article, many=True)
#         return Response(seralizers.data)
    
#     def retrieve(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, pk=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)

#     def update(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, pk=pk)
#         serializer = ArticleSerializer(article, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#     def destroy(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset,  pk=pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# REST Generic Views & Mixins along with authentication
#---------------------------------------------------------------
# from rest_framework import mixins
# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework import status

# Authnetiction can be applied on each and every form in different style with different imported modules.

# Session and Basic authentication
#from rest_framework.authentication import SessionAuthentication, BasicAuthentication
#from rest_framework.permissions import IsAuthenticated

# Token based Authnetiction
# from rest_framework.authtoken.models import Token
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated

#----------------------------------------------------------------------------------

# class GenricAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
#                                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
#     queryset = Article.objects.all()   
#     serializer_class = ArticleSerializer
#     lookup_field = 'id'

    # Appling Session and Basic authentication Authentication classes:
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]

    # Appling token based authentication Authentication classes:
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    

    # def get(self, request, id=None):
    #     if id:
    #         return self.retrieve(request)
    #     else:
    #         return self.list(request)

    # def post(self, request):
    #     return self.create(request)

    # def put(self, request, id=None):
    #     return self.update(request, id)

    # def delete(self, request, id):
    #     return self.destroy(request, id)


# REST Class Based API Views
#--------------------------------------------------------------------
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class ArticleAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, *args, **kwargs):
#         serializer = ArticleSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ArticleDetail(APIView):
#     def get_object(self, id):
#         try:
#             return Article.objects.get(id=id)
#         except Article.DoesNotExist:
#             return HttpResponse(status = status.HTTP_404_NOT_FOUND)
        
#     def get(self, request, id):
#         article = self.get_object(id)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
    
#     def put(self, request, id):
#         article = self.get_object(id)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, id):
#         article = self.get_object(id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# REST Framework api_view() Decorator:
#---------------------------------------------------------

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# @api_view(['GET','POST'])
# def Article_list(request):
#     if request.method == 'GET':
#         article =  Article.objects.all()
#         serializer = ArticleSerializer(article, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def Article_Detail(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status = status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)




# REST Framework Function Based API Views 
#--------------------------------------------------------------

# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def Article_list(request):
#     if request.method == 'GET':
#         article =  Article.objects.all()
#         serializer = ArticleSerializer(article, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status = 201)
#         return JsonResponse(serializer.errors, status = 401)

# @csrf_exempt
# def Article_Detail(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status = 404)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data, status=201)
    
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status = 201)
#         return JsonResponse(serializer.errors, status = 400)
    
#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status = 204) 
