from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from cram_api.views import account_view, course_view, space_view, teacher_view, student_view
from cram_api.views import student_with_course
from cram_api.views import student_with_study
from cram_api.views import study_view


urlpatterns = [
    url(r'^api/v1.0/basic/account/$', account_view.AccountList.as_view()),
    url(r'^api/v1.0/basic/account/(?P<pk>[0-9]+)/$', account_view.AccountDetail.as_view()),
    url(r'^api/v1.0/basic/course/$', course_view.CourseList.as_view()),
    url(r'^api/v1.0/basic/course/(?P<pk>[0-9]+)/$', course_view.CourseDetail.as_view()),
    url(r'^api/v1.0/basic/course/note/$', course_view.CourseNoteList.as_view()),
    url(r'^api/v1.0/basic/course/note/(?P<pk>[0-9]+)/$', course_view.CourseNoteDetail.as_view()),
    url(r'^api/v1.0/basic/space/$', space_view.SpaceList.as_view()),
    url(r'^api/v1.0/basic/space/(?P<pk>[0-9]+)/$', space_view.SpaceDetail.as_view()),
    url(r'^api/v1.0/basic/space/note/$', space_view.SpaceNoteList.as_view()),
    url(r'^api/v1.0/basic/space/note/(?P<pk>[0-9]+)/$', space_view.SpaceNoteDetail.as_view()),
    url(r'^api/v1.0/basic/teacher/$', teacher_view.TeacherList.as_view()),
    url(r'^api/v1.0/basic/teacher/(?P<pk>[0-9]+)/$', teacher_view.TeacherDetail.as_view()),
    url(r'^api/v1.0/basic/teacher/note/$', teacher_view.TeacherNoteList.as_view()),
    url(r'^api/v1.0/basic/teacher/note/(?P<pk>[0-9]+)/$', teacher_view.TeacherNoteDetail.as_view()),
    url(r'^api/v1.0/basic/teacher/arrangement/$', teacher_view.TeacherArrangeList.as_view()),
    url(r'^api/v1.0/basic/teacher/arrangement/(?P<pk>[0-9]+)/$', teacher_view.TeacherArrangeDetail.as_view()),
    url(r'^api/v1.0/basic/student/course/$', student_view.StudentCourseList.as_view()),
    url(r'^api/v1.0/basic/student/course/(?P<pk>[0-9]+)/$', student_view.StudentCourseDetail.as_view()),
    url(r'^api/v1.0/basic/student/course/bank/$', student_view.StudentCourseBankList.as_view()),
    url(r'^api/v1.0/basic/student/course/bank/(?P<pk>[0-9]+)/$', student_view.StudentCourseBankDetail.as_view()),
    url(r'^api/v1.0/basic/student/course/signing/$', student_view.StudentCourseSigningList.as_view()),
    url(r'^api/v1.0/basic/student/course/signing/(?P<pk>[0-9]+)/$', student_view.StudentCourseSigningDetail.as_view()),
    url(r'^api/v1.0/basic/student/meals/bank/$', student_view.StudentMealsBankList.as_view()),
    url(r'^api/v1.0/basic/student/meals/bank/(?P<pk>[0-9]+)/$', student_view.StudentMealsBankDetail.as_view()),
    url(r'^api/v1.0/basic/student/note/$', student_view.StudentNoteList.as_view()),
    url(r'^api/v1.0/basic/student/note/(?P<pk>[0-9]+)/$', student_view.StudentNoteDetail.as_view()),
    url(r'^api/v1.0/basic/student/plan/$', student_view.StudentPlanList.as_view()),
    url(r'^api/v1.0/basic/student/plan/(?P<pk>[0-9]+)/$', student_view.StudentPlanDetail.as_view()),
    url(r'^api/v1.0/basic/student/quiz/$', student_view.StudentQuizList.as_view()),
    url(r'^api/v1.0/basic/student/quiz/(?P<pk>[0-9]+)/$', student_view.StudentQuizDetail.as_view()),
    url(r'^api/v1.0/basic/student/$', student_view.StudentList.as_view()),
    url(r'^api/v1.0/basic/student/(?P<pk>[0-9]+)/$', student_view.StudentDetail.as_view()),
    url(r'^api/v1.0/basic/student/sibling/$', student_view.StudentSiblingList.as_view()),
    url(r'^api/v1.0/basic/student/sibling/(?P<pk>[0-9]+)/$', student_view.StudentSiblingDetail.as_view()),
    url(r'^api/v1.0/basic/student/study/bank/$', student_view.StudentStudyBankList.as_view()),
    url(r'^api/v1.0/basic/student/study/bank/(?P<pk>[0-9]+)/$', student_view.StudentStudyBankDetail.as_view()),
    url(r'^api/v1.0/basic/student/study/$', student_view.StudentStudyList.as_view()),
    url(r'^api/v1.0/basic/student/study/(?P<pk>[0-9]+)/$', student_view.StudentStudyDetail.as_view()),
    url(r'^api/v1.0/basic/student/study/signing/$', student_view.StudentStudySigningList.as_view()),
    url(r'^api/v1.0/basic/student/study/signing/(?P<pk>[0-9]+)/$', student_view.StudentStudySigningDetail.as_view()),
    url(r'^api/v1.0/course_student/(?P<course_id>[0-9]+)/$', student_with_course.StudentInCourseList.as_view()),
    url(r'^api/v1.0/course_student/day/(?P<day>[0-9]+)/$', student_with_course.StudentInCoursesDayList.as_view()),
    url(r'^api/v1.0/course_student/all/$', student_with_course.StudentInAllCoursesList.as_view()),
    url(r'^api/v1.0/course_signing/(?P<date>[0-9]+[-][0-9]+[-][0-9]+)/$',
        student_with_course.StudentSigningTableDayList.as_view()),
    url(r'^api/v1.0/course_signing/range/(?P<date_start>[0-9]+[-][0-9]+[-][0-9]+)/(?P<date_end>[0-9]+[-]['
        r'0-9]+[-][0-9]+)/$', student_with_course.StudentSigningTableDayRangeList.as_view()),
    url(r'^api/v1.0/course_signing/create/(?P<date>[0-9]+[-][0-9]+[-][0-9]+)/$',
        student_with_course.StudentCreateCourseSigning.as_view()),
    url(r'^api/v1.0/course_bank/create/(?P<course_id>[0-9]+)/$', student_with_course.StudentCreateSingleCourseBank.as_view()),
    url(r'^api/v1.0/course_bank/create/all/$', student_with_course.StudentCreateAllStudentBank.as_view()),
    url(r'^api/v1.0/study_student/(?P<day>[0-9]+)/$', student_with_study.StudentInOneDayList.as_view()),
    url(r'^api/v1.0/study_student/all', student_with_study.StudentInAllDayList.as_view()),
    url(r'^api/v1.0/study_signing/(?P<date>[0-9]+[-][0-9]+[-][0-9]+)/$', student_with_study.StudentDailySigningList.as_view()),
    url(r'^api/v1.0/study_signing/range/(?P<date_start>[0-9]+[-][0-9]+[-][0-9]+)/(?P<date_end>[0-9]+[-]['
        r'0-9]+[-][0-9]+)/$', student_with_study.StudentRangeSigningList.as_view()),
    url(r'^api/v1.0/study_signing/create/(?P<student_id>[0-9]+)/(?P<date>[0-9]+[-][0-9]+[-][0-9]+)/$',
        student_with_study.CreateStudySigningTable.as_view()),
    url(r'^api/v1.0/study_signing/create/all/(?P<date>[0-9]+[-][0-9]+[-][0-9]+)/$',
        student_with_study.CreateAllStudySigningTable.as_view()),
    url(r'^api/v1.0/study_bank/(?P<student_id>[0-9]+)/$', student_with_study.StudentStudyBankList.as_view()),
    url(r'^api/v1.0/study_bank/all/$', student_with_study.StudentStudyBankAllList.as_view()),
    url(r'^api/v1.0/study_bank/create/all/$', student_with_study.CreateAllStudentStudyBank.as_view()),
    url(r'^api/v1.0/study_manage/(?P<date>[0-9]+[-][0-9]+[-][0-9]+)/$',
        study_view.StudyManageList.as_view()),
    url(r'^api/v1.0/study_manage/signing/expect/(?P<date>[0-9]+[-][0-9]+[-][0-9]+)/$',
        study_view.StudySigningExpectList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
