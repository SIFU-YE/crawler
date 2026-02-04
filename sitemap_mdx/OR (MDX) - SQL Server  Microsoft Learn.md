#### 通过
# OR (MDX)
对数值表达式执行逻辑或运算。
```
  
Expression1 OR Expression2   

```

Expression1 返回数值的有效多维表达式 (MDX) 表达式。
Expression2 返回数值的有效 MDX 表达式。
一个布尔值，如果其中一个或两个参数的计算结果为 **true** ，则返回 **true** ;否则为 **false** 。
**OR** 运算符将两个参数视为布尔值， (零，0，为 **false** ;否则，在运算符执行逻辑析构之前，**) true** 。 下表说明了 **OR** 运算符如何执行逻辑析构。
Expression1 | Expression2 | 返回值  
---|---|---  
true | true  
true  
以下查询包含一个计算度量值，如果“客户”维度的“性别”层次结构上的当前成员为“男性”或“客户”维度的“婚姻状态”层次结构上的当前成员为“已婚”，则返回字符串“MARRIED OR MALE”;否则返回字符串“UNMARRIED OR FEMALE”。
```
WITH  
MEMBER MEASURES.ORDEMO AS  
IIF(  
([Customer].[Gender].CURRENTMEMBER IS [Customer].[Gender].&[M])  
OR  
([Customer].[Marital Status].CURRENTMEMBER IS [Customer].[Marital Status].&[M]),  
"MARRIED OR MALE",  
"UNMARRIED OR FEMALE")  
SELECT [Customer].[Gender].[Gender].MEMBERS ON 0,  
[Customer].[Marital Status].[Marital Status].MEMBERS ON 1  
FROM [Adventure Works]  
WHERE(MEASURES.ORDEMO)  

```

1月27日 15时 - 1月27日 15时 


