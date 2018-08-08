from django.shortcuts import render,HttpResponse
from api import models
# Create your views here.

def index(request):
        #     a.查看所有学位课并打印学位课名称以及授课老师
        # obj = models.DegreeCourse.objects.all()
        # obj1 = models.DegreeCourse.objects.filter(name='Python').values_list('teachers__name')
        # obj2 = models.DegreeCourse.objects.filter(name='JavaScript').values_list('teachers__name')
        # print(obj)
        # print(obj1)
        # print(obj2)

        #     b.查看所有学位课并打印学位课名称以及学位课的奖学金
        # obj1 = models.DegreeCourse.objects.filter(name='Python').values_list('total_scholarship')
        # obj2 = models.DegreeCourse.objects.filter(name='JavaScript').values_list('total_scholarship')
        # print(obj1)
        # print(obj2)
        #
        #     c.展示所有的专题课
        # obj = models.Course.objects.filter(degree_course__isnull=True)
        # print(obj)

        #
        #
        # d.查看id = 1
        # 的学位课对应的所有模块名称
        # obj = models.DegreeCourse.objects.filter(id=1).values_list('course__name')
        # print(obj)

        # e.获取id = 1
        # 的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
        # obj = models.CourseDetail.objects.filter(course__id =1).values('why_study','what_to_study_brief','recommend_courses__name','course__level')
        #
        #
        # print(obj)

        # f.获取id = 1
        # 的专题课，并打印该课程相关的所有常见问题
        # obj = models.OftenAskedQuestion.objects.filter(object_id=1,content_type__model='course')
        # print(obj)
        # g.获取id = 1
        # 的专题课，并打印该课程相关的课程大纲
        # obj = models.CourseOutline.objects.filter(course_detail__course__id=1).values_list('content')
        # print(obj)
        # h.获取id = 1
        # 的专题课，并打印该课程相关的所有章节
        # obj = models.CourseChapter.objects.filter(course__id=1).values_list('summary')
        # print(obj)
        # i.获取id = 1
        # 的专题课，并打印该课程相关的所有课时
        # 第1章·Python
        # 介绍、基础语法、流程控制
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # 第1章·Python
        # 介绍、基础语法、流程控制
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）

        # obj = models.CourseSection.objects.filter(chapter__course__id=1).values_list('order')
        # print(obj)
        # i.获取id = 1
        # 的专题课，并打印该课程相关的所有的价格策略
        # obj = models.PricePolicy.objects.filter(object_id=1, content_type__model='course')
        # print(obj)
        return HttpResponse('ok')