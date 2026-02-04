#### 通过
# Tail (MDX)
返回集末尾的子集。
```
  
Tail(Set_Expression [ ,Count ] )  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Count_ 指定要返回的元组数的有效数值表达式。
**Tail** 函数从指定集的末尾返回指定数量的元组。 会保留元素的顺序。 _Count_ 的默认值为 1。 如果指定的元组数目小于 1，则该函数返回空集。 如果指定的元组数目超过了集中的元组数目，则此函数返回原始集。
下例根据 Reseller Gross Profit（分销商毛利润），返回前五个销售产品子类别的分销商销售额度量值，而不管层次结构如何。 **Tail** 函数用于在使用 **Order** 函数对结果进行反向排序后，仅返回结果中的最后五个集。
```
SELECT Tail  
   (Order   
      ([Product].[Product Categories].[SubCategory].members  
         ,[Measures].[Reseller Gross Profit]  
         ,BASC  
      )  
   ,5  
   ) ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


