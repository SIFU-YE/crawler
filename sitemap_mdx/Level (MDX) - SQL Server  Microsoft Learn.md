#### 通过
# Level (MDX)
返回成员的级别。
```
  
Member_Expression.Level  

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX) 。
以下示例使用 **Level** 函数返回 Adventure Works 多维数据集中的所有月份。
```
SELECT[Date].[Fiscal].[Month].[February 2002].Level.Members ON 0,  
[Measures].[Internet Sales Amount] ON 1  
FROM [Adventure Works]  

```

以下示例使用 **Level** 函数返回 Adventure Works 多维数据集中 Model Name 属性层次结构中All-Purpose Bike Stand 的级别名称。
```
WITH MEMBER Measures.x AS   
   [Product].[Model Name].[All-Purpose Bike Stand].Level.Name  
SELECT Measures.x ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


