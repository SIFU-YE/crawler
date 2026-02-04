#### 通过
# 使用成员表达式
成员表达式包含成员标识符、成员函数或可转换为成员的表达式。
成员标识符可以有多种不同的格式。 成员标识符的最简单形式包括成员的名称。 例如：
```
SELECT Amount ON 0  
FROM [Adventure Works]  
  

```

但是，如果不同层次结构中有多个具有相同名称的成员，则无法确定查询将返回的成员。 例如，以下查询请求名为 [CY 2004] 的成员的数据。 查询成功执行，但 Adventure Works 多维数据集中至少有六个成员具有该名称：
```
SELECT [CY 2004] ON 0  
FROM [Adventure Works]  
  

```

因此，最可靠的成员标识符形式是成员的唯一名称，这可以保证标识多维数据集中的特定成员。 Analysis Services 可以通过多种方式生成唯一名称，但唯一名称始终由至少两个标识符组成：维度名称和成员名称或成员键。 唯一名称以以下格式显示：
```
  
Dimension_Name  
.[Hierarchy_Name.] [[{Member_Name | &Member_Key}.]... ] {Member_Name | &Member_Key}  
  

```

下面是 Adventure Works 多维数据集中成员唯一名称的一些示例：
```
[Measures].[Amount]  
[Date].[Calendar Year].&[2004]  
[Date].[Calendar].[Calendar Quarter].&[2004]&[1]  
[Employee].[Employees].&[112]  
[Product].[Product Categories].[All Products]  
  

```

存在许多返回成员的 MDX 函数。 有关完整列表，请参阅 MDX 函数引用 （MDX）
有关成员名称和成员密钥的详细信息，请参阅 使用成员、元组和集（MDX）。
1月27日 15时 - 1月27日 15时 


