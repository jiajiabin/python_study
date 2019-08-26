import redis

# import time

# 链接redis服务器
r = redis.Redis('192.168.53.180', port='6379', decode_responses=True)
# decode_responses=True

r.set("str1", 'hello world')
ret = r.get("str1")
print(ret)

# r.set("str2", "hellow world2!", ex=5)
r.setex("str2", 3, "hellow world2!")

# time.sleep(5)
ret = r.get("str2")
print(ret)

r.mset({"str3": "good", "str4": "better"})
ret = r.mget("str3", "str4")
print(ret)

r.set("str_01", "0123456789")
ret = r.getrange("str_01", 0, 5)
print(ret)

r.setrange("str_01", 4, "111111111")
ret = r.get("str_01")
print(ret)
print(r.strlen("str_01"))

r.set("num_str", "1")
r.incr("num_str")
print(r.get("num_str"))
r.incr("num_str2", amount=10)
print(r.get("num_str2"))

r.append("str_01", "good")
print(r.get("str_01"))

r.hset("hash_01", "name", "张三")
print(r.hget("hash_01", "name"))
print(r.hgetall("hash_01"))

r.hmset("hash_02", {"name": "李四", "age": 15, "score": "60"})
print(r.hgetall("hash_02"))

r.hdel("hash_02", "age", "scor")
print(r.hgetall("hash_02"))

r.hmset("hash_02", {"name": "李四", "age": 15, "score": "60"})
r.hincrby("hash_02", "age", amount=10)
print(r.hgetall("hash_02"))

print(r.hscan("hash_02", count=100))

i = r.hscan_iter("hash_02")
print(next(i))
print(next(i))
print(next(i))

r.rpush("l1", 1, 2, 3, 4, 5, 6)
print(r.lrange("l1", 0, -1))

r.linsert("l1", "after", 3, "abcd")
r.linsert("l1", "before", 1, "TTT")
print(r.lrange("l1", 0, -1))

r.rpush("l2", 1, 2, 3, 4, 5, 6)
r.ltrim("l2", 0, 4)
print(r.lrange("l2", 0, -1))

r.delete("list3", "list4")
r.rpush("list3", "a", "b", "c", "d")
r.rpush("list4", 1, 2, 3, 4)
while True:
    ret = r.blpop(["list3", "list4"], timeout=0)
    print(ret)
    if r.llen("list3") == 0:
        break

r.delete("set1", "set2")
r.sadd("set1", 1, 2, 3, 4, 5)
r.sadd("set2", "a", "b", "c", "d", "4", "2")
print(r.smembers("set1"), r.smembers("set2"))

print(r.sdiff("set1", "set2"))
print(r.sinter("set1", "set2"))
r.sinterstore("set3", "set1", "set2")
print(r.smembers("set3"))

r.sunionstore("set4", "set1", "set2")
print(r.smembers("set4"))
print(r.sscan("set4", count=3))

print(r.keys("hash*"))

ret = r.sscan("set4",cursor=0, count=2)
print(ret)
ret = r.sscan("set4",cursor=ret[0],count=2)
print(ret)