from redis import Redis, exceptions, RedisError
import time
from redis.sentinel import (Sentinel, SentinelConnectionPool, ConnectionError, MasterNotFoundError, SlaveNotFoundError)

sentinellist = [('192.168.56.119',26379),('192.168.56.3',26379),('192.168.56.4',26379)]
servicename = 'mymaster'
sentinel=Sentinel(sentinellist, socket_timeout=0.1)

master = sentinel.master_for(servicename, socket_timeout=0.1)
slave = sentinel.slave_for(servicename, socket_timeout=0.1)
#master.set('test','1234')

# print(sentinel.discover_master(servicename))
# print(sentinel.discover_slaves(servicename))

for i in range(1,1000):
    print("[slave]",i,slave.get('test'))
    print("[master]",i,master.get('test'))
    time.sleep(2)