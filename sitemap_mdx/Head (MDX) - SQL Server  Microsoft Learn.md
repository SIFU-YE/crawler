#### 通过
# Head (MDX)
返回集中指定数目的前几个元素，同时保留重复项。
```
  
Head(Set_Expression [ ,Count ] )  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Count_ 指定要返回的元组数的有效数值表达式。
**Head** 函数从指定集的开头返回指定数量的元组。 会保留元素的顺序。 Count 的默认值为 1。 如果指定的元组数小于 1， **Head** 函数将返回一个空集。 如果指定的元组数目超过了集中的元组数目，则此函数返回原始集。
以下示例根据 Reseller Gross Profit 返回产品的前五大销售子类别（与层次结构无关）。 使用 **Order** 函数对结果进行排序后，**Head** 函数用于仅返回结果中的前 5 个集。
```
SELECT   
[Measures].[Reseller Gross Profit] ON 0,  
Head  
   (Order   
      ([Product].[Product Categories].[SubCategory].members  
         ,[Measures].[Reseller Gross Profit]  
         ,BDESC  
      )  
   ,5  
   ) ON 1  
FROM [Adventure Works]  

```

Tail (MDX) Item（元组）(MDX) Item（成员）(MDX) Rank (MDX) MDX 函数参考 (MDX)
1月27日 15时 - 1月27日 15时 


