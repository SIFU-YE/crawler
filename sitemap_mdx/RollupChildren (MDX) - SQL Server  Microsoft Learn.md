#### 通过
# RollupChildren (MDX)
使用指定的一元运算符，通过汇总指定成员的子成员的值，从而返回所生成的值。
```
  
RollupChildren(Member_Expression, Unary_Operator)   

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
_Unary_Operator_ 指定一元运算符的有效字符串表达式。
**RollupChildren** 函数使用指定的一元运算符汇总指定成员的子级的值。
下表说明了可用于此函数的有效一元运算符。
total = total + current child  
---  
总额 = 总额 - 当前子级  
total = total * current child  
total = total / current child  
total = (total / current child) * 100  
不在汇总结果中使用子成员。 子成员的值将被忽略。  
如果成员属性中的运算符未显示在列表中，则会发生错误。 求值顺序取决于同级的顺序，而不是运算符的优先顺序。
下例使用名为“Alternate Rollup Operator”的成员属性（包含一元运算符的备用值）以备用方式汇总 Account（帐户）维度中 Net Profit（净利润）层次结构的子成员。 该成员属性不在 Adventure Works 多维数据集中，但是可以创建。 在预算应用程序中可以使用 **RollupChildren** 函数的这种用法进行模拟分析。
```
RollupChildren  
   ( [Account].[Net Profit]  
   , [Account].CurrentMember.Properties ('Alternate Rollup Operator') )  

```

1月27日 15时 - 1月27日 15时 


