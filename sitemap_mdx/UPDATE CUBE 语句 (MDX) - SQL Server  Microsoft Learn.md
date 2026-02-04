#### 通过
# MDX 数据操作 - UPDATE CUBE
UPDATE CUBE 语句用于将数据写回到多维数据集中的任何单元中，该多维数据集使用 SUM 聚合而聚合到其父级。 有关更多说明和示例，请参阅以下博客文章中的“了解分配”： 使用 Analysis Services 构建写回应用程序 (博客) 。
```
  
UPDATE [ CUBE ] Cube_Name   
   SET   
            <update clause>   
           [, <update clause> ...n ]  
  
<update clause> ::=   
      Tuple_Expression[.VALUE]= New_Value  
      [   
        USE_EQUAL_ALLOCATION   
        | USE_EQUAL_INCREMENT   
        | USE_WEIGHTED_ALLOCATION [ BY Weight_Expression]   
        | USE_WEIGHTED_INCREMENT [ BY Weight_Expression]  
      ]  

```

_Cube_Name_ 提供多维数据集名称的有效字符串。
_Tuple_Expression_ 返回元组的有效多维表达式 (MDX)。
_New_Value_ 有效的数值表达式。
_Weight_Expression_ 有效的 MDX（多维表达式）数值表达式，将返回介于 0 到 1 之间的一个十进制值。
您可以更新多维数据集中的指定叶单元或非叶单元的值，并且可以根据需要跨依赖叶单元为指定非叶单元分配值。 元组表达式指定的单元可以是多维空间中的任意有效单元（即该单元不一定是叶单元）。 但是，单元必须使用 Sum 聚合函数进行聚合，并且不得在用于标识单元格的元组中包括计算成员。
将 **UPDATE CUBE** 语句视为一个子例程可能会有所帮助，该子例程将自动生成一系列单独的单元格写回操作，这些操作将汇总到指定的总和中叶和非叶单元格。
下面是分配方法的说明。
**USE_EQUAL_ALLOCATION：** 将基于以下表达式为参与更新单元格的每个叶单元格分配一个相等的值。
```
<leaf cell value> =   
<New Value> / Count(leaf cells that are contained in <tuple>)  

```

**USE_EQUAL_INCREMENT：** 根据以下表达式，将更改对更新单元格做出贡献的每个叶单元格。
```
<leaf cell value> = <leaf cell value> +   
(<New Value > - <existing value>) /  
Count(leaf cells contained in <tuple>)  

```

**USE_WEIGHTED_ALLOCATION：** 将为每个参与更新单元格的叶单元格分配一个基于以下表达式的相等值。
```
<leaf cell value> = < New Value> * Weight_Expression  

```

**USE_WEIGHTED_INCREMENT：** 根据以下表达式，将更改对更新单元格做出贡献的每个叶单元格。
```
<leaf cell value> = <leaf cell value> +   
(<New Value> - <existing value>)  * Weight_Expression  

```

如果未指定权重表达式， **UPDATE CUBE** 语句将隐式使用以下表达式。
```
Weight_Expression = <leaf cell value> / <existing value>  

```

权重表达式应表示为 0 到 1 之间的一个小数值。 此值指定希望分配到受分配影响的叶单元的分配值比率。 客户端应用程序程序员负责创建其汇总聚合值等于此表达式分配值的一系列表达式。
客户端应用程序必须同时考虑所有维度的分配，以避免可能产生的意外结果，包括不正确的汇总值或不一致的数据。
对于事务性目的，每个 **UPDATE CUBE** 分配都应被视为原子分配。 这意味着，如果任意一个分配操作由于任何原因（例如公式中出现错误或存在安全冲突）失败，则整个 UPDATE CUBE 操作都将失败。 在处理各个分配操作的计算之前，会对数据拍摄快照以确保所得到的计算是正确的。
当用于包含整数的度量值时，USE_WEIGHTED_ALLOCATION 方法可能会由于不断地进行舍入而得出不准确的结果。
如果更新的单元不相互重叠，则 **Update Isolation Level** 连接字符串属性可用于提高 UPDATE CUBE 的性能。
1月27日 15时 - 1月27日 15时 


