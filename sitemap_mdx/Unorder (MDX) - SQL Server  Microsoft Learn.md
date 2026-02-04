#### 通过
# Unorder (MDX)
从指定集中删除任何强制排序。
```
  
Unorder(Set_Expression)   

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
**Unorder** 函数删除任何其他函数或语句（如 Order 函数）对集中包含的元组施加的任何排序。 Unorder**函数返回** 的集中元组的顺序不确定。
**Unorder** 函数用作查询优化设置处理的提示。 如果集中元组的顺序对计算或查询不重要，则使用 **Unorder** 函数可以在此类情况下提供性能优势。 例如， 当提供给此函数的集与 Analysis Services 需要保留顺序相比，NonEmpty （MDX） 函数的性能可能更好，尽管使用 SQL Server 2017 Analysis Services，查询处理器会尝试为许多函数（如 **Sum** 和 **Aggregate** ）自动执行此函数。 使用 **Unorder** 的性能优势可能仅在包含数百万元组的非常大的集上明显。
下面的伪代码说明了此函数的语法。
```
NonEmpty (UnOrder (<set_expression>))  

```

1月27日 15时 - 1月27日 15时 


