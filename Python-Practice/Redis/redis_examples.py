import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

mfd = redis_client.get('msft_fundamental_data')

print(mfd)