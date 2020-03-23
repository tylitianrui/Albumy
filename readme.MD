# Albumy   
图片社交项目-后端python

## 1.开发环境
macos + vacode + python3.6 


## 2.技术说明
### 1.虚拟环境
python版本: python 3.7
#### 1. **安装virtualenv**
此项目安装依赖都在虚拟环境之中，对外封闭。  
```
pip3 install virtualenv
````
或者使用国内源 
```
pip3 install virtualenv  -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

#### 2.创建虚拟环境
在项目目录下,执行：  
```
virtualenv -p $(which  python3) venv
```
#### 3.激活虚拟环境

```
source venv/bin/activate
```
退出虚拟环境
```
deactivate
```

#### 3. 依赖管理
导出依赖
```
pip freeze > requirements.txt
```
安装依赖
```
pip install -r requirements.txt
```
注：
- txt格式是为了照顾使用win进行开发的伙伴
- 安装依赖包可以使用国内源，例如: `pip install flask  -i https://mirrors.aliyun.com/pypi/simple` 或者 `pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple`

## 3. 文档
[文档](./docs/catalog.md)
