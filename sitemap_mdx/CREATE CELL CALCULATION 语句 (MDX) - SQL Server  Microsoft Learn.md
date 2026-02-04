#### 通过
# MDX 数据定义 - CREATE CELL CALCULATION
创建计算，以便通过多维表达式 (MDX) 对多维数据集中的一组指定元组求值。
```
  
[WITH <CELL CALCULATION clause> Calculation_Name  
   [,WITH <CELL CALCULATION clause> Calculation_Name...n]  
CREATE CELL CALCULATION CURRENTCUBE | Cube_Name.Calculation_Name   
  
<CELL CALCULATION clause> ::=  
   FOR Set_Expression AS 'MDX_Expression'   
      [ [ CONDITION = 'Logical_Expression' ]   
    | [ DISABLED = { TRUE | FALSE } ]   
    | [ DESCRIPTION =String ]   
    | [ CALCULATION_PASS_NUMBER = Integer]   
    | [ CALCULATION_PASS_DEPTH = Integer]   
    | [ SOLVE_ORDER = Integer]   
    | [ Calculation_Name= Scalar_Expression ], ...n]  

```

_Cube_Name_ 提供多维数据集名称的有效字符串。
_Calculation_Name_ 一个提供单元计算名称的有效字符串。
_Set_Expression_ 返回一个集的有效 MDX 表达式。
_字符串_ 有效的字符串值。
_MDX_Expression_ 有效的 MDX 表达式。
_Logical_Expression_ 有效的 MDX 逻辑表达式。
_整数_ 有效的整数值。
_Calculation_Name_ 一个提供单元计算属性名称的有效字符串。
_Scalar_Expression_ 有效的 MDX 标量表达式。
通过使用计算单元，客户端应用程序就可以指定一组特定单元的汇总值，而不必像在自定义汇总公式或计算成员中一样指定所有单元的汇总值。 例如，可以指定 `{[Canada],[Time].[2000]}` 所定义的集中的任意单元都允许包含通过公式定义的值。 不在此集中的其他任何单元都按正常方式计算。
巴科斯-诺尔范式 (BNF) 的 `{*(<comment> | <whitespace> | <newline>)}` 将分析为 `{*}`，以实现向后兼容。
创建会话作用域的计算单元 创建查询作用域的单元计算 (MDX) 在 MDX 中生成单元计算 (MDX) 使用单元属性 (MDX) FORMAT_STRING 内容 (MDX) FORE_COLOR 和 BACK_COLOR 内容 (MDX) MDX 数据定义语句 (MDX)
1月27日 15时 - 1月27日 15时 


