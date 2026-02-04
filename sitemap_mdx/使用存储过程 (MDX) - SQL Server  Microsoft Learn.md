#### 通过
# 使用存储过程 (MDX)
可以通过编写 .NET 存储过程或用户定义的函数， (MDX) 扩展 Analysis Services 和多维表达式的功能。 有关详细信息，请参阅 ADOMD.NET 服务器编程
当引用或调用存储过程时，应在括号前面指定函数名称。 可以在括号内指定表达式（称为“参数”），以提供要传递给参数的数据。 调用函数时，必须为所有参数提供参数值，并且必须按照用户定义函数中定义的相同参数顺序指定参数值。
以下示例查询假定在 Analysis Services 服务器上注册了名为 SampleAssembly 的程序集：
```
SELECT SampleAssembly.RandomSample([Geography].[State-Province].Members, 5) on ROWS,   
[Date].[Calendar].[Calendar Year] on COLUMNS  
FROM [Adventure Works]  
WHERE [Measures].[Reseller Freight Cost]  

```

_存储过程_ 是 Analysis Services 中用于这些类型函数的术语。 早期版本的 Analysis Services 将这些类型的函数称为 _用户定义的函数_ 。
Analysis Services 同时支持 COM 和 CLR 程序集。 建议使用 CLR 程序集，因为 CLR 程序集具有增强的安全性。 如果服务器上安装了 Microsoft Office Excel，也可以使用 Excel 功能。
Microsoft Visual Basic for Applications (VBA) COM 程序集是自动注册的。
1月27日 15时 - 1月27日 15时 


