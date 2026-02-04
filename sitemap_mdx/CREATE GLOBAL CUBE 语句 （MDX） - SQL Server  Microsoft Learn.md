#### 通过
# MDX 数据定义 - CREATE GLOBAL CUBE
根据服务器上的多维数据集中的子多维数据集创建并填充本地持久化多维数据集。 连接到服务器不需要连接到本地持久化多维数据集。 有关本地多维数据集的详细信息，请参阅 本地多维数据集（Analysis Services - 多维数据）。
```
  
CREATE GLOBAL CUBE local_cube_name STORAGE 'Cube_Location'   
FROM source_cube_name (<param list>)  
  
<param list>::= <param> ,<param list> | <param>  
  
<param>::= <dims list> | <measures list>  
  
<measures list>::= <measure>[, <measures list>]   
  
<dims list>::= <dim def> [, <dims list>]  
  
<measure>::= MEASURE source_cube_name.measure_name [<visibility qualifier>] [AS measure_name]   
  
<dim def>::= <source dim def> | <derived dim def>  
  
<source dim def>::= DIMENSION source_cube_name.dimension_name [<dim flags>] [<visibility qualifier>] [AS dimension_name>] [FROM <dim from clause> ] [<dim content def>]  
  
<dim flags>::= NOT_RELATED_TO_FACTS   
  
<dim from clause>::= < dim DM from clause> | <reg dim from clause>   
  
<dim DM from clause>::= dm_model_name> COLUMN column_name   
  
<dim reg from clause>::= dimension_name  
  
<dim content def>::= ( <level list> [,<grouping list>] [,<member slice list>] [,<default member>] )  
  
<level list>::= <level def> [, <level list>]  
  
<level def>::= LEVEL level_name [<level type> ] [AS level_name] [<level content def>]  
  
<level content def>::= ( <property list> ) | NO_PROPERTIES  
  
<level type>::= GROUPING  
  
<property list>::= <property def> [, <property list>]  
  
<property def>::= PROPERTY property_name   
  
<grouping list>::= <grouping entity> [,<grouping list>]  
  
<grouping entity>::= GROUP group_level_name.group_name (<mixed list>)  
  
<grp mixed list>::= <grp mixed element> [,<grp mixed list>]  
  
<grp mixed element>::= <grouping entity> | <member def>  
  
<member slice list>::= <member list>  
  
<member list>::= <member def> [, <member list>]  
  
<member def>::= MEMBER member_name  
  
<default member>::= DEFAULT_MEMBER AS MDX_expression  
  
<visibility qualifier>::= HIDDEN   

```

local_cube_name 本地多维数据集的名称。
“Cube_Location” 本地持久化多维数据集的名称和路径。
source_cube_name 本地多维数据集所基于的多维数据集的名称。
source_cube_name.measure_name 本地多维数据集中包含的源度量值的完全限定名称。 不允许度量值维度的计算成员。
measure_name 本地多维数据集中度量值的名称。
source_cube_name.dimension_name 本地多维数据集中包含的源维度的完全限定名称。
dimension_name 本地多维数据集中维度的名称。
FROM <dim from 子句> 仅派生维度定义的有效规范。
NOT_RELATED_TO_FACTS 仅派生维度定义的有效规范。
<级别类型> 仅派生维度定义的有效规范。
本地多维数据集根据定义它的度量值和定义进行定义。 有两种类型的维度。
  * 源维度 - 这些维度是属于多个源多维数据集之一的维度
  * 派生维度 - 这些是提供新分析功能的维度。 派生维度可以是基于垂直或水平切片的源维度定义的常规维度，也可以包含维度成员的自定义分组。 派生维度也可以是基于数据挖掘模型的数据挖掘维度。


Dimension 关键字可以引用维度或层次结构。
在本地多维数据集中，可以执行以下任务：
  * 消除源多维数据集中存在的维度
  * 从维度中添加或消除层次结构
  * 消除度量值组或特定度量值


CREATE GLOBAL CUBE 语句遵循以下规则：
  * CREATE GLOBAL CUBE 语句自动将所有命令（如计算度量值或操作）复制到本地多维数据集。 如果命令包含显式引用父多维数据集的多维表达式（MDX）表达式，则本地多维数据集无法运行该命令。 若要防止此问题，在为命令定义 MDX 表达式时，请使用 **CURRENTCUBE** 关键字。 在 MDX 表达式中引用多维数据集时，**CURRENTCUBE** 关键字使用当前多维数据集上下文。
  * 从本地多维数据集文件中的现有全局多维数据集创建的全局多维数据集不能保存在同一本地多维数据集文件中。 例如，创建名为 SalesLocal1 的全局多维数据集，并将此多维数据集保存到 C：\SalesLocal.cub 文件中。 然后连接到 C：\SalesLocal.cub 文件，并创建名为 SalesLocal2 的第二个全局多维数据集。 如果现在尝试将 SalesLocal2 全局多维数据集保存到 C：\SalesLocal.cub 文件，将收到错误。 但是，可以将 SalesLocal2 全局多维数据集保存到其他本地多维数据集文件中。
  * 全局多维数据集不支持不同的计数度量值。 由于包含非重复计数度量值的多维数据集是非累加性的，因此 CREATE GLOBAL CUBE 语句不支持创建或使用非重复计数度量值。
  * 向本地多维数据集添加度量值时，还必须至少包含一个与要添加的度量值相关的维度。
  * 将父子层次结构添加到本地多维数据集时，将忽略父子层次结构上的级别和筛选器，并包含整个父子层次结构。
  * 本地多维数据集不支持成员属性。
  * 不能从透视创建本地多维数据集。
  * 将半累加度量值包含在本地多维数据集中时，适用以下规则：
    * 如果要添加的度量值的 AggregateFunction 属性为 ByAccount，则必须包含 Account 维度。
    * 如果要添加的 AggregateFunction 属性度量值为 FirstChild、LastChild、FirstNonEmpty、LastNonEmpty 或 AverageOfChildren，则必须包含整个 Time 维度。
  * 无法将数据挖掘维度添加到本地多维数据集。
  * 引用维度具体化并添加为常规维度。
  * 当包含多对多维度时，以下规则适用：
    * 必须添加整个多对多维度。
    * 必须添加中间度量值组。
    * 必须将所有维度的整个添加到多对可能关系中涉及的两个度量值组。


以下示例演示如何创建仅包含“经销商销售金额”度量值、“经销商”维度和“日期”维度的 Adventure Works 多维数据集的本地持久版本。
```
CREATE GLOBAL CUBE [LocalReseller]  
   Storage 'C:\LocalAWReseller1.cub'  
   FROM [Adventure Works]  
   (  
      MEASURE  [Adventure Works].[Reseller Sales Amount],  
      DIMENSION [Adventure Works].[Reseller],  
      DIMENSION [Adventure Works].[Date]  
   )  

```

以下示例演示创建本地多维数据集时切片。 创建的全局多维数据集基于按会计年度级别 2005 成员垂直切片的 Adventure Works 多维数据集，并按财政年度和月份级别水平切片。
```
CREATE GLOBAL CUBE [LocalReseller]  
   Storage 'C:\LocalAWReseller2.cub'  
   FROM [Adventure Works]  
   (  
      MEASURE  [Adventure Works].[Reseller Sales Amount],  
      DIMENSION [Adventure Works].[Reseller],  
      DIMENSION [Adventure Works].[Date]  
      (  
LEVEL [Fiscal Year],  
LEVEL [Month],  
MEMBER [Date].[Fiscal].[Fiscal Year].&[2005]  
      )  
   )  

```

MDX 数据定义语句 （MDX） CREATE SESSION CUBE 语句 （MDX）
1月27日 15时 - 1月27日 15时 


