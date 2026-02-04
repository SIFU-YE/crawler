#### 通过
# AddCalculatedMembers (MDX)
返回通过将计算成员添加到指定集而生成的集。
```
  
AddCalculatedMembers(Set_Expression)   

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
默认情况下，MDX 在解析集函数时会排除计算成员。 **AddCalculatedMembers** 函数检查Set_Expression中指定的集表达式 _，_ 并包括计算成员是该集表达式范围内包含的成员的同级。
此函数只能与一维集表达式一起使用。
以下示例说明了此函数的用法。
```
-- This query returns the calculated members for the cube  
-- by retrieving all members, and then excluding non-calculated members.  
SELECT   
   AddCalculatedMembers(  
      {[Measures].Members}  
      )-[Measures].Members ON COLUMNS  
FROM [Adventure Works]   

```

以下示例从 **Adventure Works** 多维数据集返回`Measures.[Unit Price]`成员，以及**“度量值”** 维度中的所有计算成员。
```
SELECT  
   AddCalculatedMembers({Measures.[Unit Price]}) ON COLUMNS  
FROM   
   [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


