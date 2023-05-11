import redis
import time

r = redis.Redis(host='localhost', port=6379)

# r.set("France", "Paris")
# r.set("Germany", "Berlin")

# france_capital = r.get("France")
# germany_capital = r.get("Germany")

# print(france_capital)
# print(germany_capital)

#alternatively you can do a multiple set.

r.mset({"Germany": "Berlin", "France": "Paris"})

print(r.get ("Germany"))
print(r.get ("France"))

if (r.exists("Germany")):
    print(r.get("Germany"))
else:
    print("Cannot find the capital. Get from API")

r.psetex("Serbia", 1000, "Belgrade")

print(r.get("Serbia"))

time.sleep(2)

print(r.get("Serbia"))
