#### 通过
# Ancestor (MDX)
此函数返回指定成员在指定级别或距离处的祖先。
```
  
Level syntax  
Ancestor(Member_Expression, Level_Expression)  
  
Numeric syntax  
Ancestor(Member_Expression, Distance)  

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
_Level_Expression_ 返回级别的有效多维表达式 (MDX)。
_距离_ 指定与指定成员距离的有效数值表达式。
使用 **上级** 函数，可为函数提供 MDX 成员表达式，然后提供作为成员上级级别的 MDX 表达式或表示该成员之上的级别数的数值表达式。 有了此信息， **Ancestors** 函数将返回该级别的上级成员。
若要返回包含上级成员的集，而不是仅使用上级成员，请使用 上级 (MDX)  函数。
如果指定了级别表达式， **则 Ancestor** 函数将返回指定级别的指定成员的上级。 如果指定成员与指定级别不在同一个层次结构中，该函数将返回错误。
如果指定了距离， **则 Ancestor** 函数返回指定成员的上级，即成员表达式指定的层次结构中指定的步骤数。 可以将成员指定为属性层次结构的成员或用户定义层次结构的成员，有时还可以指定为父子层次结构的成员。 数值 1 返回成员的父成员，数值 2 返回成员的祖父成员（如果存在）。 数值 0 返回成员本身。
对于父级级别未知或无法命名的情况，请使用这种形式的 **上级** 函数。
下面的示例使用一个级别表达式，并返回 Australia 中每个 State-Province 的 Internet Sales Amount 及其占 Australia 总 Internet Sales Amount 的百分比。
```
WITH MEMBER Measures.x AS [Measures].[Internet Sales Amount] /   
   (  
   [Measures].[Internet Sales Amount],    
      Ancestor   
         (  
         [Customer].[Customer Geography].CurrentMember,  
            [Customer].[Customer Geography].[Country]  
         )  
   ), FORMAT_STRING = '0%'  
SELECT {[Measures].[Internet Sales Amount], Measures.x} ON 0,  
{  
   Descendants   
      (  
        [Customer].[Customer Geography].[Country].&[Australia],  
           [Customer].[Customer Geography].[State-Province], SELF   
      )  
} ON 1  
FROM [Adventure Works]  

```

以下示例使用数值表达式并返回澳大利亚每个State-Province的 Internet Sales Amount，以及其占所有国家/地区的 Internet 销售总额的百分比。
```
WITH MEMBER Measures.x AS [Measures].[Internet Sales Amount] /   
   (  
      [Measures].[Internet Sales Amount],  
         Ancestor   
            ([Customer].[Customer Geography].CurrentMember, 2)  
   ), FORMAT_STRING = '0%'  
SELECT {[Measures].[Internet Sales Amount], Measures.x} ON 0,  
{  
   Descendants   
      (  
         [Customer].[Customer Geography].[Country].&[Australia],  
            [Customer].[Customer Geography].[State-Province], SELF   
      )  
} ON 1  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


