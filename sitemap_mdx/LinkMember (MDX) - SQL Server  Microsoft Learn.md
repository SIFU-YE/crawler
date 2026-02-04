#### 通过
# LinkMember (MDX)
返回相当于指定层次结构中的指定成员的成员。
```
  
LinkMember(Member_Expression, Hierarchy_Expression)   

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
_Hierarchy_Expression_ 返回层次结构的有效多维表达式 (MDX)。
**LinkMember** 函数从指定层次结构返回成员，该成员与相关层次结构中指定成员的每个级别的键值匹配。 每个级别上的属性必须具有相同的键基数和数据类型。 在非自然层次结构中，如果某属性的键值有多个匹配项，结果将是错误的或不确定。
以下示例使用 **LinkMember** 函数在 Adventure Works 多维数据集中返回日历层次结构中 Date.Date 属性层次结构的 2002 年 7 月 1 日成员的默认度量值。
```
SELECT  Hierarchize  
   (Ascendants   
      (LinkMember   
         ([Date].[Date].[July 1, 2002], [Date].[Calendar]  
         )  
       )  
    ) ON 0  
FROM [Adventure Works]  

```

Hierarchize (MDX) Ascendants (MDX) MDX 函数参考 (MDX)
1月27日 15时 - 1月27日 15时 


