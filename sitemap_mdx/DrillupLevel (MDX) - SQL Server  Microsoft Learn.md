#### 通过
# DrillupLevel (MDX)
浅化某个集在指定级别以下的成员。
```
  
DrillupLevel(Set_Expression [ , Level_Expression ] )  

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
_Level_Expression_ 返回级别的有效多维表达式 (MDX)。
**DrillupLevel** 函数返回一组成员，这些成员基于指定集中包含的成员进行分层组织。 指定集中的成员顺序将予以保留。
如果指定了级别表达式， **DrillupLevel** 函数将通过仅检索高于指定级别的成员来构造集。 如果指定了级别表达式，并且指定集中表示的指定级别没有成员，则返回指定的集。
如果未指定级别表达式，则此函数只检索那些比指定的集所引用的第一个维度的最低级别高一个级别的成员，然后用它们来构造集。
下例将返回位于子类别级别之上第一个集中的成员集。
```
SELECT DrillUpLevel   
  ({[Product].[Product Categories].[All Products]  
    ,[Product].[Product Categories].[Subcategory].&[32],  
    [Product].[Product Categories].[Product].&[215]},  
  [Product].[Product Categories].[Subcategory]  
    )  
  ON 0  
  FROM [Adventure Works]  
  WHERE [Measures].[Internet Order Quantity]  

```

1月27日 15时 - 1月27日 15时 


