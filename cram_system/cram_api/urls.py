from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from cram_api.views import account_view, course_view, space_view, teacher_view, student_view


urlpatterns = [
    url(r'^api/v1.0/account/$', account_view.AccountList.as_view()),
    url(r'^api/v1.0/account/(?P<pk>[0-9]+)/$', account_view.AccountDetail.as_view()),
    url(r'^api/v1.0/course/$', course_view.CourseList.as_view()),
    url(r'^api/v1.0/course/(?P<pk>[0-9]+)/$', course_view.CourseDetail.as_view()),
    url(r'^api/v1.0/course/note/$', course_view.CourseNoteList.as_view()),
    url(r'^api/v1.0/course/note/(?P<pk>[0-9]+)/$', course_view.CourseNoteDetail.as_view()),
    url(r'^api/v1.0/space/$', space_view.SpaceList.as_view()),
    url(r'^api/v1.0/space/(?P<pk>[0-9]+)/$', space_view.SpaceDetail.as_view()),
    url(r'^api/v1.0/space/note/$', space_view.SpaceNoteList.as_view()),
    url(r'^api/v1.0/space/note/(?P<pk>[0-9]+)/$', space_view.SpaceNoteDetail.as_view()),
    url(r'^api/v1.0/teacher/$', teacher_view.TeacherList.as_view()),
    url(r'^api/v1.0/teacher/(?P<pk>[0-9]+)/$', teacher_view.TeacherDetail.as_view()),
    url(r'^api/v1.0/teacher/note/$', teacher_view.TeacherNoteList.as_view()),
    url(r'^api/v1.0/teacher/note/(?P<pk>[0-9]+)/$', teacher_view.TeacherNoteDetail.as_view()),
    url(r'^api/v1.0/teacher/arrangement/$', teacher_view.TeacherArrangeList.as_view()),
    url(r'^api/v1.0/teacher/arrangement/(?P<pk>[0-9]+)/$', teacher_view.TeacherArrangeDetail.as_view()),
    url(r'^api/v1.0/student/course/$', student_view.StudentCourseList.as_view()),
    url(r'^api/v1.0/student/course/(?P<pk>[0-9]+)/$', student_view.StudentCourseDetail.as_view()),
    url(r'^api/v1.0/student/course/bank/$', student_view.StudentCourseBankList.as_view()),
    url(r'^api/v1.0/student/course/bank/(?P<pk>[0-9]+)/$', student_view.StudentCourseBankDetail.as_view()),
    url(r'^api/v1.0/student/course/signing/$', student_view.StudentCourseSigningList.as_view()),
    url(r'^api/v1.0/student/course/signing/(?P<pk>[0-9]+)/$', student_view.StudentCourseSigningDetail.as_view()),
    url(r'^api/v1.0/student/meals/bank/$', student_view.StudentMealsBankList.as_view()),
    url(r'^api/v1.0/student/meals/bank/(?P<pk>[0-9]+)/$', student_view.StudentMealsBankDetail.as_view()),
    url(r'^api/v1.0/student/note/$', student_view.StudentNoteList.as_view()),
    url(r'^api/v1.0/student/note/(?P<pk>[0-9]+)/$', student_view.StudentNoteDetail.as_view()),
    url(r'^api/v1.0/student/plan/$', student_view.StudentPlanList.as_view()),
    url(r'^api/v1.0/student/plan/(?P<pk>[0-9]+)/$', student_view.StudentPlanDetail.as_view()),
    url(r'^api/v1.0/student/quiz/$', student_view.StudentQuizList.as_view()),
    url(r'^api/v1.0/student/quiz/(?P<pk>[0-9]+)/$', student_view.StudentQuizDetail.as_view()),
    url(r'^api/v1.0/student/$', student_view.StudentList.as_view()),
    url(r'^api/v1.0/student/(?P<pk>[0-9]+)/$', student_view.StudentDetail.as_view()),
    url(r'^api/v1.0/student/sibling/$', student_view.StudentSiblingList.as_view()),
    url(r'^api/v1.0/student/sibling/(?P<pk>[0-9]+)/$', student_view.StudentSiblingDetail.as_view()),
    url(r'^api/v1.0/student/study/bank/$', student_view.StudentStudyBankList.as_view()),
    url(r'^api/v1.0/student/study/bank/(?P<pk>[0-9]+)/$', student_view.StudentStudyBankDetail.as_view()),
    url(r'^api/v1.0/student/study/$', student_view.StudentStudyList.as_view()),
    url(r'^api/v1.0/student/study/(?P<pk>[0-9]+)/$', student_view.StudentStudyDetail.as_view()),
    url(r'^api/v1.0/student/study/signing/$', student_view.StudentStudySigningList.as_view()),
    url(r'^api/v1.0/student/study/signing/(?P<pk>[0-9]+)/$', student_view.StudentStudySigningDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
