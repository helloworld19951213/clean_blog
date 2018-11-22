# Clean Blog
---

###  > `FIX`

+ ###### 修改xadmin导入方式(本地包导入)
+ ###### static 引用方式(详见 setting)

### > `Add`

+ ###### 富文本框输入 改为 MarkDown文本输入 
+ ###### 项目部署uwsgi、nginx静态资源代理

### > `BUG`

+ <s>###### `代码高亮`</s>
+ ###### 可能客户端 archive界面 显示不了那个月的文章，是因为mysql时区的设置问题 可以在 cmd 中
+ ######    cmd 输入 mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql -uroot mysql -p 输入密码就可以了
   - ###### 详见[Heading link](https://chowyi.com/Django%E4%BD%BF%E7%94%A8MySQL%E5%90%8E%E7%AB%AF%E6%97%A5%E6%9C%9F%E4%B8%8D%E8%83%BD%E6%8C%89%E6%9C%88%E8%BF%87%E6%BB%A4%E7%9A%84%E9%97%AE%E9%A2%98%E5%8F%8A%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88/ "Heading link")
   
### > `Attaction`

+ ###### 如果本地跑记得把DEBUG 改为TRUE
+ ###### uwsgi 配置文件是那个ini后缀的文件 其他是一些uwsgi产生的文件
+ ###### nginx 配置文件也在uwsgi_cnf里面 直接在 nginx 原配置文件下(/etc/nginx/nginx.conf)的http{}中加入 include nginx_blog.conf 就可以了
---

一个基于Django开发的博客系统:

- Python3.6 和 Django1.10
- MySQL储存方案
- xadmin后台管理
- <s>ckeditor编辑器，图片上传</s>改为 markdown文本 支持富文本的所有输入
- Bootstrap前端模板
- RSS订阅
- 标签分类与日期归档
- 文章评论
- haystack文章内容搜索

Usage:

- 新建虚拟环境

<pre>
git clone https://github.com/helloworld19951213/clean_blog.git
virtualenv --python=<py3path> venv
. venv/bin/activate
pip install -r requirements.txt

</pre>

- 收集静态资源

<pre>
python manage.py collectstatic
</pre>

- 数据库迁移

<pre>
python manage.py makemigrations
python manage.py migrate
mysql 执行migrate时，可能会出现编码错误，可以在创建数据库时指定编码： create database myblog character set utf8mb4;
</pre>

- 创建管理员
<pre>
python manage.py createsuperuser
</pre>

------
### 首页

![index](/pic/2.png)

### 详情页

![index](/pic/3.png)

### 评论发表

![index](/pic/8.png)

### 归档

![index](/pic/7.png)

### xadmin后台

![index](/pic/5.png)

### Editor.md[文章编辑器](https://pandao.github.io/editor.md/)

![index](/pic/1.png)


