from django.shortcuts import render
from classes.models import Classroom
from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	DestroyAPIView,
	CreateAPIView,
	)
from .serializers import(
	ClassroomListSerializer,
	ClassroomDetailSerializer,
	ClassroomCreateSerializer,
	ClassroomUpdateSerializer,
	)

# Create your views here.

class ClassroomListView(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class =  ClassroomListSerializer


class ClassroomDetailView(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class ClassrommUpdateView(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class ClassroomCreateView(CreateAPIView):
	serializer_class = ClassroomCreateSerializer

	def perform_create(self, serializers):
		serializers.save(teacher=self.request.user)


class ClassroomDeleteView(DestroyAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'



