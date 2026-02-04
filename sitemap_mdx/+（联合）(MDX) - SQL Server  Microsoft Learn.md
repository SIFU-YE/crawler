#### 通过
# 联合 - MDX 运算符参考
执行一个集运算以返回两个集的并集并删除重复成员。
```
  
Set_Expression + Set_Expression      

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
一个包含两个指定集的成员的集。
**+ (Union)** 运算符在功能上等效于 Union (MDX)  函数。
下面的示例演示了此运算符的用法。
```
-- This member returns the gross profit margin for each year for North American countries.  
SELECT   
    [Date].[Calendar].[Calendar Year].Members ON 0,  
    {[Sales Territory].[Sales Territory].[Country].[United States]} +  
     {[Sales Territory].[Sales Territory].[Country].[Canada]} ON 1  
FROM  
    [Adventure Works]  
WHERE  
    ([Measures].[Gross Profit Margin])  

```

1月27日 15时 - 1月27日 15时 


