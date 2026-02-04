#### 通过
# Value (MDX)
返回查询上下文中的属性层次结构的当前成员与 Measures 维度的当前成员的交集的值。
```
  
Member_Expression[.Value]   

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
**Value** 函数将指定成员的值作为字符串返回。 **Value** 参数是可选的，因为成员的值是成员的默认属性，如果未指定其他值，则为成员返回的值。 有关成员属性的详细信息，请参阅 MDX) (内部成员 属性和 MDX) (用户定义的成员属性 。
下例将返回成员值并显式返回该成员的名称。
```
WITH MEMBER [Date].[Calendar].NumericValue as [Date].[Calendar].[July 1, 2001].Value  
MEMBER [Date].[Calendar].MemberName AS [Date].[Calendar].[July 1, 2001].Name  
  
SELECT {[Date].[Calendar].NumericValue, [Date].[Calendar].MemberName} ON 0  
from [Adventure Works]  

```

下例将以轴上成员的默认返回值返回成员值。
```
SELECT {[Date].[Calendar].[July 1, 2001]} ON 0  
from [Adventure Works]  

```

MemberValue (MDX) Properties (MDX) Name (MDX) UniqueName (MDX) MDX 函数参考 (MDX)
1月27日 15时 - 1月27日 15时 


