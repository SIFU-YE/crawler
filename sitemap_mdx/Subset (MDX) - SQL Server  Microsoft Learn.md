#### 通过
# Subset (MDX)
返回指定集中元组的子集。
```
  
Subset(Set_Expression, Start [ ,Count ] )  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Start_ 指定要返回第一个元组位置的有效数值表达式。
_Count_ 指定要返回的元组数的有效数值表达式。
从指定的集中， **Subset** 函数返回一个子集，该子集包含指定数量的元组，从指定的开始位置开始。 开始位置基于以零为基的索引；即 0 对应于指定集中的第一个元组，1 对应于第二个元组，依此类推。
如果未指定 _Count_ ，该函数将返回从 _Start_ 到集末尾的所有元组。
下例根据 Reseller Gross Profit（分销商毛利润），返回前五个销售产品子类别的分销商销售额度量值，而不管层次结构如何。 **使用 Order** 函数对结果进行排序后，Subset 函数用于仅返回结果中的前五个集。
```
SELECT Subset  
   (Order   
      ([Product].[Product Categories].[SubCategory].members  
         ,[Measures].[Reseller Gross Profit]  
         ,BDESC  
      )  
   ,0  
   ,5  
   ) ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


