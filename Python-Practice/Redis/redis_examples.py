import redis
import json

redis_client = redis.Redis(host='localhost', port=6379, db=0)

mfd = redis_client.get('msft_fundamental_data')

print(mfd)

redis_client.set('microsoft_fundamental_data', json.dumps({"pe": 33}))