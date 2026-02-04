
## 应用说明
基于mondrian的多维数据源所创建的cube。实现参数排序，对时间参数备选值倒序排列，通过书写MDX实现参见切片参数备选值设置。
下面以Cube 【Sales】为例，演示通过书写MDX实现参见切片参数备选值设置。
## 操作步骤
1、新建多维分析。选择Cube 【Sales】构建多维分析。
2、把“时间”维度拖放到【切片区】。
3、在右边栏的 【参数】下找到“时间”多维参数，并双击打开进行书写MDX。
在其MDX表达式中输入如下：
`select` `order``( {[时间].[月].ALLMEMBERS},[时间].currentmember.``name``,``desc``) } ``on` `columns,{} ``on` `rows` `from` `[Sales]`  
---  
具体设置如下图：
4、预览效果如下图：  
