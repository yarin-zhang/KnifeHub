# KnifeBox 刀盒

KnifeBox 取自“瑞士军刀”（Swiss Army Knife）的意思，KnifeBox 允许你收纳你的小工具，可以自由集成可用的 Python 代码的工具库，能够将自己所需的 Python 代码片段整合到一个地方，并允许通过 API 请求调用。


## 开发运行

```
uvicorn main:app --host 0.0.0.0 --port 9080 --reload
```

## 生产运行

```
docker build -t myapp .
docker run -p 80:80 myapp
```