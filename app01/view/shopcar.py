from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import  Response
from rest_framework.pagination import  PageNumberPagination
from api import  models
from app01.serializers import shopcar,appo1serializer
from  app01.utils import response
import  redis
import  json
conn = redis.Redis(host='192.168.11.179',port=6379)
user_id = 1
class ShopCarView(ViewSetMixin,APIView):
    def list(self,request,*args,**kwargs):
        """
        购物车get请求
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = response.BaseResponse()
        try:
            user_shop_car = []
            key = 'ycx_shopping_car_%s_*' % (user_id,)
            pattern = conn.keys(key)
            for key in pattern:
                temp = {
                    'id':conn.hget(key,'id').decode('utf-8'),
                    'name':conn.hget(key,'name').decode('utf-8'),
                    'img':conn.hget(key,'course_img').decode('utf-8'),
                    'defulat_price_id':conn.hget(key,'defulat_price_id').decode('utf-8'),
                    'price_dict':json.loads(conn.hget(key,'price_dict').decode('utf-8'))
                }
                user_shop_car.append(temp)

            ret.data = user_shop_car
        except Exception as e:
            ret.code = 3
            ret.error = '获取失败'
        return Response(ret.dict)








    def create(self,request,*args,**kwargs):
       """
       添加到购物车
       :param request:
       :param args:
       :param kwargs:
       :return:
       """
       # 1.先要获取用户选择的课程ID和价格策略ID
       ret = response.BaseResponse()
       course_id = request.data.get('course_id')
       price_id = request.data.get('price_id')
       course_list = models.Course.objects.filter(pk = course_id).first()
       # 2.1 判断选择的课程是否合法
       if not course_list:
           ret.code = 1
           ret.error = '课程不存在'
           return Response(ret.dict)
#      2.2 判断价格策略是不是合法的
       price_list = course_list.price_policy.all()
       price_dict = {}
       for row in price_list:
           temp = {
               'id':row.id,
               'price':row.price,
               'valid_period':row.valid_period,
               'valid_period_display':row.get_valid_period_display()
           }
           price_dict[row.id]= temp
       if  price_id not in price_dict:
           ret.code = 2
           ret.error = '价格不存在'
           return Response(ret.dict)
       # 3.加入购物车(redis)
       # 限制购物车购买的东西
       key = 'ycx_shopping_car_%s_%s' % (user_id, course_id)
       paarent = conn.keys(key)
       if paarent and len(paarent)>=20:
           ret.code = 3
           ret.error = '请将购物车里面的东西付完款在买'
           return Response(ret.dict)
       conn.hset(key,'id',course_id)
       conn.hset(key,'name',course_list.name)
       conn.hset(key,'course_img',course_list.course_img)
       conn.hset(key,'defulat_price_id',price_id)
       conn.hset(key,'price_dict',json.dumps(price_dict))
       # 购物车里面的东西胡子啊一定时间内自动销毁
       conn.expire(key,20*60)
       ret.error = '添加成功'
       return Response(ret.dict)



    def destroy(self,request,*args,**kwargs):
        """
        删除功能
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = response.BaseResponse()
        try:
            course_obj = request.data.get('course_id')
            key = 'ycx_shopping_car_%s_%s' % (user_id, course_obj)
            conn.delete(key)
            ret.data = '删除成功'
        except Exception as e :
            ret.code = 3
            ret.error = '删除失败'
        return Response(ret.dict)



    def update(self,request,*args,**kwargs):
        """
        更新购物车内容
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = response.BaseResponse()
        try:
            course_id = request.data.get('course_id')
            price_id = str(request.data.get('price_id')) if request.data.get('price_id') else None
            # 判断课程iD是否合法
            key =  'ycx_shopping_car_%s_%s' % (user_id, course_id)
            if not conn.exists(key):
                ret.code = 1
                ret.error = '课程不存在'
                return Response(ret.dict)

            price_dict = json.loads(conn.hget(key,'price_dict').decode('utf-8'))
            if price_id not in price_dict:
                ret.code = 1
                ret.error = '价格策略不存在'
                return Response(ret.dict)
            conn.hset(key,'defulat_price_id',price_id)
            conn.expire(key,20*60)
            ret.data = '修改成功'
        except Exception as e:
            ret.code = 1
            ret.error = '修改失败'

        return Response(ret.dict)








