from rest_framework import serializers
from api import  models
class ShpoCarSerializer(serializers.ModelSerializer):
    shopcar = serializers.SerializerMethodField()
    # valid_period = serializers.CharField(source='get_valid_period_display')
    def get_shopcar(self,obj):
        ret = []
        obj_list = obj.price_policy.all()
        for row in obj_list:
            ret.append({'price':row.price,'period':row.get_valid_period_display()})
        return ret
    class Meta:
        model = models.Course
        fields = ['shopcar','name']
        # fields = '__all__'
        depth = 1


