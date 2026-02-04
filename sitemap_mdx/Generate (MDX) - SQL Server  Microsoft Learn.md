#### 通过
# Generate (MDX)
将一个集应用于另一个集中的每个成员，然后对得到的集求并集。 另外，此函数返回通过用字符串表达式对集求值而创建的串联字符串。
```
  
Set expression syntax  
Generate( Set_Expression1 ,  Set_Expression2 [ , ALL ]  )  
  
String expression syntax  
Generate( Set_Expression1 ,  String_Expression [ ,Delimiter ]  )  

```

_Set_Expression1_ 返回集的有效多维表达式 (MDX)。
_Set_Expression2_ 返回集的有效多维表达式 (MDX)。
_String_Expression_ 通常为指定集中每个元组当前成员名称 (CurrentMember.Name) 的有效字符串表达式。
_分隔符_ 以字符串表达式表示的有效分隔符。
如果指定了第二个集， **则 Generate** 函数将返回一个集，方法是将第二个集中的元组应用于第一个集中的每个元组，然后按联合联接生成的元组。 如果指定 **了 ALL** ，函数将保留生成的集中重复项。
如果指定了字符串表达式， **则 Generate** 函数将返回一个字符串，方法是针对第一个集中的每个元组计算指定的字符串表达式，然后串联结果。 根据需要，可以分隔字符串，从而分隔得到的串联字符串中的每个结果。
在以下示例中，由于 [Date].[Calendar Year].[Calendar Year].MEMBERS 集中有四个成员，因此，查询四次返回包含 Measure Internet Sales Amount 的集：
```
SELECT   
GENERATE( [Date].[Calendar Year].[Calendar Year].MEMBERS  
, {[Measures].[Internet Sales Amount]}, ALL)  
ON 0  
FROM [Adventure Works]  

```

删除 ALL 将更改查询，这样仅返回一次 Internet Sales Amount：
```
SELECT   
GENERATE( [Date].[Calendar Year].[Calendar Year].MEMBERS  
, {[Measures].[Internet Sales Amount]})  
ON 0  
FROM [Adventure Works]  

```

**Generate** 最常见的实际用途是在一组成员上计算复杂的集表达式（如 TopCount）。 以下示例查询显示行上每个日历年的前 10 种产品：
```
SELECT   
{[Measures].[Internet Sales Amount]}  
ON 0,  
GENERATE(   
[Date].[Calendar Year].[Calendar Year].MEMBERS  
, TOPCOUNT(  
[Date].[Calendar Year].CURRENTMEMBER  
*  
[Product].[Product].[Product].MEMBERS  
,10, [Measures].[Internet Sales Amount]))  
ON 1  
FROM [Adventure Works]  

```

请注意，每年显示不同的前 10 个，并且使用 **“生成** ”是获得此结果的唯一方法。 将日历年和前 10 种产品的集进行简单交叉联接将显示所有时间的前 10 种产品（每年都重复），如以下示例所示：
```
SELECT   
{[Measures].[Internet Sales Amount]}  
ON 0,  
[Date].[Calendar Year].[Calendar Year].MEMBERS  
*   
TOPCOUNT(  
[Product].[Product].[Product].MEMBERS  
,10, [Measures].[Internet Sales Amount])  
ON 1  
FROM [Adventure Works]  

```

以下示例演示了如何使用 **Generate** 返回字符串：
```
WITH   
MEMBER MEASURES.GENERATESTRINGDEMO AS  
GENERATE(   
[Date].[Calendar Year].[Calendar Year].MEMBERS,  
[Date].[Calendar Year].CURRENTMEMBER.NAME)  
MEMBER MEASURES.GENERATEDELIMITEDSTRINGDEMO AS  
GENERATE(   
[Date].[Calendar Year].[Calendar Year].MEMBERS,  
[Date].[Calendar Year].CURRENTMEMBER.NAME, " AND ")  
SELECT   
{MEASURES.GENERATESTRINGDEMO, MEASURES.GENERATEDELIMITEDSTRINGDEMO}  
ON 0  
FROM [Adventure Works]  

```

这种形式的 **Generate** 函数在调试计算时非常有用，因为它使你能够返回一个字符串，显示一个集中所有成员的名称。 这可能比 SetToStr (MDX)  函数返回的集的严格 MDX 表示形式更容易阅读。
1月27日 15时 - 1月27日 15时 


