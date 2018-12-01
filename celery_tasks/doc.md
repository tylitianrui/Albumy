# celery原生用法
# 此为最基本的用法
### 依赖
pip install celery[redis,msgpack]
####启动 进入Albumy目录中，即celery_tasks所在的目录中。执行celery -A celery_tasks worker -l info

###异常情况

在启动都没问题，但是在接受任务时会 报错：CRITICAL/MainProcess] Unrecoverable error: AttributeError  AttributeError: 'float' object has no attribute 'items'
这类的错误  
解决方案 pip install redis==2.10.6  不要使用redis 3版本的

