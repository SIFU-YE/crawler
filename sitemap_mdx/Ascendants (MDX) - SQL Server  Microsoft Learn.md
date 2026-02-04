#### 通过
# Ascendants (MDX)
返回指定成员的祖先集（包含该成员本身）。
```
  
Ascendants(Member_Expression)  

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
**Ascendants** 函数返回成员的所有上级，从成员本身到成员层次结构的顶部;更具体地说，它会对指定成员的层次结构执行后序遍历，然后返回与该成员相关的所有升序成员，包括一个集中的自身。 这与 上级 函数形成鲜明对比，后者在特定级别返回特定的升级成员或上级。
以下示例从 **Adventure Works** 多维数据集返回该`[Sales Territory].[Northwest]`成员的经销商订单计数以及该成员的所有下级。 **Ascendants** 函数构造包含 ROWS 轴的成员`[Sales Territory].[Northwest]`及其升序的集。
```
SELECT  
   Measures.[Reseller Order Count] ON COLUMNS,  
   Order(  
      Ascendants(  
         [Sales Territory].[Northwest]  
      ),  
      DESC  
   ) ON ROWS  
FROM  
   [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


