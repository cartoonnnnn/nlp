sudo apt update
sudo apt install redis-server -y
sudo service redis-server start
redis-cli

SET product:1 '{"Name":"Laptop","Category":"Electronics","Price":900}'
SET product:2 '{"Name":"Phone","Category":"Electronics","Price":700}'
SET product:3 '{"Name":"Shoes","Category":"Fashion","Price":800}'
SET product:4 '{"Name":"Watch","Category":"Accessories","Price":600}'
SET product:5 '{"Name":"Headphones","Category":"Electronics","Price":500}'

SADD category:Electronics product:1 product:2 product:5
SADD category:Fashion product:3
SADD category:Accessories product:4

ZADD price_index 900 product:1
ZADD price_index 700 product:2
ZADD price_index 800 product:3
ZADD price_index 600 product:4
ZADD price_index 500 product:5

GET product:1

SMEMBERS category:Electronics

ZRANGEBYSCORE price_index 500 1000

SET product:1 '{"Name":"Laptop","Category":"Electronics","Price":950}'
ZADD price_index 950 product:1

DEL product:5
SREM category:Electronics product:5
ZREM price_index product:5
