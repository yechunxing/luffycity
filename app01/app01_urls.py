from django.conf.urls import url,include
from django.contrib import admin
from app01.view import  course,shopcar
urlpatterns = [
    url(r'^course/', course.Course.as_view()),
    url(r'^coursedetail/', course.CourseDetail.as_view()),
    url(r'^degreecourse/', course.DergeeCourseSerializerView.as_view()),
    url(r'^schoolship/', course.ScholarshipSerializerView.as_view()),
    url(r'^courselist/', course.CourseListView.as_view()),
    url(r'^coure/', course.CourseSerializersView.as_view()),
    url(r'^cou/', course.courseview.as_view()),
    url(r'^question/', course.CourseQuestionView.as_view()),
    url(r'^online/', course.CourseOnlineView.as_view()),
    url(r'^chapter/', course.CourseChapterView.as_view()),
    # url(r'^shopcar/(?P<id>\d+)/', shopcar.ShopCarView.as_view({'post':'create'})),
    # 购物车
    url(r'^shopcar/', shopcar.ShopCarView.as_view({'post':'create','get':'list','delete':'destroy','put':'update'})),
]