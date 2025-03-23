from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework.decorators import api_view,authentication_classes,permission_classes
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from .models import Books
from .serializers import BooksSerializer




@api_view(['GET','POST','PUT','DELETE','PATCH'])
      # Token Authentication
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def Books_data(request, pk=None):
  if request.method == 'GET':
    id = pk
    if id is not None:
     stu = Books.objects.get(id=id)
     serializer = BooksSerializer(stu) 
     return Response(serializer.data)   
    stu = Books.objects.all()
    serializer = BooksSerializer(stu, many=True)
    return Response(serializer.data)
  if request.method=="POST":
    serializer = BooksSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':"Data Created"})
    return Response(serializer.errors)
  if request.method == 'PUT':
    id=pk
    stu = Books.objects.get(pk=id)
    serializer = BooksSerializer(stu,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Data Completely Upadated'})
    return Response(serializer.errors)
  if request.method  == 'DELETE':
    id = pk
    stu = Books.objects.get(pk=id)
    stu.delete()
    return Response({'msg':'Data Deleted'})
  if request.method == 'PATCh':
    id=pk
    stu = Books.objects.get(pk=id)
    serializer = BooksSerializer(stu,data=request.data,partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Data Partially Upadated'})
 
    