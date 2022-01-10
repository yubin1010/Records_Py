from redis import Redis, exceptions, RedisError
import time,sys,random
from redis.sentinel import (Sentinel, SentinelConnectionPool, ConnectionError, MasterNotFoundError, SlaveNotFoundError)

sentinellist = [('192.168.56.119',26379),('192.168.56.3',26379),('192.168.56.4',26379)]
servicename = 'mymaster'
sentinel=Sentinel(sentinellist, socket_timeout=0.1)
maxIndex= 1000

try:
    master = sentinel.master_for(servicename, socket_timeout=0.1)
    slave = sentinel.slave_for(servicename, socket_timeout=0.1)

except MasterNotFoundError:
    print("Master not found")
    sys.exit()
except SlaveNotFoundError:
    print("Slave not found")
    sys.exit()
except ConnectionError:
    print("Connection Error")
    sys.exit()

startT=time.time()

# print(sentinel.discover_master(servicename))
# print(sentinel.discover_slaves(servicename))

for i in range(1,maxIndex):
    for n in range(1,random.randint(0,5)):
        #hash 형태로 index:1의 형식의 key, random한 값의 filed, value set -> 1000번
        master.hset("index:"+str(i), random.randint(1,300),random.randint(1,5))

# writing 시간 계산
elapsedT = round(time.time() - startT,3)

# reading 시간 계산을 위해 reset
startT = time.time()

# user:i 형식의 값 전부 reading
for i in range(1,maxIndex):
    slave.hgetall("index:"+str(i))

# reading 시간 계산
elapsedT2=round(time.time() - startT,3)

count = 0

# 프린트
for i in range(1,maxIndex):
    data = slave.hgetall("index:"+str(i))
    if len(data)>0:
        count += 1
        print(count, "[index:"+str(i)+"]",data)
    time.sleep(2)

#print("-"*100)
#print("[Writing Time]:",elapsedT, "sec., [Reading Time]: ", elapsedT2,"sec.")