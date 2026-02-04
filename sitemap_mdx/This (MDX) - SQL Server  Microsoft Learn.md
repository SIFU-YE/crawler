#### 通过
# This (MDX)
返回用于多维表达式 (MDX) 脚本中的分配的当前子多维数据集。
**可以使用 This** 函数代替任何子多维数据集表达式，以在 MDX 计算脚本的当前范围内提供当前子多维数据集。 **此** 函数必须在赋值左侧使用。
以下 MDX 脚本片段说明如何将 This 关键字用于 SCOPE 语句来为子多维数据集进行分配：
```
Scope  
(  
[Date].[Fiscal Year].&[2005],  
[Date].[Fiscal].[Fiscal Quarter].Members,  
[Measures].[Sales Amount Quota]  
) ;  
This = ParallelPeriod  
(  
[Date].[Fiscal].[Fiscal Year], 1,  
[Date].[Fiscal].CurrentMember  
) * 1.35 ;  
/*-- Allocate equally to months in FY 2002 -----------------------------*/  
Scope  
(  
[Date].[Fiscal Year].&[2002],  
[Date].[Fiscal].[Month].Members  
) ;  
This = [Date].[Fiscal].CurrentMember.Parent / 3 ;  
End Scope ;  
End Scope;  

```

1月27日 15时 - 1月27日 15时 


