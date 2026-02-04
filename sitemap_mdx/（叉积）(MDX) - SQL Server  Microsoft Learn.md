#### 通过
# 交叉联接 - MDX 运算符参考
执行一个集运算以返回两个集的叉积。
```
  
Set_Expression * Set_Expression  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
一个包含两个指定参数的叉积的集。
*** (Crossjoin)** 运算符在功能上等效于 Crossjoin 函数。
下面的示例演示了此运算符的用法。
```
-- This query returns the gross profit margin for product types  
-- and reseller types crossjoined by year.  
SELECT   
    [Date].[Calendar].[Calendar Year].Members *  
    [Reseller].[Reseller Type].Children ON 0,  
    [Product].[Category].[Category].Members ON 1  
FROM  
    [Adventure Works]  
WHERE  
    ([Measures].[Gross Profit Margin])  

```

1月27日 15时 - 1月27日 15时 


