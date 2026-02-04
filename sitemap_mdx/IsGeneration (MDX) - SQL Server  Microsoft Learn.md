#### 通过
# IsGeneration (MDX)
返回指定成员是否处于指定的代中。
```
  
IsGeneration(Member_Expression, Generation_Number)   

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
_Generation_Number_ 指定对指定成员进行计算的代的数值表达式。
如果指定成员位于指定的代号中， **IsGeneration** 函数将返回 **true** 。 否则，函数返回 **false** 。 此外，如果指定成员的计算结果为空成员， **IsGeneration** 函数将返回 **false** 。
为了创建代索引，叶成员的代索引为 0。 非叶成员的代索引的确定方式为：先从指定成员的所有子成员的并集中获取最高的代索引，然后向该索引添加 1。 由于非叶成员的代索引的确定方式，一个非叶成员可能会属于多个代。
如果 [Date].[Fiscal].CurrentMember 属于第二代，下面的示例将返回 TRUE。
```
WITH MEMBER MEASURES.ISGENERATIONDEMO AS  
IsGeneration([Date].[Fiscal].CURRENTMEMBER, 2)  
SELECT {MEASURES.ISGENERATIONDEMO} ON 0,  
[Date].[Fiscal].MEMBERS ON 1  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


