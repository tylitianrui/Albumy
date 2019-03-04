# Albumy   
## 思路基于李辉的项目，代码自己写的。restful
### 启动celery
在项目目录下（即Albumy下）执行  celery -B  -A albumy.celery_worker  worker  就会把beat   celery都启动啦 
##
- 1.本项目采用id进行请求数据，安全性很差。爬虫可根据id递增，进行爬取的数据
- 2.python项目很多互联网产品，一旦获取token后，几乎获取到全部权限，不安全


