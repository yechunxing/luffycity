from rest_framework import serializers
from rest_framework.validators import ValidationError
from api import  models


# class CourseSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()


class Course_list(serializers.ModelSerializer):
    level_name = serializers.CharField(source='get_level_display')
    hours = serializers.CharField(source='coursedetail.hours')
    course_slogan = serializers.CharField(source='coursedetail.course_slogan')
    # recommend_courses = serializers.CharField(source='coursedetail.recommend_courses.all')

    recommend_courses = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = ['id','name','level_name','hours','course_slogan','recommend_courses']

    def get_recommend_courses(self,row):
        recommend_list = row.coursedetail.recommend_courses.all()
        return [ {'id':item.id,'name':item.name} for item in recommend_list]
















# 课程列表
# class Course_list(serializers.ModelSerializer):
#     class Meta:
#         model = models.DegreeCourse
#         fields = '__all__'








# 课程详情
class CourseDetail(serializers.ModelSerializer):
    class Meta:
        model = models.CourseDetail
        fields = '__all__'



# a.查看所有学位课并打印学位课名称以及授课老师

class DergeeCourseSerializer(serializers.ModelSerializer):
    teacher_list = serializers.SerializerMethodField()
    def get_teacher_list(self,obj):
        obj_list =  obj.teachers.all()
        ret = []
        for row in obj_list:
            ret.append({'name':row.name})
        return ret
    class Meta:
        model = models.DegreeCourse
        fields = ['name','teacher_list']
        # fields = '__all__'
        depth = 1

# 查看所有学位课并打印学位课名称以及学位课的奖学金
class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DegreeCourse
        fields = ['name','total_scholarship']
        # fields = '__all__'
        depth = 1


# c. 展示所有的专题课
class CoureseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['degree_course']
        depth = 1


# d. 查看id=1的学位课对应的所有模块名称

class CourseSerializers(serializers.ModelSerializer):
    cour = serializers.CharField(source='degree_course')
    # coure_list = serializers.SerializerMethodField()
    # def get_coure_list(self,obj):
    #     ret = []
    #     obj_list =  obj.course.all()
    #     for row in obj_list:
    #         ret.append({'name':row.name})
    #     return ret
    class Meta:
        model = models.Course
        fields = ['cour']
        depth = 1
# e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses

class course(serializers.ModelSerializer):
    level = serializers.CharField(source='get_level_display')
    a = serializers.CharField(source='coursedetail.why_study')
    b = serializers.CharField(source='coursedetail.what_to_study_brief')
    c = serializers.SerializerMethodField()
    def get_c(self,obj):
        obj_list = obj.coursedetail.recommend_courses.all()
        ret = []
        for row in obj_list:
            ret.append({'name':row.name})
        return ret
    class Meta:
        model = models.Course
        fields = ['level','name','a','b','c']
        depth = 1

# f.获取id = 1的专题课，并打印该课程相关的所有常见问题

class CourseQuestion(serializers.ModelSerializer):
    question_list = serializers.SerializerMethodField()
    def get_question_list(self,obj):
        obj_list = obj.asked_question.all()
        ret = []
        for row in obj_list:
            ret.append({'question':row.question,'answer':row.answer})
        return ret
    class Meta:
        model = models.Course
        fields = ['question_list']
        depth = 3

 # g.获取id = 1的专题课，并打印该课程相关的课程大纲
class CourseOnline(serializers.ModelSerializer):
    online_list = serializers.SerializerMethodField()

    def get_online_list(self,obj):
        obj_list = obj.coursedetail.courseoutline_set.all()
        ret = []
        for row in obj_list:
            ret.append({'title':row.title})
        return ret
    class Meta:
        model = models.Course
        fields = ['online_list']
        depth = 1


#  h.获取id = 1的专题课，并打印该课程相关的所有章节

class CourseChapter(serializers.ModelSerializer):
    chapter_list = serializers.SerializerMethodField()
    def get_chapter_list(self,obj):
        ret = []
        obj_list = obj.coursechapters.all()
        for row in obj_list:
            ret.append({'name':row.summary})
        return ret

    class Meta:
        model = models.Course
        fields = ['chapter_list']
        depth = 1