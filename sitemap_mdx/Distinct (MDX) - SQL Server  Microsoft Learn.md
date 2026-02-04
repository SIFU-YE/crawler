#### 通过
# Distinct (MDX)
对指定的集求值，删除该集中的重复元组，然后返回结果集。
```
  
Distinct(Set_Expression)  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
如果 **Distinct** 函数在指定集中发现重复元组，则函数仅保留重复元组的第一个实例，同时保持该集的顺序不变。
以下示例查询说明如何将 Distinct 函数与命名集一起使用，以及如何将该函数与 Count 函数一起使用来查找集中不同元组的数目：
```
WITH SET MySet AS  
{[Customer].[Customer Geography].[Country].&[Australia],[Customer].[Customer Geography].[Country].&[Australia],  
[Customer].[Customer Geography].[Country].&[Canada],[Customer].[Customer Geography].[Country].&[France],  
[Customer].[Customer Geography].[Country].&[United Kingdom],[Customer].[Customer Geography].[Country].&[United Kingdom]}  
MEMBER MEASURES.SETCOUNT AS  
COUNT(MySet)  
MEMBER MEASURES.SETDISTINCTCOUNT AS  
COUNT(DISTINCT(MySet))  
SELECT {MEASURES.SETCOUNT, MEASURES.SETDISTINCTCOUNT} ON 0,  
DISTINCT(MySet) ON 1  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


