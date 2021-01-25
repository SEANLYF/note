



# ReadtheDocs 构建项目

## 构建项目

```bash
mkdir <projectname> # 创建项目目录
sphinx-quickstart # 构建项目框架
make html # 在build/html目录下生成html相关文件
sphinx-autobuild source build/html # 直接访问html文件不是很方便，借助该命令启动HTTP服务，默认端口8000，127.0.0.1:8000访问
```



- Makefile: 一个包含指令的文件，在使用make命令时，可以使用这些指令来构建文档输出
- build: 生成的文件的输出目录
- make.bat: windows用命令行
- _static: 静态文件目录，比如图片等
- _templates: 模板目录
- conf.py: 存放sphinx的配置，包括在sphinx-quickstart时选中的配置，也可以自行定义其他值
- index.rst: 文档项目起始文件

### 目录结构

```bash
note/

|----build/
|    |----html/
|    |----doctrees/
|----source/
|    |----conf.py
|    |----index.rst
|    |----_static/
|    |----_templates/
|    |----readthedocs.md
|    |----amazon/
|    |    |----index.rst #
|    |    |----amazon.md # subproject
|----Makefile
|----make.bat
```

### index.rst

```
.. notebook documentation master file, created by
   sphinx-quickstart on Fri Jan 22 17:24:25 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to notebook's documentation!
====================================

.. toctree:: # 声明了一个树状结构
   :maxdepth: 1 # 表示目录的级数
   :caption: Contents: # 用于指定文本标题，可以暂时去掉

   amazon/index
   nginx.md
   readthedocs.md


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

.. +空格开头, 属于多行评论（类似于注释），不会显示到网页上

## 主题优化

```python
# conf.py
import sphinx_rtd_theme
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_theme = 'sphinx_rtd_theme'
```



## 文档托管

```bash
# 创建github仓库
cd <projectname>
touch README.md .gitignore
echo 'build/' >> .gitignore

git init
git add .
git commit -m 'first commit'
git branch -M main
git remote add origin git@github.com:SEANLYF/<projectname>.git
git push -u origin main

# 在readthedocs.org网站上导入项目
```



## Markdown语法编写

```bash
pip install recommonmark # 安装recommonmark插件
```

```python
# 修改conf.py文件
from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']
```



## AutoStructify配置

```python
# conf.py
import recommonmark
from recommonmark.transform import AutoStructify

def setup(app):
    app.add_config_value('recommonmark_config',{
        'url_resolver': lambda url: github_doc_root + url,
        'auto_toc_tree_section': 'Contents',
    }, True)
    app.add_transform(AutoStructify)
```



## Adding CSS or JavaScript

```python
# conf.py
# these paths are either relative to html_static_path or fully qualified paths
html_css_files = ['css/custom.css',]
html_js_files = ['js/custom.js',]

```



## Overriding or replacing a theme's stylesheet

```python
# conf.py
# if your replacement stylesheet exists at _static/css/yourtheme.css
html_style = 'css/yourtheme.css'
```

## Cross-referencing with Sphinx

```

```

