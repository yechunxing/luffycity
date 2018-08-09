import  redis
# conn = redis.Redis(host ='192.168.11.61', port = 6379)
#
# conn.set('yechunxing_name','ycx')
#
# # val = conn.get('yechunxing_name')
# val = conn.get('lichuanyun_name').decode('utf-8')
# print(val)
conn =redis.Redis(host='192.168.11.179',port=6379)
conn.set('yechunxing_name','ycx')
val = conn.get('yechunxing_name')
print(val)