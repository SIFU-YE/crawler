#### 通过
# Ordinal (MDX)
返回与某一级别相关联的从零开始计算的序数值。
```
  
Level_Expression.Ordinal   

```

_Level_Expression_ 返回级别的有效多维表达式 (MDX)。
**Ordinal** 函数经常与 **IIF** 和 **CurrentMember** 函数结合使用，根据查询结果中每个特定单元格的序号位置，在不同的层次结构级别有条件地显示不同的值。 例如，可以使用 **Ordinal** 函数在某些级别执行计算，并在其他级别显示默认值“N/A”。
下面的示例返回 Calendar 层次结构中的 Calendar Quarter 级别的序号。
```
WITH MEMBER Measures.x AS [Date].[Calendar].[Calendar Quarter].Ordinal  
SELECT Measures.x on 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


