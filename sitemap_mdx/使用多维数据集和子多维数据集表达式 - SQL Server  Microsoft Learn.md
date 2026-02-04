#### 通过
# 使用多维数据集和子多维数据集表达式
在多维表达式（MDX）语句中使用多维数据集和子多维数据集表达式来定义、操作或检索多维数据集或子多维数据集中的数据。
多维数据集表达式包含多维数据集标识符或 CURRENTCUBE 关键字，因此只能是简单的表达式。 许多 MDX 语句使用 CURRENTCUBE 关键字来标识当前多维数据集上下文，而无需多维数据集标识符。
多维数据集标识符在 MDX 语句的 BNF 表示法说明中显示为 _Cube_Name_ 。
多维数据集表达式可能出现在多个位置。 在 MDX SELECT 语句中，它们指定要从中检索数据的多维数据集。 在以下示例查询中，表达式 [Adventure Works] 引用该名称的多维数据集：
```
SELECT [Measures].[Internet Sales Amount] ON COLUMNS  
FROM [Adventure Works]  

```

在 CREATE MEMBER 语句中，多维数据集表达式指定要创建的计算成员显示的多维数据集。 在以下示例中，该语句针对 Adventure Works 多维数据集的“度量值”维度创建计算度量值：
`CREATE MEMBER [Adventure Works].[Measures].[Test] AS 1`
在 MDX 脚本中使用 CREATE MEMBER 语句时，可以将多维数据集的名称替换为 CURRENTCUBE 关键字，因为要在其中创建计算成员的多维数据集必须与 MDX 脚本所属的多维数据集相同，如以下示例所示：
`CREATE MEMBER CURRENTCUBE.[Measures].[Test] AS 1;`
这样做可以更轻松地将计算成员定义从一个多维数据集复制并粘贴到另一个多维数据集，因为多维数据集的名称不再硬编码。
## SubCube 表达式
子多维数据集表达式可以包含子多维数据集标识符或返回子多维数据集的 MDX 语句。 如果子多维数据集表达式包含子多维数据集标识符，它将是一个简单的表达式。 如果它包含返回子多维数据集的 MDX 语句，则它是一个复杂语句。 例如，MDX SELECT 语句返回一个子多维数据集，可用于允许子多维数据集表达式的位置，如以下示例所示：
```
SELECT [Measures].MEMBERS ON COLUMNS,  
[Date].[Calendar Year].MEMBERS ON ROWS  
FROM  
(SELECT [Measures].[Internet Sales Amount] ON COLUMNS,  
[Date].[Calendar Year].&[2004] ON ROWS  
FROM [Adventure Works])  

```

FROM 子句中 SELECT 语句的这种用法也称为子选。
遇到子多维数据集表达式的另一个常见方案是在 MDX 脚本中进行作用域分配时。 在下面的示例中，SCOPE 语句用于将赋值限制为包含 [Measures] 的子多维数据集。[Internet 销售金额]：
```
SCOPE([Measures].[Internet Sales Amount]);  
This=1;  
END SCOPE;  

```

子多维数据集标识符显示为 _Subcube_Name_ 。 MDX 语句的 BNF 表示法说明。
基本 MDX 查询 （MDX） 在 MDX （MDX） 生成子多维数据集 CREATE SUBCUBE 语句 （MDX） 表达式 （MDX） SCOPE 语句 （MDX）
1月27日 15时 - 1月27日 15时 


