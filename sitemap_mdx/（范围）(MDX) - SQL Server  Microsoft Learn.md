#### 通过
# :（范围）(MDX)
执行一个集运算以返回一个自然排序集，它将两个指定成员作为端点，并将这两个指定成员之间的所有成员作为该集的成员。
```
  
Member_Expression : Member_Expression      

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
包含指定成员以及指定成员之间的所有成员的集。
两个参数所指定的成员必须位于给定维度的同一级别和层次结构中。 如果两个参数指定同一成员，则 **： (Range)** 运算符将返回仅包含指定成员的集。 如果第一个参数为 Null，则该集包含从第二个参数中指定的成员级别开始直到包括该成员的所有成员。 如果第二个参数为 Null，则该集包含从第一个参数中指定的成员开始直到包括同一级别最后一个成员的所有成员。
在 MDX 中没有与此集运算符功能相同的函数。
下面的示例演示了此运算符的用法。
```
-- This query returns the freight cost per user  
-- for products, averaged by month, for the first quarter.  
With Member [Measures].[Freight Per Customer] as  
 (  
     [Measures].[Internet Freight Cost]  
     /   
     [Measures].[Customer Count]  
)  
  
SELECT   
    {[Ship Date].[Calendar].[Month].&[2004]&[1] : [Ship Date].[Calendar].[Month].&[2004]&[3]} ON 0,  
    [Product].[Category].[Category].Members ON 1  
FROM  
    [Adventure Works]  
WHERE  
    ([Measures].[Freight Per Customer])  

```

1月27日 15时 - 1月27日 15时 


