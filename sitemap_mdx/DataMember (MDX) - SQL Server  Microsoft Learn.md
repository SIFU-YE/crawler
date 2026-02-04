#### 通过
# DataMember (MDX)
返回系统生成的、与某个维度的非叶成员相关联的数据成员。
```
  
Member_Expression.DataMember  

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
此函数对任何层次结构中的非叶成员进行操作，可由 UPDATE CUBE 语句 (MDX)  命令直接将数据写回非叶成员，而不是叶成员的后代。
如果指定的成员为叶成员，或者如果非叶成员没有关联的数据成员，则返回指定的成员。
以下示例在计算度量值中使用 **DataMember** 函数来显示每个员工的销售配额：
```
WITH MEMBER measures.IndividualQuota AS   
([Employee].[Employees].currentmember.datamember, [Measures].[Sales Amount Quota])  
,FORMAT_STRING='Currency'  
SELECT {[Measures].[Sales Amount Quota],[Measures].IndividualQuota} ON COLUMNS,  
[Employee].[Employees].MEMBERS ON ROWS  
FROM [Adventure Works]  

```

MDX 函数参考 (MDX) MDX 中的重要概念 (Analysis Services)
1月27日 15时 - 1月27日 15时 


