#### 通过
# Union (MDX)
返回两个集的并集，并且可以选择保留重复成员。
```
  
Standard syntax  
Union(Set_Expression1, Set_Expression2 [,...n][, ALL])  
  
Alternate syntax 1  
Set_Expression1 + Set_Expression2 [+...n]  
  
Alternate syntax 2  
{Set_Expression1 , Set_Expression2 [,...n]}  

```

_设置表达式 1_ 返回集的有效多维表达式 (MDX)。
_设置表达式 2_ 返回集的有效多维表达式 (MDX)。
此函数返回两个或多个指定集的并集。 使用标准语法和备用语法 1 时，默认情况下会消除重复项。 使用标准语法时，使用 **ALL** 标志在联接集中保留重复项。 从该集的尾部删除重复项。 使用替代语法 2 时始终会保留重复项。
以下示例演示了使用每种语法的 **Union** 函数的行为。
```
SELECT Union   
   ([Date].[Calendar Year].children  
   , {[Date].[Calendar Year].[CY 2002]}  
   , {[Date].[Calendar Year].[CY 2003]}  
   ) ON 0  
FROM [Adventure Works]  
  

```
```
SELECT Union   
   ([Date].[Calendar Year].children  
   , {[Date].[Calendar Year].[CY 2002]}  
   , {[Date].[Calendar Year].[CY 2003]}  
   , ALL  
   ) ON 0  
FROM [Adventure Works]  
  

```

### 替代语法 1，消除重复项
```
SELECT   
   [Date].[Calendar Year].children   
   + {[Date].[Calendar Year].[CY 2002]}   
   + {[Date].[Calendar Year].[CY 2003]} ON 0  
FROM [Adventure Works]  
  

```

### 替代语法 2，保留重复项
```
SELECT   
   {[Date].[Calendar Year].children  
   , [Date].[Calendar Year].[CY 2002]  
   , [Date].[Calendar Year].[CY 2003]} ON 0  
FROM [Adventure Works]  
  

```

1月27日 15时 - 1月27日 15时 


