#### 通过
# DistinctCount (MDX)
返回集中非重复的非空元组的数目。
```
  
DistinctCount(Set_Expression)  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
**DistinctCount** 函数等效于 `Count(Distinct(Set_Expression), EXCLUDEEMPTY)`。
以下查询说明如何使用 DistinctCount 函数：
```
WITH SET MySet AS  
{[Customer].[Customer Geography].[Country].&[Australia],[Customer].[Customer Geography].[Country].&[Australia],
[Customer].[Customer Geography].[Country].&[Canada],[Customer].[Customer Geography].[Country].&[France],  
[Customer].[Customer Geography].[Country].&[United Kingdom],[Customer].[Customer Geography].[Country].&[United Kingdom]}  
* 
{([Date].[Calendar].[Date].&[20010701],[Measures].[Internet Sales Amount] )}   
MEMBER MEASURES.SETDISTINCTCOUNT AS  
DISTINCTCOUNT(MySet)  
SELECT {MEASURES.SETDISTINCTCOUNT} ON 0 
FROM [Adventure Works] 

```

DistinctCount 函数返回一个集中的非重复项数;在此示例中，可选的第二个参数用于排除没有给定元组值的项。 在这种情况下，第一个参数的 集中有四个不同的项，但 函数返回三个，因为只有澳大利亚、加拿大和法国具有 2001 年 7 月 1 日 Internet Sales Amount 的数据。
1月27日 15时 - 1月27日 15时 


