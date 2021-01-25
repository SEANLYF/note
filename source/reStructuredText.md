reStructuredText
================
## Structure

```
This is a paragraph. It's quite
short.
# 此处为空行
    This paragraph will result in an indented block of
    text, typically used for quoting other text.
# 此处为空行
This is another one.

======Result=====
This is a paragraph. It's quite short.

    This paragraph will result in an indented block of text, typically used for quoting other text.

This is another one.
```

## Text styles

```
*a* # italics
**a** # bold
```

## Lists

```
1. numbers
A. numbers
1) numbers
(1) numbers # 1. numbers
 1. numbers

- numbers
+ numbers
* numbers
  * numbers
    * numbers
    
what
 Definition
 
*what*
 Definition
```

## Performatting

```
An example::
 Definition
```

## Sections

```
# 标题从大到小
==============
document title
==============
```



## Images

```
# 图片位置：source/_static/test.png
.. image:: images/biohazard.png
   :height: 100
   :width: 200
   :scale: 50
   :alt: alternate text
```

