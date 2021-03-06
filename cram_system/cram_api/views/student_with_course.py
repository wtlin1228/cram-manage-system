from rest_framework import generics
from rest_framework.response import Response
from cram_api.services.student_with_course import *


class StudentInCourseList(generics.RetrieveAPIView):
    """
    List all Students in a specified course.
    """
    def get(self, request, course_id, format=None):
        content = get_course_student_by_course_id(course_id)
        return Response(content)


class StudentInCoursesDayList(generics.RetrieveAPIView):
    """
    List all students of the courses in a specific day.
    """
    def get(self, request, day, format=None):
        content = get_course_student_by_day(day)
        return Response(content)


class StudentInAllCoursesList(generics.RetrieveAPIView):
    """
    List all students for all courses.
    """
    def get(self, request, format=None):
        content = get_all_course_student()
        return Response(content)


class StudentSigningTableDayList(generics.RetrieveAPIView):
    """
    List all signing tables in a specific day.
    """
    def get(self, resuest, date, format=None):
        content = get_course_signing_by_date(date)
        return Response(content)


class StudentSigningTableDayRangeList(generics.RetrieveAPIView):
    """
    List all signing tables in a day range.
    """
    def get(self, request, date_start, date_end, format=None):
        content = get_course_signing_by_date_range(date_start, date_end)
        return Response(content)


class StudentCreateCourseSigning(generics.RetrieveAPIView):
    """
    Create Course signing table for a specific day.
    
    input example : 
    {
        date = 2017-4-26
    }
    """
    def get(self, request, date, format=None):
        content = create_course_signing_by_date(date)
        return Response(content)


class StudentCreateSingleCourseBank(generics.RetrieveAPIView):
    """
    Create course bank for each student for a specific course.
    """
    def get(self, request, course_id, format=None):
        content = create_course_bank_by_course_id(course_id)
        return Response(content)


class StudentCreateAllStudentBank(generics.RetrieveAPIView):
    """
    Create course bank for each student for the all courses.
    """
    def get(self, request, format=None):
        content = create_all_course_bank()
        return Response(content)



