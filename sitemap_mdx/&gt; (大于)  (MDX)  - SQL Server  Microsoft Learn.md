#### 通过
#  > (大于) (MDX) 
执行比较运算，以确定一个多维表达式 (MDX) 的值是否大于另一个 MDX 表达式的值。
```
  
MDX_Expression > MDX_Expression  

```

_MDX_Expression_ 有效的 MDX 表达式。
布尔值，具体情形如下：
  * 如果两个参数均为非 null，并且第一个参数的值大于第二个参数的值，则**为 true** 。
  * 如果两个参数均为非 null，并且第一个参数的值等于或小于第二个参数的值，则**为 false** 。
  * 如果两个参数或其中任何一个参数计算出来的值为空值，则为 Null。


以下示例查询演示了此运算符的用法。
```
-- This query returns the gross profit margin (GPM)  
-- for Australia where the GPM is more than 50%.  
With Member [Measures].[HighGPM] as  
  IIF(  
      [Measures].[Gross Profit Margin] > .5,  
      [Measures].[Gross Profit Margin],  
      null)  
SELECT   
NON EMPTY [Sales Territory].[Sales Territory Country].[Australia] ON 0,  
    NON EMPTY [Product].[Category].Members ON 1  
FROM  
    [Adventure Works]  
WHERE  
    ([Measures].[HighGPM])  
  

```

1月27日 15时 - 1月27日 15时 


