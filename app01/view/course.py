from api import  models
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from app01.serializers import appo1serializer
from app01.utils.response import BaseResponse
from rest_framework.pagination import PageNumberPagination
class Course(APIView):
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            course_list = models.DegreeCourse.objects.all()
            # 分页
            p = PageNumberPagination()
            page_list = p.paginate_queryset(course_list,request,self,)
            obj = appo1serializer.Course_list(instance=course_list, many=True)
            ret.data = obj.data
        except Exception as e:
            ret.code = 1
            ret.error = '获取数据失败'
        return Response(ret.dict)
class CourseDetail(APIView):
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            course_detail_list = models.CourseDetail.objects.all()
            p = PageNumberPagination()
            page_list = p.paginate_queryset(course_detail_list,request,self)
            obj = appo1serializer.CourseDetail(course_detail_list, many=True)
            ret.data = obj.data
        except Exception as e:
            ret.code = 1
            ret.error = '获取数据失败'
        return Response(ret.dict)



# a.查看所有学位课并打印学位课名称以及授课老师

class DergeeCourseSerializerView(APIView):
    def get(self,request,*args,**kwargs):
        res = {'code':0}
        DegreeCourse_list = models.DegreeCourse.objects.all()
        obj = appo1serializer.DergeeCourseSerializer(DegreeCourse_list,many=True)
        res['data'] = obj.data
        return Response(res)
# 查看所有学位课并打印学位课名称以及学位课的奖学金

class ScholarshipSerializerView(APIView):
    def get(self,request,*args,**kwargs):
        res = {'code':0}
        Schoolship_list = models.DegreeCourse.objects.all()
        obj = appo1serializer.ScholarshipSerializer(Schoolship_list,many=True)
        res['data'] = obj.data
        return Response(res)

# c. 展示所有的专题课
class CourseListView(APIView):
    def get(self, request, *args, **kwargs):
        res = {'code': 0}
        course_list = models.Course.objects.all()
        obj = appo1serializer.CoureseListSerializer(course_list, many=True)
        res['data'] = obj.data
        return Response(res)

# d. 查看id=1的学位课对应的所有模块名称


class CourseSerializersView(APIView):
    def get(self, request, *args, **kwargs):
        res = {'code': 0}
        course_list = models.Course.objects.filter(id=1)
        obj = appo1serializer.CourseSerializers(course_list, many=True)
        res['data'] = obj.data
        return Response(res)


#  e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses

class courseview(APIView):
    def get(self, request, *args, **kwargs):
        res = {'code': 0}
        course_list = models.Course.objects.filter(id=1)
        obj = appo1serializer.course(course_list, many=True)
        res['data'] = obj.data
        return Response(res)


# f.获取id = 1的专题课，并打印该课程相关的所有常见问题

class CourseQuestionView(APIView):
    def get(self, request, *args, **kwargs):
        res = {'code': 0}
        course_list = models.Course.objects.filter(id=1)
        obj = appo1serializer.CourseQuestion(course_list, many=True)
        res['data'] = obj.data
        return Response(res)

 # g.获取id = 1的专题课，并打印该课程相关的课程大纲

class CourseOnlineView(APIView):
    def get(self, request, *args, **kwargs):
         res = {'code': 0}
         course_list = models.Course.objects.filter(id=1)
         obj = appo1serializer.CourseOnline(course_list, many=True)
         res['data'] = obj.data
         return Response(res)

#  h.获取id = 1的专题课，并打印该课程相关的所有章节

class CourseChapterView(APIView):
    def get(self, request, *args, **kwargs):
        res = {'code': 0}
        course_list = models.Course.objects.filter(id=1)
        obj = appo1serializer.CourseChapter(course_list, many=True)
        res['data'] = obj.data
        return Response(res)