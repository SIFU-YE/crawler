#### 通过
# -（负号）(MDX)
执行一元运算，以返回数值表达式的负值。
```
  
- Numeric_Expression  

```

_Numeric_Expression_ 返回数值的有效多维表达式 (MDX) 表达式。
一个具有指定参数的数据类型的负值。
下面的示例演示了此运算符的用法。
```
-- This member creates a negative version of the  
-- Reseller Freight Cost.  
WITH MEMBER   
   Measures.[Resell Cost as Negative]   
   AS -Measures.[Reseller Freight Cost]  
SELECT   
   [Date].[Calendar Month of Year].Children ON COLUMNS,  
   [Product].[Product Categories].Children ON ROWS  
FROM  
    [Adventure Works]  
WHERE  
    {[Measures].[Resell Cost as Negative]}  

```

1月27日 15时 - 1月27日 15时 


