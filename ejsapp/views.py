from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from .models import Mark, Subject, Student, Date
from .serializers import MarkSerializer, SubjectSerializer, StudentSerializer, DateSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    @action(detail=False, methods=['GET'], url_path="my", url_name="my")
    def get_my_subjects(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response([])

        user = request.user
        subjects = Subject.objects.filter(teacher=user)
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]

    @action(detail=False, methods=['GET'], url_path="by_subject", url_name="by_subject")
    def get_students_by_subject(self, request, pk=None):
        subject_id = request.query_params.get('id')

        if not request.user.is_authenticated or not subject_id:
            return Response([])

        subject = Subject.objects.filter(id=subject_id, teacher=request.user)

        if not subject:
            return Response([])

        students = Student.objects.filter(subject=subject_id)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class DateViewSet(viewsets.ModelViewSet):
    queryset = Date.objects.all()
    serializer_class = DateSerializer
    authentication_classes = [TokenAuthentication]

    @action(detail=False, methods=['GET'], url_path="by_subject", url_name="by_subject")
    def get_dates_by_subject(self, request):
        subject_id = request.query_params.get('id')

        if not request.user.is_authenticated or not subject_id:
            return Response([])

        subject = Subject.objects.filter(id=subject_id, teacher=request.user)
        if not subject:
            return Response([])

        dates = Date.objects.filter(subject=subject_id)
        serializer = DateSerializer(dates, many=True)
        return Response(serializer.data)


class MarkViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    authentication_classes = [TokenAuthentication]

    @action(detail=False, methods=['GET'], url_path="by_student", url_name="by_student")
    def get_marks_by_student_and_date(self, request):
        student_id = request.query_params.get('student_id')
        date_id = request.query_params.get('date_id')

        if not request.user.is_authenticated or not student_id or not date_id:
            return Response([])

        marks = Mark.objects.filter(student=student_id, date=date_id)
        serializer = MarkSerializer(marks, many=True)
        return Response(serializer.data)




