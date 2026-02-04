#### 通过
#  <= （小于或等于） （MDX）
执行比较作，确定一个多维表达式（MDX）表达式的值是否小于或等于另一个 MDX 表达式的值。
```
  
MDX_Expression <= MDX_Expression  

```

_MDX_Expression_ 有效的 MDX 表达式。
基于以下条件的布尔值：
  * 如果两个参数均为非 null，并且第一个参数的值都小于或等于第二个参数的值，则为 **true** 。
  * 如果两个参数均为非 null，并且第一个参数的值大于第二个参数的值，则为 **false** 。
  * 如果任一参数或两个参数的计算结果均为 null 值，则为 null。


下面的示例演示如何使用此运算符。
```
-- This query returns the gross profit margin (GPM)  
-- for Australia where the GPM is less than or equal to 30%.  
With Member [Measures].[LowGPM] as  
  IIF(  
      [Measures].[Gross Profit Margin] <= .5,  
      [Measures].[Gross Profit Margin],  
      null)  
SELECT   
NON EMPTY [Sales Territory].[Sales Territory Country].[Australia] ON 0,  
    NON EMPTY [Product].[Category].Members ON 1  
FROM  
    [Adventure Works]  
WHERE  
    ([Measures].[LowGPM])  

```

1月27日 15时 - 1月27日 15时 


