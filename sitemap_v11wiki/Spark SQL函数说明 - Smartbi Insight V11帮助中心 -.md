
# 1 什么是SparkSQL
Spark SQL是Spark用于结构化数据处理的Spark模块。
SparkSQL的前身是Shark，是一个将Spark和Hive结合的框架，利用hive SQL简化的思想，将RDD进行简化。Shark的出现，是SQL-on-Hadoop的性能比Hive有了10-100倍的提高。
随着Spark的发展，Shark的发展受制于Hive，在此基础上发展出SparkSQL和Hive on Spark，SparkSQL 作为 Spark 生态的一员继续发展，而不再受限于 Hive，只是兼容 Hive。
SparkSQL可以用于简化可伸缩的分布式数据集RDD（Resilient Distributed Dataset）的开发，提高开发效率，且执行效率飞快。
# 2 哪些组件用到了SparkSQL
自助ETL\ETL高级查询中的【派生列】、【过滤】以及【SQL脚本】（即将更名为Spark SQL）组件，支持输入spark SQL函数或语句，完成对数据进行处理或查询的任务。  
---  
数据模型-ETL高级查询 |   
# 3 SparkSQL语法说明
数学和统计运算符、函数 |   
---|---  
逻辑运算符、条件判断函数 |   
数据类型转换函数  
字符串处理函数  
# 4 功能入口
1、【新建模型】并且在模型中增加 【**ETL高级查询】。**
2、进入到 **ETL高级查询：**
  * 先从左侧拖入【Excel文件】，上传本地excel文件，点击**执行该节点** 。示例数据


  * 拖入【读取Excel sheet】节点，再 **执行该节点：**


  * 拖入【列选择】组件，连接组件，再**执行该节点：**


  * 拖入【派生列】，连接组件，再 **执行该节点：**


  * 点击【派生列配置】，进入配置面板，输入相关SparkSQL函数，参考：各**函数说明**

  
