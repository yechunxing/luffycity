from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import  Response
from rest_framework.pagination import  PageNumberPagination
from api import  models
from app01.serializers import shopcar,appo1serializer
from  app01.utils import response
class ShopCarView(ViewSetMixin,APIView):
    def list(self,request,*args,**kwargs):
        obj_list = models.Course.objects.all()
        obj = appo1serializer.Course_list(obj_list,many=True)
        return Response(obj.data)
    def create(self,request,*args,**kwargs):
        pk = self.request.data.get('id')
        ret = response.BaseResponse()
        course_obj = models.Course.objects.filter(pk=pk).first()
        price_list = course_obj.price_policy.all()
        res = []
        shopping_car = {1:{'title':None,'price':None}}
        for row in price_list:
            price_obj = row.price
            res.append(price_obj)
            # print(price_obj)
        if  not course_obj:
            ret.code = 1
            ret.error = '加入购物车失败'
            ret.data = course_obj.data
            return Response(ret)
        else:
            if res:
                shopping_car[1]['title'] = course_obj.name
                shopping_car[1]['price'] = res[0]
                return Response(shopping_car)



            # obj = shopcar.ShpoCarSerializer(course_obj)
            # return Response('123')