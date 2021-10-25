from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm,VideoForm
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .serializers import userlistSerializer,CourseSerializer,VideoSerializer,EnrolledListSerializer
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from .models import Course,EnrolledList,Video
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
#'17ACggnretcmgj5yey2tC3sw5sqyUnwGfK'
def index(request):
    return render(request,'index.html')
def loginus(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('/dash')
        else:
            messages.info(request,"username or password is incorrect")
            return redirect('/login')

    else:
        return render(request,'login.html')
def register(request):
    
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "account was created successfully")
        else:
            print(form.errors)
        form =UserForm()
        context={'form':form}
        return render(request,'register.html',context=context)
    else:
        form =UserForm()
        context={'form':form}
        return render(request,'register.html',context=context)
def logoutus(request):
    return redirect('/login')
@login_required(login_url='/login')
def dash(request):
    query=Video.objects.all()
    context={'query':query[0]}
    print(query[0].title)
    return render(request,'user_home.html',context)
#rest api
@login_required(login_url='/login')
def play(request,pk):
    query=Video.objects.get(pk=pk)
    print(query.title)
    context={'query':query}
    return render(request,'page1.html',context)
@login_required(login_url='/login')
def create(request):
    
    if request.method=="POST":
        form=VideoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "content successfully")
        else:
            print(form.errors)
        form =VideoForm()
        context={'form':form}
        return render(request,'video_create.html',context=context)
    else:
        form =VideoForm()
        context={'form':form}
        return render(request,'video_create.html',context=context)
import stripe
stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
@login_required(login_url='/login')
def donate(request):
    return render(request,'payment.html')
class userlist(APIView):
    def get(self,request,format=None):

        queryset = User.objects.all()
        serializer_class = userlistSerializer

        serialized_data=serializer_class(queryset,many=True)
        print(serialized_data)
        return Response(serialized_data.data)


    def post(self,request,format=None):
        serializer_class=userlistSerializer
        serialized=serializer_class(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            serialized_data=serializer.data
            return Response(serialized_data,status=status.HTTP_201_CREATED)
        else:

            return Response(serialized.errors(),status=status.HTTP_404_BAD_REQUEST)
class EnrolledList(APIView):
    def get(self,request,format=None):
        serializer=EnrolledListSerializer
        obj=Course.objects.all()
        serialised_class=serializer(obj,many=True)
        return Response(serialised_class.data)
class CourseList(APIView):
    def get(self,request,format=None):
        serializer=CourseSerializer
        obj=Course.objects.all()
        serialised_class=serializer(obj,many=True)
        return Response(serialised_class.data)
    def post(self,request,format=None):
        serializer_class=CourseSerializer
        serialized=serializer_class(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            serialized_data=serializer.data
            return Response(serialized_data,status=status.HTTP_201_CREATED)
        else:

            return Response(serialized.errors(),status=status.HTTP_404_BAD_REQUEST)
class couserentity(APIView):
    def get(self,request,pk,format=None):
        serializer=CourseSerializer()
        obj=Course.objects.get(pk=pk)
        serialised_class=serializer(obj,many=True)
        return Response(serialised_class.data)




