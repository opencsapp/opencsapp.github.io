---
hide:
  - toc
---
# DataPoints&copy;提交

# 如何使用
1. [DataPoints&copy;数据库](datapoints.md)是一个只读的数据表，对应的DataPoints, 申请者信息，项目列表三个表的更改请通过[DataPoints信息收集表](DataPoints收集表.md)，[申请者信息收集表](申请者信息收集表.md)，[添加新项目](添加新项目.md)进行。

# 如何提交

1. 首先在[申请者信息收集表](申请者信息收集表.md)中提交自己的个人信息（仅需一次，不可更改）
3. 然后在[DataPoints信息收集表](DataPoints收集表.md)中提交录取DataPoints，填写过程中可以通过申请者字段链接到自己的账户，并关联以上填写的个人信息。DataPoints支持无限次更改
4. 对于没有在数据库中录入的项目，通过[添加新项目](添加新项目.md)进行添加后，即可在项目字段中找到。

# FAQ

### 我通过申请者信息收集表提交了个人信息，现在想要更改其中某些信息，应当如何操作

请提交一个新的[申请者信息收集表](申请者信息收集表.md)，并在[DataPoints信息收集表](DataPoints收集表.md)中将之前的DataPoints链接到新的个人信息。我们会定期删除这些冗余的用户信息。

### 为什么我无法通过微信扫码登录

这是因为浏览器限制了重定向，请在地址栏右侧允许重定向之后再次尝试。或者也可以先[登录SeaTable](https://cloud.seatable.cn/)之后刷新该页面。

### 403 Forbidden. CSRF verification failed. Request aborted.

这是因为CSRF cookie设置问题，请直接在表格下方找到 在SeaTable中填写 按钮，点击进入填写。

### 为什么我在[DataPoints信息收集表](DataPoints收集表.md)中填写完成之后，没有找到提交按钮

[DataPoints信息收集表](DataPoints收集表.md)自动保存，无需提交

### 为什么我在[DataPoints信息收集表](DataPoints收集表.md)中填写完成之后，没有看到其他用户的记录

您的信息已经实时汇总到了[DataPoints&copy;数据库](datapoints.md)

### 为什么我在[DataPoints&copy;数据库](datapoints.md)中看到的账户都是乱码

因为没有登录，登录后刷新即可看到昵称

### 你们提供的选项没有符合我背景的描述

请打开一个[Issue](https://github.com/csmsapp/csmsapp.github.io/issues)提供你的需求，管理员会帮你处理。

### 我对字段有新的建议，应该如何反馈

请打开一个[Issue](https://github.com/csmsapp/csmsapp.github.io/issues)提供你的反馈，管理员会帮你处理。

### 我因为隐私问题想撤回我的DataPoints。

请在[DataPoints信息收集表](DataPoints收集表.md)中将之前的DataPoints删除即可。

### 我因为隐私问题想撤回我的个人信息。

请打开一个[Issue](https://github.com/csmsapp/csmsapp.github.io/issues)提供你的用户名，管理员会帮你处理。
