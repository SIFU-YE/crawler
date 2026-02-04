#### 通过
# 标识符 (MDX)
标识符是 Analysis Services 对象的名称。 每个对象都可以且必须具有标识符。 这些对象包括多维数据集、维度、层次结构、级别、成员等等。 可以使用对象的标识符在多维表达式 (MDX) 语句中引用对象。
根据命名对象的方式，对象标识符可以是常规标识符，也可以是分隔标识符。
常规标识符和带分隔符的标识符必须包含 1 到 100 个字符。
常规标识符是符合成为常规标识符的下列格式规则的对象名称。 常规标识符可以和分隔符一起使用，也可以不和分隔符一起使用。
  1. 第一个字符必须是下列字符之一：
     * Unicode Standard 2.0 定义的字母。 除了其他语言的字母字符外，Unicode 定义的字母还包括从 a 到 z 以及从 A 到 Z 的拉丁字符。
     * 下划线 (_) 。
  2. 后续字符可以是：
     * Unicode Standard 2.0 中定义的字母。
     * 基本拉丁字符或其他国家/地区字符中的十进制数字。
     * 下划线 (_) 。
  3. 标识符一定不能是 MDX 保留关键字。 MDX 中的保留关键字区分大小写。 有关详细信息，请参阅 保留关键字 (MDX 语法) 。
  4. 不允许嵌入空格或特殊字符。


在以下 MDX 语句中，标识符 `Measures`、`Product` 和 `Style` 都符合常规标识符的格式规则。 这些常规标识符不需要使用分隔符。
```
SELECT Measures.MEMBERS ON COLUMNS,  
Product.Style.CHILDREN ON ROWS  
FROM [Adventure Works]  
  

```

虽然没有要求，但您也可以将分隔符和常规标识符一起使用。 在以下 MDX 语句中，通过使用方括号正确地分隔了常规标识符 `Measures`、`Product` 和 `Style`。
```
SELECT [Measures].MEMBERS ON COLUMNS,  
[Product].[Style].CHILDREN ON ROWS  
FROM [Adventure Works]  
  

```

不符合成为常规标识符的格式规则的标识符必须始终使用方括号 ([]) 进行分隔。
分隔符仅用于标识符。 无论关键字是否在 Analysis Services 中标记为保留，分隔符都不能用于关键字。
下列情况下需要使用分隔标识符：
  * 当对象的名称或名称中的一部分使用保留关键字时。
建议不要将保留关键字用作对象名称。 从早期版本的 Analysis Services 升级的数据库可能包含标识符，这些标识符包含早期版本中未保留但现已保留的单词。 必须先更改对象的标识符，才能使用分隔标识符引用对象。
  * 当对象的名称使用未被列为限定标识符的字符时。
Analysis Services 允许带分隔符的标识符使用当前代码页中的任何字符。 但是，不加选择地在对象名称中使用特殊字符会使 MDX 语句和脚本难以读取和维护。


分隔标识符的主体可以包含当前代码页中的字符（包括分隔符本身）的任意组合。 如果分隔标识符的主体包含分隔符，则需进行特殊处理：
  * 如果标识符的主体只包含左方括号 ([)，则无需进行额外处理。
  * 如果标识符的主体包含一个右方括号 (])，则必须指定两个右方括号 (]])。


在以下假设 MDX 语句中，`Sales Volume`、`Sales Cube` 和 `select` 都是分隔标识符：
```
-- The [Sales Volume] and [Sales Cube] identifiers contain a space.  
SELECT Measures.[Sales Volume]  
FROM [Sales Cube]  
WHERE Product.[select]  
-- The [select] identifier is a reserved keyword.  

```

在下面的这个示例中，对象的名称是 `Total Profit [Domestic]`。 若要引用此对象，必须使用以下分隔标识符：
`[Total Profit [Domestic]]]`
请注意，不必更改 `Domestic` 前面的左方括号来创建分隔标识符。 但是，必须将 `Domestic` 后面的右方括号替换为两个右方括号。
使用限定对象名称时，可能需要分隔组成对象名称的多个标识符。 例如，需要分隔以下代码中的 Front Brakes 标识符。
SELECT [Measures].MEMBERS ON COLUMNS,
[Product].[Product].[Front Brakes] ON ROWS
FROM [Adventure Works]
此外，还分隔了上一示例中的 Measures 标识符，以说明分隔多个标识符的情况。
MDX 语言参考 (MDX) MDX 查询基础知识 (Analysis Services) MDX 语法元素 (MDX)
1月27日 15时 - 1月27日 15时 


