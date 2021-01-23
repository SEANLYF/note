nginx
=====


**安装**


1. wget https://nginx.org/download/nginx-1.19.6.tar.gz
2. tar -zxvf nginx-1.19.6.tar.gz
3. cd nginx-1.19.6
4. ./configure
5. make
6. make install
7. /usr/local/nginx/nginx # 启动


**错误及解决方法**

1、nginx bind() to 0.0.0.0:80 failed

原因：80端口被占用

解决方法：更改端口

/usr/local/nginx/nginx.conf  ---> server  listen: 80 更改即可
