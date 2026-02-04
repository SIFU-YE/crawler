#### 通过
# Item（元组）(MDX)
返回某个集中的元组。
```
  
Index syntax  
Set_Expression.Item(Index)  
  
String expression syntax  
Set_Expression.Item(String_Expression1 [ ,String_Expression2,...n])  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_String_Expression1_ 通常是以字符串表示的元组的有效字符串表达式。
_String_Expression2_ 通常是以字符串表示的元组的有效字符串表达式。
_Index_ 根据集中位置指定要返回的特定元组的有效数值表达式。
**Item** 函数从指定的集返回元组。 有三种可能的方法可以调用 **Item** 函数：
  * 如果指定了单个字符串表达式， **则 Item** 函数将返回指定的元组。 例如，"([2005].Q3, [Store05])"。
  * 如果指定了多个字符串表达式， **则 Item** 函数将返回由指定坐标定义的元组。 字符串数必须与轴数一致，而且每个字符串都必须标识一个唯一的层次结构。 例如，"[2005].Q3", "[Store05]"。
  * 如果指定了整数，**Item** 函数将返回 Index 指定的从零开始的位置的元 _组。_


下面的示例返回 ([1996],Sales)：
`{([1996],Sales), ([1997],Sales), ([1998],Sales)}.Item(0)`
下面的示例使用一个级别表达式，并返回 Australia 中每个 State-Province 的 Internet Sales Amount 及其占 Australia 总 Internet Sales Amount 的百分比。 此示例使用 Item 函数从 **Ancestors** 函数返回的集中提取第一个 (，并且仅提取元组) 。
```
WITH MEMBER Measures.x AS [Measures].[Internet Sales Amount] /   
   ( [Measures].[Internet Sales Amount],    
      Ancestors   
      ( [Customer].[Customer Geography].CurrentMember,  
        [Customer].[Customer Geography].[Country]  
      ).Item (0)  
   ), FORMAT_STRING = '0%'  
SELECT {[Measures].[Internet Sales Amount], Measures.x} ON 0,  
{ Descendants   
   ( [Customer].[Customer Geography].[Country].&[Australia],  
     [Customer].[Customer Geography].[State-Province], SELF   
   )   
} ON 1  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


