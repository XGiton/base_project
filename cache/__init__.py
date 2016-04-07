# -*- coding: utf-8 -*-
# --- Redis Cache ---
from redis.sentinel import Sentinel
from config import (
    REDIS_NAME,
    REDIS_DB,
    REDIS_PWD,
    REDIS_0_HOST,
    REDIS_0_PORT,
    REDIS_1_HOST,
    REDIS_1_PORT,
)


redis_sentinel = Sentinel(
    [(REDIS_0_HOST, REDIS_0_PORT), (REDIS_1_HOST, REDIS_1_PORT)],
    password=REDIS_PWD,
    db=REDIS_DB
)
r = redis_sentinel.master_for(REDIS_NAME)
