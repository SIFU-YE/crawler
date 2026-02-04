#### 通过
# Predict (MDX)
此函数由于内部不一致而正被删除。
有关使用 DMX 表达式的解决方法，请查看示例部分。
返回用数值表达式对数据挖掘模型求得的值。
```
  
Predict(Mining_Model_Name,String_Expression)   

```

_Mining_Model_Name_ 表示挖掘模型名称的有效字符串表达式。
_String_Expression_ 计算结果为指定挖掘模型的有效 DMX 表达式的有效字符串表达式。
**Predict** 函数在指定挖掘模型的上下文中计算指定的字符串表达式。
在数据挖掘表达式 (DMX) 参考中提供了数据挖掘语法和函数。
下面的示例使用 Customer Clusters 挖掘模型预测群集的名称以及与特定客户的距离：
```
WITH MEMBER MEASURES.CLNAME AS   
PREDICT("Customer Clusters", "Cluster()")  
MEMBER MEASURES.CLDISTANCE AS   
PREDICT("Customer Clusters", "ClusterDistance(Cluster())")  
SELECT {MEASURES.CLNAME, MEASURES.CLDISTANCE} ON 0   
FROM [Adventure Works]  
WHERE([Customer].[Customer Geography].[Customer].&[12012])  

```

1月27日 15时 - 1月27日 15时 


