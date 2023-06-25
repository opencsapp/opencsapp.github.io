---
hide:
  - toc
---

# DataPoints&copy;提交

[:fontawesome-solid-square-poll-horizontal: DataPoints 收集表](newdatapoints.md){ .md-button } [:fontawesome-solid-square-poll-horizontal: Progress 收集表](newprogress.md){ .md-button } [:fontawesome-solid-square-poll-horizontal: Visa 收集表](newvisa.md){ .md-button } [:fontawesome-solid-square-poll-horizontal: 申请者信息收集表](newapplicant.md){ .md-button } [:fontawesome-solid-square-poll-horizontal: 添加新项目](newprogram.md){ .md-button }

[:fontawesome-solid-database: 访问 DataPoints&copy;数据库](datapoints.md){ .md-button .md-button--primary }

# 如何提交

1. [DataPoints&copy;数据库](datapoints.md)是一个只读的数据表，对应的 DataPoints，Progress，Visa, 申请者信息，项目列表五个子表的更改请通过[DataPoints 收集表](newdatapoints.md)，[Progress 收集表](newprogress.md)，[Visa 收集表](newvisa.md), [申请者信息收集表](newapplicant.md)，[添加新项目](newprogram.md)进行。
2. 首先在[申请者信息收集表](newapplicant.md)中提交自己的个人信息（仅需一次，不可更改）
3. 然后在[DataPoints 收集表](newdatapoints.md)中提交录取 DataPoints，填写过程中可以通过申请者字段链接到自己的账户，并关联以上填写的个人信息。DataPoints 支持无限次更改
4. 进展的提交可以在[Progress 收集表](newprogress.md)中进行，操作与 DataPoints 相同
5. Visa的提交可以在[Visa 收集表](newvisa.md)中进行，操作与 DataPoints 相同，可以多次更新签证状态
6. 对于没有在数据库中录入的项目，通过[添加新项目](newprogram.md)进行添加后，即可在项目字段中找到。

# FAQ

### 如何保证我提交的datapoints会开源而非被owner用于收费访问获利？

[DataPoints&copy;数据库](datapoints.md)是完全开源的，任何用户均可点击右上角导出全部数据，这保证DataPoints&copy;中的信息不会被私人垄断。我们欢迎任何个人或团体在[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/)条款下分享或构建材料，只需遵守条款的Attribution, NonCommercial, ShareAlike规则即可。

### [DataPoints&copy;数据库](datapoints.md)中储存的信息安全吗，是否会因为误操作丢失或因为恶意添加记录而崩溃？

[DataPoints&copy;数据库](datapoints.md)会自动保存历史镜像确保信息安全

### 我通过申请者信息收集表提交了个人信息，现在想要更改其中某些信息，应当如何操作

请提交一个新的[申请者信息收集表](newapplicant.md)，并在[DataPoints 收集表](newdatapoints.md)中将之前的 DataPoints 链接到新的个人信息。我们会定期删除这些冗余的用户信息。

### 为什么我无法通过微信扫码登录

这是因为浏览器限制了重定向，请在地址栏右侧允许重定向之后再次尝试。或者也可以先[登录 SeaTable](https://cloud.seatable.cn/)之后刷新该页面。

### 403 Forbidden. CSRF verification failed. Request aborted.

这是因为 CSRF cookie 设置问题，请直接在表格下方找到 在 SeaTable 中填写 按钮，点击进入填写。

### 每条记录太长了，左右滑动很麻烦

在该行最左侧序号处悬浮，可以找到缩放按钮，点击即可在标签页中浏览该条记录

### 为什么我在[DataPoints 收集表](newdatapoints.md)中填写完成之后，没有找到提交按钮

[DataPoints 收集表](newdatapoints.md)自动保存，无需提交

### 为什么我在[DataPoints 收集表](newdatapoints.md)中填写完成之后，没有看到其他用户的记录

您的信息已经实时汇总到了[DataPoints&copy;数据库](datapoints.md)

### 为什么我在[DataPoints&copy;数据库](datapoints.md)中看到的账户都是乱码

因为没有登录，登录后刷新即可看到昵称

### 为什么三个子表中的 ID 都不连续，中间的记录是被隐藏了吗

中间的记录因为各种原因被删除了，包括但不限于测试使用/隐私原因删除

### 单选提供的选项没有符合我背景的描述

请打开一个[Issue](https://github.com/opencsapp/opencsapp.github.io/issues)提供你的需求，管理员会帮你处理。

### 我对字段有新的建议，应该如何反馈

请打开一个[Issue](https://github.com/opencsapp/opencsapp.github.io/issues)提供你的反馈，管理员会帮你处理。

### 我因为隐私问题想撤回我的 DataPoints。

请在[DataPoints 收集表](newdatapoints.md)中将之前的 DataPoints 删除即可。

### 我因为隐私问题想撤回我的个人信息。

请打开一个[Issue](https://github.com/opencsapp/opencsapp.github.io/issues)提供你的用户名，管理员会帮你处理。
