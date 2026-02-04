#### 通过
# MDX 数据操作 - DRILLTHROUGH
检索用于在多维数据集中创建指定单元的基础表行。
```
  
DRILLTHROUGH[MAXROWSUnsigned_Integer]   
      <MDX SELECT statement>   
      [RETURNSet_of_Attributes_and_Measures   
            [,Set_of_Attributes_and_Measures ...]  
      ]  

```

_Unsigned_Integer_ 正整数值。
_MDX SELECT 语句_ 任何有效的多维表达式 (MDX) SELECT 语句。
_Set_of_Attributes_and_Measures_ 以逗号分隔的维度属性和度量值列表。
钻取是一种操作，最终用户可通过该操作选择多维数据集中的一个单元，然后在该单元的源数据中检索结果集，以获取更加详细的信息。 默认情况下，钻取结果集来自表行（通过求值来计算选定的多维数据集单元的值）。 如果最终用户要执行钻取操作，则他们的客户端应用程序必须支持此功能。 在 Analysis Services 中，除非查询 ROLAP 分区或维度，否则将直接从 MOLAP 存储检索结果。
钻取安全性基于为多维数据集定义的常规安全选项。 如果无法用 MDX 获取一些数据，钻取也将以同样的方式限制用户。
MDX 语句指定了目标单元。 **MAXROWS** 参数指定的值指示生成的行集应返回的最大行数。
默认情况下，返回的最大行数为 10000 行。 这意味着，如果不指定 **MAXROWS** ，将获得 10，000 行或更少。 如果此值对于方案而言太低，则可以将 **MAXROWS** 设置为更高的数字，例如 `MAXROWS 20000`。 如果整体太低，可以通过更改 **OLAP\Query\DefaultDrillthroughMaxRows** 服务器属性来增加默认值。 有关更改此属性的详细信息，请参阅 Analysis Services 中的服务器属性。
除非另行指定，否则返回的列包括与指定度量值的度量值组相关的所有维度（多对多维度除外）的所有粒度属性。 多维数据集维度带有 $ 前缀，以区分维度和度量值组。 **RETURN** 子句用于指定钻取查询返回的列。 以下函数可以通过 **RETURN** 子句应用于单个属性或度量值。
Name(attribute_name) 返回指定属性成员的名称。
UniqueName(attribute_name) 返回指定属性成员的唯一名称。
Key(attribute_name[, N]) 返回指定属性成员的键，其中 N 指定组合键中的列（如果有的话）。 N 的默认值为 1。
Caption(attribute_name) 返回指定属性成员的标题。
MemberValue(attribute_name) 返回指定属性成员的成员值。
CustomRollup(attribute_name) 返回指定属性成员的自定义汇总表达式。
CustomRollupProperties(attribute_name) 返回指定属性成员的自定义汇总属性。
UnaryOperator(attribute_name) 返回指定属性成员的一元运算符。
以下示例为 2007 年 7 月的经销商销售额度量值指定单元格， (澳大利亚的默认度量值) 。 RETURN 子句指定返回此单元下各项销售的日期、产品型号名称、雇员姓名、销售额、税额和产品成本价值。
```
DRILLTHROUGH  
SELECT  
   ([Date].[Calendar].[Month].[July 2007])  
ON 0   
FROM [Adventure Works]  
WHERE [Geography].[Country].[Australia]  
RETURN   
  [$Date].[Date]  
  ,KEY([$Product].[Model Name])  
  ,NAME([$Employee].[Employee])  
  ,[Reseller Sales].[Reseller Sales Amount]  
  ,[Reseller Sales].[Reseller Tax Amount]  
  ,[Reseller Sales].[Reseller Standard Product Cost]  

```

1月27日 15时 - 1月27日 15时 


