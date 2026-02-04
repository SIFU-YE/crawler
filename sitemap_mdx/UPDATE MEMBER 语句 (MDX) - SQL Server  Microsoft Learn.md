#### 通过
# MDX 数据定义 - UPDATE MEMBER
更新现有的计算成员。
```
  
UPDATE MEMBER Cube_Name.Member_Name   
   AS MDX_Expression  
      [,Property_Name = Property_Value, ...n]  
......[,SCOPE_ISOLATION = CUBE]  

```

_Cube_Name_ 一个有效的字符串，用于指定包含该成员的多维数据集的名称。
_Member_Name_ 指定现有成员名称的有效字符串。
_MDX_Expression_ 代表该成员更新目标的有效的多维表达式 (MDX) 表达式。
_Property_Name_ 指定计算成员属性名称的有效字符串。
_Property_Value_ 指定计算成员属性值的有效标量表达式。
UPDATE MEMBER 语句在保留此成员相对于其他计算的优先的同时，更新现有计算成员。 因此，您不能使用 UPDATE MEMBER 语句来更改 SOLVEORDER。
UPDATE MEMBER 语句不能在多维数据集的 MDX 脚本中指定。
指定当前连接的多维数据集以外的多维数据集将导致错误。 因此，应使用 CURRENTCUBE 来代替多维数据集名称，以表示当前的多维数据集。
有关 OLE DB 定义的成员属性的详细信息，请参阅 OLE DB 文档。
每个成员都有一组默认属性。 下表列出了这些默认属性。
FORMAT_STRING | 客户端应用程序可用于显示单元格值的 Office 样式格式字符串。  
---|---  
VISIBLE | 指示计算成员在架构行集中是否可见的值。 可以使用 AddCalculatedMembers 函数将可见的计算成员添加到集中。 非零值表示计算成员可见。 此属性的默认值为 _Visible_ 。 不可见的计算成员通常用作更复杂的计算成员过程的中间步骤。 这些计算成员也可以由其他类型的成员（如度量值）引用。  
NON_EMPTY_BEHAVIOR | 解析空单元时，MDX 用来确定计算成员的行为的度量值或集。  
CAPTION | 指定客户端应用程序用来显示成员的标题的字符串值。  
DISPLAY_FOLDER | 指定显示文件夹的路径的字符串值，客户端应用程序将在此处显示成员。 文件夹级别的分隔符由客户端应用程序定义。 对于 Analysis Services 提供的工具和客户端，反斜杠 (\\) 作为级别分隔符。 若要为定义的成员提供多个显示文件夹，请使用分号 (;) 分隔文件夹。  
ASSOCIATED_MEASURE_GROUP | 与此成员关联的度量值组的名称。  
DROP MEMBER 语句 (MDX) CREATE MEMBER 语句 (MDX) MDX 数据定义语句 (MDX)
1月27日 15时 - 1月27日 15时 


