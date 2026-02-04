#### 通过
# IS (MDX)
对两个对象表达式执行逻辑比较。
```
  
Expression1 IS ( Expression2 | NULL )  

```

Expression1 返回 MDX 对象引用的有效多维表达式 (MDX) 表达式。
Expression2 返回 MDX 对象引用的有效 MDX 表达式。
一个布尔值，如果两个参数引用同一对象，则返回 **true** ;否则为 **false** 。 如果指定了 **NULL** 关键字，则 _如果 Expression1_ 为 **null** ，则运算符返回 **true** ;否则为 **false** 。
**IS** 运算符通常用于确定元组和成员是否是幂等的，这意味着它们是完全等效的。
以下示例演示如何使用 **IS** 运算符检查轴上的当前成员是否为特定成员：
```
With  
//Returns TRUE if the currentmember is Bikes  
Member [Measures].[IsBikes?] AS  
[Product].[Category].CurrentMember IS [Product].[Category].&[1]  
SELECT  
{[Measures].[IsBikes?]} ON 0,  
[Product].[Category].[Category].Members ON 1  
FROM  
[Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


