#### 通过
# Item（成员）(MDX)
返回指定元组中的成员。
```
  
Tuple_Expression.Item( Index )  

```

_Tuple_Expression_ 返回元组的有效多维表达式 (MDX)。
_Index_ 指定要返回元组中指定特定成员位置的有效数值表达式。
**Item** 函数从指定的元组返回成员。 函数返回在 _Index_ 指定的从零开始的位置找到的成员。
下面的示例返回各列上的成员 `[2003]`（元组 `[Date].[Calendar Year].&[2003], [Measures].[Internet Sales Amount] ).` 中的第一项）：
```
SELECT  
{( [Date].[Calendar Year].&[2003], [Measures].[Internet Sales Amount] ).Item(0)} ON 0  
,{[Measures].[Reseller Sales Amount]} ON 1  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


