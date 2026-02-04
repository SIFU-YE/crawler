#### 通过
# IsEmpty (MDX)
返回表达式的计算结果是否为空单元值。
```
  
IsEmpty(Value_Expression)   

```

_Value_Expression_ 有效 MDX（多维表达式）表达式，通常返回成员或元组的单元坐标。
如果计算的表达式为空单元格值， **则 IsEmpty** 函数返回 **true** 。 否则，此函数返回 **false** 。
成员的默认属性为成员的值。
**IsEmpty** 函数是可靠地测试空单元格的唯一方法，因为空单元格值在 Analysis Services 中具有特殊含义。
如果值表达式的计算返回错误，则函数将返回 **false** 。 值表达式也可能返回错误，例如，属性引用引用了无效或不存在的属性。
有关空单元的详细信息，请参阅 OLE DB 文档。
如果 Date 维度的 Fiscal 层次结构上当前成员的 Internet Sales Amount 返回一个空单元，则下面的示例将返回 TRUE：
```
WITH MEMBER MEASURES.ISEMPTYDEMO AS  
IsEmpty([Measures].[Internet Sales Amount])  
SELECT {[Measures].[Internet Sales Amount],MEASURES.ISEMPTYDEMO} ON 0,  
[Date].[Fiscal].MEMBERS ON 1  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


