#### 通过
#  (MDX) 函数除外
计算两个集并删除第一个集中与第二个集中的元组重复的元组，也可以选择保留重复项。
```
  
Except(Set_Expression1, Set_Expression2 [, ALL ] )  

```

_Set_Expression1_ 返回集的有效多维表达式 (MDX)。
_Set_Expression2_ 返回集的有效多维表达式 (MDX)。
如果指定 **了 ALL** ，该函数将保留在第一个集中找到的重复项;仍会删除在第二个集中找到的重复项。 成员的返回顺序与它们在第一个集中出现的顺序相同。
以下示例说明了此函数的用法。
```
   //This query shows the quantity of orders for all products,  
   //with the exception of Components, which are not  
   //sold.  
SELECT   
   [Date].[Month of Year].Children  ON COLUMNS,  
   Except  
      ([Product].[Product Categories].[All].Children ,  
         {[Product].[Product Categories].[Components]}  
      ) ON ROWS  
FROM  
   [Adventure Works]  
WHERE  
   ([Measures].[Order Quantity])  

```

1月27日 15时 - 1月27日 15时 


