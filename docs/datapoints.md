---
hide:
  - navigation
  - toc
---

# CS Masters Application DataPoints&copy;

??? note "请先阅读使用指南"
       1. DataPoints&copy;是host在SeaTable上的数据库，支持方便的过滤，排序，和分组，上手难度低。支持Python SDK，SQL Query等高阶操作，有需要的用户可通过[用户手册](https://seatable.cn/help/)和[Bilibili教程](https://space.bilibili.com/1305719772?spm_id_from=333.337.search-card.all.click)学习。
       2. 该数据库共分为四个子表，分别为DataPoints, Progress，申请者信息，项目列表。申请者信息表每条记录对应一个SeaTable Account，记录了申请者的详细背景；项目列表每条记录对应一个项目；DataPoints每条记录链接到一个申请者和一个项目，使得用户可以方便地按照用户或项目浏览或检索；Progress与Datapoints类似，用于汇总各校进展（Tips：双击申请者和项目字段单元格可以打开链接内容；鼠标悬浮在行号上可以点击查看该条记录）
       3. 该数据库遵循[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/)， 公益开源，期待用户根据[DataPoints&copy;提交](submit.md)中的指引提交你的申请结果，帮助到更多的申请者！（Tips：希望匿名的用户可以提交前先到[SeaTable Profile](https://cloud.seatable.cn/profile/)修改头像和昵称）
       4. 可以通过视图对数据进行分析查看，点击左上角下拉菜单，可以选择预设视图。用户也可以自行添加视图进行数据浏览。
       5. 鼠标悬浮在列头上的i符号，可以查看该字段的详细说明
       6. 点击右上角插件，可以体验高级统计统计，时间线，高级查询功能。其中高级统计功能预设了几组可视化图表

<iframe className="dtable-embed" src="https://cloud.seatable.cn/dtable/external-links/ff48695db50e48358d5b/" frameBorder="0" width="100%" height="960" allowfullscreen="true" style="background: transparent; border: 1px solid #ccc;"></iframe>

<script>
   let BtnEle = document.querySelector(".md-button");
   let frameEle = document.querySelector(".frame");
   BtnEle.addEventListener("click", () => {
      frameEle.className = "fullScreen";
   });
</script>

[:fontawesome-solid-square-poll-horizontal: 提交新 DataPoints](submit.md){ .md-button .md-button--primary }    [:fontawesome-solid-pen-to-square: 在 SeaTable 中浏览](https://cloud.seatable.cn/dtable/external-links/ff48695db50e48358d5b/){ .md-button}
