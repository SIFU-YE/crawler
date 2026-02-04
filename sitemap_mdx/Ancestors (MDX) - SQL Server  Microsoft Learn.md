#### 通过
# Ancestors (MDX)
此函数返回指定成员在指定级别或距离处的所有祖先的集。 使用 Analysis Services 时，返回的集将始终包含单个成员 - Analysis Services 不支持单个成员的多个父级。
```
  
Level syntax  
Ancestors(Member_Expression, Level_Expression)  
  
Numeric syntax  
Ancestors(Member_Expression, Distance)  

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
_Level_Expression_ 返回级别的有效多维表达式 (MDX)。
_距离_ 指定与指定成员距离的有效数值表达式。
使用 **上级** 函数时，为函数提供 MDX 成员表达式，然后提供作为该成员的上级级别的 MDX 表达式或表示该成员以上级别数的数值表达式。 利用此信息， **上级** 函数返回成员集 (该成员集由该级别的一个成员) 组成。
若要返回上级成员，而不是上级集，请使用 上级 函数。
如果指定了级别表达式，则 **Ancestors** 函数返回指定级别上指定成员的所有上级集合。 如果指定成员与指定级别不在同一层次结构中，则函数将返回错误。
如果指定了距离，则 **Ancestors** 函数将返回所有成员的集合，这些成员是成员表达式指定的层次结构中指定的步骤数。 成员可以指定为属性层次结构、用户定义层次结构的成员，或在某些情况下指定为父子层次结构的成员。 数值 1 返回父级别处的成员集，数值 2 返回祖父级别处（如果存在）的成员集。 数值 0 返回仅包含成员本身的集。
对于父级级别未知或无法命名的情况，请使用上 **级** 函数的此形式。
以下示例使用 **Ancestors** 函数返回成员、其父级和祖父级的 Internet Sales Amount 度量值。 此例使用级别表达式指定要返回的级别。 这些级别与成员表达式中指定的成员在同一个层次结构中。
```
SELECT {  
    Ancestors([Product].[Product Categories].[Product].[Mountain-100 Silver, 38],[Product].[Product Categories].[Category]),  
    Ancestors([Product].[Product Categories].[Product].[Mountain-100 Silver, 38],[Product].[Product Categories].[Subcategory]),  
    Ancestors([Product].[Product Categories].[Product].[Mountain-100 Silver, 38],[Product].[Product Categories].[Product])  
    } ON 0,  
[Measures].[Internet Sales Amount] ON 1  
FROM [Adventure Works]  

```

以下示例使用 **Ancestors** 函数返回成员、其父级和祖父级的 Internet Sales Amount 度量值。 此例使用数值表达式指定要返回的级别。 这些级别与成员表达式中指定的成员在同一个层次结构中。
```
SELECT {  
   Ancestors(  
      [Product].[Product Categories].[Product].[Mountain-100 Silver, 38],2  
      ),  
   Ancestors(  
      [Product].[Product Categories].[Product].[Mountain-100 Silver, 38],1  
      ),  
   Ancestors(  
      [Product].[Product Categories].[Product].[Mountain-100 Silver, 38],0  
      )  
   } ON 0,  
[Measures].[Internet Sales Amount] ON 1  
FROM  [Adventure Works]  

```

以下示例使用 **Ancestors** 函数返回属性层次结构成员的父级的 Internet Sales Amount 度量值。 此示例使用数值表达式来指定要返回的级别。 由于成员表达式中的成员是属性层次结构的成员，因此其父成员是“(全部)”级别。
```
SELECT {  
   Ancestors(  
      [Product].[Product].[Mountain-100 Silver, 38],1  
      )  
   } ON 0,  
[Measures].[Internet Sales Amount] ON 1  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


