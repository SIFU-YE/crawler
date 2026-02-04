#### 通过
# MDX 脚本 - IF
如果条件为真，则执行语句。
```
  
IF expression THEN assignment END IF  

```

_expression_ 计算结果为返回 True 或 False 的布尔值的多维表达式 (MDX)。
_assignment_ 为子多维数据集或计算属性赋值的 MDX 表达式。
将 IF 语句用于控制流，这与 IIf (MDX)  函数和 CASE 语句 (MDX)  不同，后者只能用于返回值或对象。
在以下示例中，作用域限制在 Customers 维度中 Customers Geography 层次结构的 Country 级别。 如果当前度量值为 Internet Sales Amount，则 Internet Sales Amount 设置为 10：
```
SCOPE ([Customer].[Customer Geography].[Country].MEMBERS);  
IF Measures.CurrentMember IS [Measures].[Internet Sales Amount] THEN this = 10 END IF;  

```

`END SCOPE`;
1月27日 15时 - 1月27日 15时 


