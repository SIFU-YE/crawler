#### 通过
# MemberValue (MDX)
返回成员的值。
```
  
Member_Expression.MemberValue  

```

_Member_Expression_ 计算结果为成员的有效多维表达式 (MDX)。
返回的成员值包含以下信息（按这些信息在返回值中出现的顺序列出）：
  * 值绑定（如果已定义）。
  * 原始数据类型的键（如果不存在名称绑定，或者键和标题绑定到同一列）。
  * 成员的标题。


下例将返回 Adventure Works 多维数据集 Date 维度中的第一个日期的值绑定、成员键和标题。
```
WITH MEMBER Measures.ValueColumn as [Date].[Calendar].[July 1, 2001].MemberValue  
MEMBER Measures.KeyColumn as [Date].[Calendar].[July 1, 2001].Member_Key  
MEMBER Measures.NameColumn as [Date].[Calendar].[July 1, 2001].Member_Name  
  
SELECT {Measures.ValueColumn, Measures.KeyColumn, Measures.NameColumn}  ON 0  
from [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


