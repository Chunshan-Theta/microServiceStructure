
docker build -t nlu_redis_dummy . 



manual process

#docker run -p 6379:6379 -it nlu_srv_veri_mdl -name nlu_srv_veri_mdl  /bin/bash
docker run -p 6379:6379 --name=nluredisdummy -it nlu_redis_dummy   /bin/bash

redis-server /etc/redis/redis.conf --protected-mode no &

cd /app

python simpleServer.py 