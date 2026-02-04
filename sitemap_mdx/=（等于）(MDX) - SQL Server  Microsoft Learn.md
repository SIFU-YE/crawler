#### 通过
# =（等于）(MDX)
执行比较运算，以确定一个多维表达式 (MDX) 的值是否等于另一个 MDX 表达式的值。
若要比较对象，请使用 IS (MDX)  运算符。 例如，检查查询轴上的当前成员是否为特定成员时，使用 IS 运算符。
```
  
MDX_Expression = MDX_Expression   

```

_MDX_Expression_ 有效的 MDX 表达式。
布尔值，具体情形如下：
  * 如果第一个参数的值等于第二个参数的值，则**为 true** 。
  * 如果第一个参数的值不等于第二个参数的值，则为 **false** 。
  * 如果两个参数均为 null，或者一个参数为 null，另一个参数为 0，则为 **true** 。


以下查询说明上述情况的示例：
```
With  
--Returns true  
Member [Measures].bool1 as 1=1  
--Returns false  
Member [Measures].bool2 as 1=0  
--Returns true  
Member [Measures].bool3 as null=null  
--Returns true  
Member [Measures].bool4 as 0=null  
--Returns false  
Member [Measures].bool5 as 1=null  
Select {[Measures].bool1,[Measures].bool2,[Measures].bool3,[Measures].bool4,[Measures].bool5}  
On 0  
From [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


