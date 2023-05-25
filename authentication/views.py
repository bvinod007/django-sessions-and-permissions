from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Books
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

class BookViews(APIView):
    @login_required
    def get(self, request):
        data = Books.objects.all()
        serializer = BookSerializer(data, many=True)
        return Response({
            'status': True,
            'message': 'Successful GET request',
            'data': serializer.data
        })
    
    @csrf_exempt
    def post(self, request):
        try:
            data = request.data
            serializer = BookSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'Succeful POST request',
                    'data': serializer.data
                })
            
            return Response({
                'status': False,
                'message': 'Invalid data',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
        return Response({
            'status': False,
            'message': 'Something went wrong',
            'data': {}
        })

@csrf_exempt
@api_view(['POST'])
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            return Response({
                'status': 400,
                'message': 'User not exist.',
            })
        
        else:
            user = authenticate(username=username, password=password)
            if user is None:
                return Response({
                    'status': 400,
                    'message': 'Invalid user credentials',
                })
            else:
                login(request, user)
                return Response({
                    'status': 200,
                    'message': 'User loggedin successfully!',
                })

@csrf_exempt
@api_view(['POST'])
def logout_page(request):
    logout(request)
    return Response({
        'status': True,
        'message': 'User logged out successfully!'
    })

@csrf_exempt
@api_view(['POST'])
def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return Response({
            'status': False,
            'message': 'User already exist!',
            })

        else:
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
            )
            user.set_password(password)
            user.save()
            return Response({
                'status': 200,
                'message': 'User Resiget succeful!',
            })
