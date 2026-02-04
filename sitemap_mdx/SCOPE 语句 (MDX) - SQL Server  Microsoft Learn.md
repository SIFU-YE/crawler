#### 通过
# MDX 脚本 - SCOPE
将指定多维表达式 (MDX) 语句的作用域限制于指定的子多维数据集。
```
  
SCOPE(Subcube_Expression)   
   [ MDX_Statement ]  
END SCOPE  
  
Subcube_Expression ::=(Auxiliary_Subcube [, Auxiliary_Subcube,...n])  
  
Auxiliary_Subcube ::=   
        Limited_Set   
    | Root([dimension_name])   
    | Leaves([dimension_name])  
  
Limited_Set ::=   
        single_tuple   
    | member   
    | Common_Grain_Members   
    | hierarchy.members   
    | level.members   
    | {}   
    | Descendants  
            (  
                  Member  
         , [level  
         [  
            , SELF   
             | AFTER   
                          | BEFORE   
                          | SELF_AND_AFTER   
                          | SELF_AND_BEFORE   
                          | SELF_BEFORE_AFTER   
                          | LEAVES  
                  ]  
            )   
[* <limited set>]  

```

_Subcube_Expression_ 有效的 MDX 子多维数据集表达式。
_MDX_Statement_ 有效的 MDX 语句。
_Common_Grain_Members_ 有效的 MDX 语句，该语句的值为粒度相同的成员。
_single_tuple_ 单个元组。
SCOPE 语句用于确定执行一个或多个 MDX 语句时会影响到的子多维数据集。 除非 MDX 语句包含在 SCOPE 语句中，否则 MDX 语句的隐式作用域为整个多维数据集。
SCOPE 语句会处理隐藏的成员。
SCOPE 语句将创建公开“孔”的子多维数据集，而不考虑 **MDX 兼容性** 设置。 例如，`Scope( Customer.State.members )` 语句可以在不包含州的国家或地区中包括州，但在其他情况下会插入不可见的占位符成员。
在 SCOPE 语句中创建的计算成员和命名集不受 SCOPE 语句的影响。
以下示例根据 Adventure Works 示例解决方案中的 MDX 计算脚本，将当前范围定义为 2005 财政年度的会计季度和销售额配额度量值，然后使用 **ParallelPeriod** 函数将值分配给当前范围内的单元格。 然后，该示例使用另一个 SCOPE 语句修改范围，然后使用 This (MDX)  函数执行另一个赋值。
```
Scope   
 (   
    [Date].[Fiscal Year].&[2005],  
    [Date].[Fiscal].[Fiscal Quarter].Members,  
    [Measures].[Sales Amount Quota]  
 ) ;     
  
   This = ParallelPeriod                               
          (   
             [Date].[Fiscal].[Fiscal Year], 1,  
             [Date].[Fiscal].CurrentMember   
          ) * 1.35 ;  
  
/*-- Allocate equally to months in FY 2002 -----------------------------*/  
  
  Scope   
  (   
     [Date].[Fiscal Year].&[2002],  
     [Date].[Fiscal].[Month].Members   
  ) ;     
  
    This = [Date].[Fiscal].CurrentMember.Parent / 3 ;     
  
  End Scope ;     
End Scope ;     

```

1月27日 15时 - 1月27日 15时 


