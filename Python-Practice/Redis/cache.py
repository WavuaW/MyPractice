import redis

r = redis.Redis(host='localhost', port=6379)

r.set("France", "Paris")
r.set("Germany", "Berlin")

france_capital = r.get("France")
germany_capital = r.get("Germany")

print(france_capital)
print(germany_capital)

