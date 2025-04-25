from datetime import datetime
from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import generics
from .helpers import save_pdf
from django.conf import settings



from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
def home(request):
    student_obj = Student.objects.all()
    serializer = StudentSerializer(student_obj, many=True)

    return Response({'status' : 200, 'message' : serializer.data})

@api_view(['POST'])
def post_data(request):
    serializer = StudentSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status' : 200, 'payload' : serializer.data, 'message' : 'Data saved successfully'})
    else:
        return Response({'status' : 404, 'error' : serializer.errors, 'message' : 'Data not saved successfully'})

# @api_view(['PUT'])
# def update_student(request, id):
#     try:
#         student_obj = Student.objects.all(id=id)
#         serializer = StudentSerializer(student_obj, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status' : 200, 'payload' : serializer.data, 'message' : 'Data saved successfully'})
#         else:
#             return Response({'status' : 404, 'error' : serializer.errors, 'message' : 'Data not saved successfully'})
#     except Student.DoesNotExist:
#         return Response({'status' : 404, 'error' : 'Student not found', 'message' : 'Data not saved successfully'})

@api_view(['PUT'])
def update_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)
        serializer = StudentSerializer(student_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data, 'message': 'Data updated successfully'})
        else:
            return Response({'status': 400, 'error': serializer.errors, 'message': 'Validation failed'})
    except Student.DoesNotExist:
        return Response({'status': 404, 'error': 'Student not found', 'message': 'Update failed'})
    


@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)
        student_obj.delete()
        return Response({'status': 200, 'message': 'Student deleted successfully'})
    except Student.DoesNotExist:
        return Response({'status': 404, 'error': 'Student not found', 'message': 'Delete failed'})

@api_view(['GET'])
def get_book(request):
    book_obj = Book.objects.all()
    serializer = BookSerializer(book_obj, many=True)
    return Response({'status' : 200, 'payload' : serializer.data, 'message' : 'Book data fetched successfully'})

from rest_framework_simplejwt.tokens import RefreshToken


class ResgisterUser(APIView):


    def post(self, request):
      serializer = UserSerializer(data=request.data)
      if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            
            #generate a twt tokens manually
            refresh_token =RefreshToken.for_user(user)
            token_data = {
               'refresh': str(refresh_token),
               'access': str(refresh_token.access_token),
            }


            token_obj,  created = Token.objects.get_or_create(user=user)
            return Response({
                'status': 200,
                'payload': serializer.data,
                'token_auth': token_obj.key,
                'jwt': token_data

            })      
      else:
        return Response({'status': 400, 'error': serializer.errors, 'message': 'Validation failed'})
      



      
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated  


class StudentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        student_obj = Student.objects.all()
        serializer = StudentSerializer(student_obj, many=True)

        return Response({'status' : 200, 'message' : serializer.data})

    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status' : 200, 'payload' : serializer.data, 'message' : 'Data saved successfully'})
        else:
            return Response({'status' : 404, 'error' : serializer.errors, 'message' : 'Data not saved successfully'})


    def put(self, request, id=None):
        try:
          student_obj = Student.objects.get(id=id)
          serializer = StudentSerializer(student_obj, data=request.data)
          if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data, 'message': 'Data updated successfully'})
          else:
            return Response({'status': 400, 'error': serializer.errors, 'message': 'Validation failed'})
        except Student.DoesNotExist:
          return Response({'status': 404, 'error': 'Student not found', 'message': 'Update failed'})
    

    def delete(self, request, id=None):
        try:
            student_obj = Student.objects.get(id=id)
            student_obj.delete()
            return Response({'status': 200, 'message': 'Student deleted successfully'})
        except Student.DoesNotExist:
            return Response({'status': 404, 'error': 'Student not found', 'message': 'Delete failed'})

#---geneic view---



class StudentGeneric(generics.ListAPIView, generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentGeneric1(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    ookup_field = 'id ' # Specify the field to use for lookup 



# class GeneratetoPdf(APIView):
#     def get(self, request):
#         student_obj = Student.objects.all()
#         serializer = StudentSerializer(student_obj, many=True)
#         data = {
#             'today': datetime.today().date(),
#             'students': student_obj
#         }

#         file_name, status =  save_pdf(data)

#         if not status:
#             return Response({'status' : 404, 'message' : 'pdf not generated successfully'})
#         # file_path = str(settings.BASE_DIR) + f'/public/static/{file_name}.pdf'

#         return Response({
#             'status': 200,
#             'path': f'/media/{file_name}',
#             'message': 'PDF generated successfully'
#         })

class GeneratetoPdf(APIView):
    def get(self, request):
        student_obj = Student.objects.all()
        data = {
            'today': datetime.today().date(),
            'students': student_obj
        }

        file_name, status = save_pdf(data)

        if not status:
            return Response({'status': 404, 'message': 'PDF not generated successfully'})

        return Response({
            'status': 200,
            'path': f'{settings.MEDIA_URL}{file_name}',
            'message': 'PDF generated successfully'
        })