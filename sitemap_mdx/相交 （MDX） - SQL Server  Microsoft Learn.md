#### 通过
# 相交 （MDX）
返回两个输入集的交集，可以选择保留重复项。
```
  
Intersect(Set_Expression1 , Set_Expression2 [ , ALL ] )  

```

_Set_Expression1_ 返回集的有效多维表达式 （MDX） 表达式。
_Set_Expression2_ 返回集的有效多维表达式 （MDX） 表达式。
**Intersect** 函数返回两组的交集。 默认情况下，该函数在与集相交之前从这两个集中删除重复项。 指定的两个集必须具有相同的维数。
可选的 **ALL** 标志保留重复项。 如果指定 **了 ALL** ， **则 Intersect** 函数会像往常一样与非重复元素相交，并且与第一个集中具有匹配重复项的第一个集中的每个重复项相交。 指定的两个集必须具有相同的维数。
以下查询返回 Years 2002 和 2003，这两个成员都出现在指定的集中：
```
SELECT  
INTERSECT(  
{[Date].[Calendar Year].&[2001], [Date].[Calendar Year].&[2002],[Date].[Calendar Year].&[2003]}  
, {[Date].[Calendar Year].&[2002],[Date].[Calendar Year].&[2003], [Date].[Calendar Year].&[2004]})  
ON 0  
FROM  
[Adventure Works]  

```

以下查询失败，因为指定的两组包含不同层次结构的成员：
```
SELECT  
INTERSECT(  
{[Date].[Calendar Year].&[2001]}  
, {[Customer].[City].&[Abingdon]&[ENG]})  
ON 0  
FROM  
[Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


