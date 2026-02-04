#### 通过
#  < (小于) (MDX) 
执行比较运算，以确定一个多维表达式 (MDX) 的值是否小于另一个 MDX 表达式的值。
```
  
MDX_Expression < MDX_Expression  

```

_MDX_Expression_ 有效的 MDX 表达式。
布尔值，具体情形如下：
  * 如果两个参数均为非 null，并且第一个参数的值小于第二个参数的值，则为 **true** 。
  * 如果两个参数均为非 null，并且第一个参数的值等于或大于第二个参数的值，则为 **false** 。
  * 如果两个参数或其中任何一个参数计算出来的值为空值，则为 Null。


下面的示例演示了此运算符的用法。
```
-- This query returns the gross profit margin (GPM)  
-- for clothing sales where the GPM is less than 30%.  
With Member [Measures].[LowGPM] as  
  IIF(  
      [Measures].[Gross Profit Margin] < .3,  
      [Measures].[Gross Profit Margin],  
      null)  
SELECT NON EMPTY  
    [Sales Territory].[Sales Territory Country].Members ON 0,  
    [Product].[Category].[Clothing] ON 1  
FROM  
    [Adventure Works]  
WHERE  
    ([Measures].[LowGPM])  

```

1月27日 15时 - 1月27日 15时 


