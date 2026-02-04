#### 通过
#  (MDX) 运算符除外
执行一个集运算，以返回两个集之间的不同项并删除重复成员。
```
  
Set_Expression - Set_Expression  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
**- (Except)** 运算符在功能上等效于 Except 函数。
以下示例演示此运算符的用法：
```
// This query shows the quantity of orders for all product categories  
// with the exception of Components.  
SELECT   
   [Measures].[Order Quantity] ON COLUMNS,  
   [Product].[Product Categories].[All].Children   
   - [Product].[Product Categories].[Components] ON ROWS  
FROM  
    [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


