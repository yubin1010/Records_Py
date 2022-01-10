from rediscluster import RedisCluster
import random, time
startup_nodes = [{"host": "192.168.56.119", "port": "6379"},{"host": "192.168.56.3", "port": "7379"},{"host": "192.168.56.4", "port": "7379"}]

rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

print(rc.get("index1"))

# for i in range(0,3):
#     rc.set("index"+str(i), random.randint(1,300))
#     print(rc.get("index"+str(i)))
#     time.sleep(2)