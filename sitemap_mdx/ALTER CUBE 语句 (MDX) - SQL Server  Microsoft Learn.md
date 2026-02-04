#### 通过
# MDX 数据定义 - ALTER CUBE
更改指定多维数据集的结构，通常用于支持维度写回。 有关在应用程序中使用写回的详细信息，请参阅此博客文章： 使用 Analysis Services 生成写回应用程序 (博客) 
```
  
ALTER CUBE  
      Cube_Name | CURRENTCUBE  
      <alter clause>   
            [ < alter clause> ...n]  
  
< alter clause> ::=   
   <create dimension member clause>   
  | <remove dimension member clause>  
  | <move dimension member clause>   
    | <update clause>   
    | <create cell calculation clause>  
  
<create dimension member clause> ::=  
CREATE DIMENSION MEMBER [ParentName.]MemberName  
    , [[KEY = Key_Value]   
    | [Property_Name = Property_Value[, ...n]]  
  
<dropping clause>::=  
DROP   
      DIMENSION MEMBER Member_Name   
            Member_Name ...n ]   
      [WITH DESCENDANTS]  
      | [ SESSION ] [ CALCULATED ] MEMBER Member_Name   
                  [ ,Member_Name,...n ]   
    | SET Set_Name  
                  [ ,Set_Name,...n ]   
    | [ SESSION ] CELL CALCULATION CellCalc_Name  
                  [ ,CellCalc_Name,...n ]   
    | ACTION Action_Name  
  
<move dimension member clause> ::=  
MOVE DIMENSION MEMBER MemberName  
        [, SKIPPED_LEVELS = Unsigned_Integer]   
      [WITH DESCENDANTS]  
    UNDER ParentName      
  
<update clause> ::=  
UPDATE   
    CUSTOM ROLLUP FOR MEMBER MemberName  
      [,MemberName, ...n] AS MDX_Expression  
   | DIMENSION Dimension_Name | Hierarchy_Name  
      , DEFAULT_MEMBER = MDX_Expression  
   | DIMENSION MEMBER MemberName AS  
   [MDX_Expression]  
   [Property_Name = Property_Value[, ...n]]  
  
<create cell calculation clause>::=  
CELL CALCULATION Calculation_Name   
   FOR Set_Expression AS MDX_Expression   
            [ [ CONDITION = 'Logical_Expression' ]   
    | [ DISABLED = { TRUE | FALSE } ]   
    | [ DESCRIPTION =String ]   
    | [ CALCULATION_PASS_NUMBER = Integer]   
    | [ CALCULATION_PASS_DEPTH = Integer]   
    | [ SOLVE_ORDER = Integer]   
    | [ Calculation_Name= Scalar_Expression ], ...n]  

```

将一个新行添加到基础维度表中。
_ParentName_ 除非在根节点新建维度成员，否则提供该维度成员父级名称的有效字符串表达式。
_MemberName_ 提供成员名称的有效字符串表达式。
_Key_Value_ 定义新维度成员键值的有效标量表达式。
_Property_Name_ 代表成员属性的有效多维表达式 (MDX) 标识符。
_Property_Value_ 定义计算成员属性值的有效多维表达式 (MDX) 标量表达式。
如果从可写维度中删除一个维度成员，就会从基础维度表中删除该成员和与其对应的行。
_Cube_Name_ 提供多维数据集名称的有效字符串表达式。
_Member_Name_ 提供成员名称或成员键的有效字符串表达式。
如果未使用 WITH DESCENDANTS 子句，则已删除成员的子级将成为已删除成员父级的子级。 如果使用 WITH DESCENDANTS 子句，则还会删除维度表内的所有后代及其对应的行。
有关删除计算成员、命名集、操作和单元格计算的信息，请参阅 DROP MEMBER Statement (MDX) 、 DROP SET 语句 (MDX) 、 DROP ACTION Statement (MDX) 和 DROP CELL CALCULATION Statement (MDX) 。
该子句更新多维数据集的默认成员，并且在定义默认成员的 MDX 计算脚本中使用。 可以为数据库维度、多维数据集维度或者用户登录名指定默认成员。 还可以在会话期间更改默认成员。
_Dimension_Name_ 提供维度名称的有效字符串。
_MDX_Expression_ 返回单个成员的有效 MDX 表达式。
指定的 MDX 表达式可以为静态或动态。
在基础维度表内修改某行。
_ParentName_ 提供要移动维度成员的新父级名称的有效字符串表达式。
_MemberName_ 提供成员名称的有效字符串表达式。
Unsigned__Integer_ 指定要跳过的级别数的有效数字。
如果指定了 WITH DESCENDANTS 子句，则移动整个树。 如果未指定 WITH DESCENDANTS 子句，则所移动父级的子级将成为所移动成员父级的子级。 移动造成的影响仅仅是在基础维度表中更新了父键列的值。
UPDATE DIMENSION MEMBER 子句可以修改成员的属性以及与成员相关的自定义成员公式。
_MemberName_ 提供成员名称的有效字符串表达式。
_MDX_Expression_ 返回单个成员的有效 MDX 表达式。
_Property_Value_ 定义计算成员属性值的有效 MDX 标量表达式。
有关使用 ALTER CUBE 语句创建单元格计算的详细信息，请参阅 DROP CELL CALCULATION Statement (MDX) 。
1月27日 15时 - 1月27日 15时 


