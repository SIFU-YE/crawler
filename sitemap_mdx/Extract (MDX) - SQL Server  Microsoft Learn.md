#### 通过
# Extract (MDX)
返回由提取的层次结构元素中的元组构成的集。
```
  
Extract(Set_Expression, Hierarchy_Expression1 [,Hierarchy_Expression2, ...n] )  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Hierarchy_Expression1_ 返回层次结构的有效多维表达式 (MDX)。
_Hierarchy_Expression2_ 返回层次结构的有效多维表达式 (MDX)。
**Extract** 函数返回一个由提取的层次结构元素中的元组组成的集。 对于指定集中的每个元组，将指定层次结构的成员提取到结果集中的新元组。 此函数始终删除重复元组。
**Extract** 函数执行交叉联接函数的相反操作。
以下查询演示如何对 **NonEmpty** 函数返回的一组元组使用 **Extract** 函数：
```
SELECT [Measures].[Internet Sales Amount] ON 0,  
//Returns the distinct combinations of Customer and Date for all purchases  
//of Bike Racks or Bike Stands  
EXTRACT(  
NONEMPTY(  
[Customer].[Customer].[Customer].MEMBERS  
*  
[Date].[Date].[Date].MEMBERS  
*  
{[Product].[Product Categories].[Subcategory].&[26],[Product].[Product Categories].[Subcategory].&[27]}  
*  
{[Measures].[Internet Sales Amount]}  
)  
,  [Customer].[Customer], [Date].[Date])  
ON 1  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


