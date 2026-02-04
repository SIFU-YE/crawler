#### 通过
# Properties (MDX)
返回一个包含成员属性值的字符串，或返回一个强类型值。
```
  
Member_Expression.Properties(Property_Name [, TYPED])  

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
_Property_Name_ 成员属性名称的有效字符串表达式。
**Properties** 函数返回指定成员属性的指定成员的值。 成员属性可以是任何内部成员属性（如 **NAME** 、 **ID** 、 **KEY** 或 **CAPTION** ），也可以是用户定义的成员属性。 有关详细信息，请参阅 MDX) (内部成员 属性和用户定义成员属性 (MDX) 。
默认情况下，将该值强迫为一个字符串。 如果指定 **了 TYPED** ，则返回值为强类型。
  * 如果属性是内部的，则函数返回成员的原始类型。
  * 如果属性类型是用户定义的，则返回值的类型与 **MemberValue** 函数的返回值的类型相同。


Properties ('Key') 返回与 Key0 相同的结果，但组合键除外。 Properties ('Key') 将为组合键返回 null。 对组合键使用 Key _x_ 语法，如示例中所示。 Properties('Key0')、Properties('Key1')、Properties('Key2') 等共同构成了组合键。
下例既返回内部属性也返回用户定义成员属性，并且利用 TYPED 参数返回“星期几”成员属性的强类型值。
```
WITH MEMBER Measures.MemberName AS   
   [Date].[Calendar].[July 1, 2003].Properties('Name')  
MEMBER Measures.MemberVal AS   
   [Date].[Calendar].[July 1, 2003].Properties('Member_Value')  
MEMBER Measures.MemberKey AS   
   [Date].[Calendar].[July 1, 2003].Properties('Key')  
MEMBER Measures.MemberID AS   
   [Date].[Calendar].[July 1, 2003].Properties('ID')  
MEMBER Measures.MemberCaption AS   
   [Date].[Calendar].[July 1, 2003].Properties('Caption')  
MEMBER Measures.DayName AS   
   [Date].[Calendar].[July 1, 2003].Properties('Day Name', TYPED)  
MEMBER Measures.DayNameTyped AS   
   [Date].[Calendar].[July 1, 2003].Properties('Day Name')  
MEMBER Measures.DayofWeek AS   
   [Date].[Calendar].[July 1, 2003].Properties('Day of Week')  
MEMBER Measures.DayofMonth AS   
   [Date].[Calendar].[July 1, 2003].Properties('Day of Month')  
MEMBER Measures.DayofYear AS   
   [Date].[Calendar].[July 1, 2003].Properties('Day of Year')  
  
SELECT {Measures.MemberName  
   , Measures.MemberVal  
   , Measures.MemberKey  
   , Measures.MemberID  
   , Measures.MemberCaption  
   , Measures.DayName  
   , Measures.DayNameTyped  
   , Measures.DayofWeek  
   , Measures.DayofMonth  
   , Measures.DayofYear  
   }  ON 0  
FROM [Adventure Works]  

```

以下示例演示如何使用 KEY _x_ 属性。
```
WITH   
MEMBER Measures.MemberKey AS   
   [Customer].[Customer Geography].[State-Province].&[QLD]&[AU].Properties('Key')  
MEMBER Measures.MemberKey0 AS   
   [Customer].[Customer Geography].[State-Province].&[QLD]&[AU].Properties('Key0')  
MEMBER Measures.MemberKey1 AS   
   [Customer].[Customer Geography].[State-Province].&[QLD]&[AU].Properties('Key1')  
  
SELECT {Measures.MemberKey  
   , Measures.MemberKey0  
   , Measures.MemberKey1     
   }  ON 0  
FROM [Adventure Works]  
  

```

1月27日 15时 - 1月27日 15时 


