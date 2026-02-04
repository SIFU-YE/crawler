#### 通过
# Crossjoin (MDX)
返回一个或多个集的叉积。
```
  
Standard syntax  
Crossjoin(Set_Expression1 ,Set_Expression2 [,...n] )  
  
Alternate syntax  
Set_Expression1 * Set_Expression2 [* ...n]  

```

_Set_Expression1_ 返回集的有效多维表达式 (MDX)。
_Set_Expression2_ 返回集的有效多维表达式 (MDX)。
**交叉联接** 函数返回两个或更多个指定集的交叉乘积。 所得集中元组的顺序取决于要联接的集的顺序以及其成员的顺序。 例如，当第一个集由 {x1， x2,...,x _n_} 组成，而第二个集由 {y1， y2， ...， y _n_} 组成时，这些集的交叉乘积为：
{ (x1、y1) 、 (x1、y2) ,..., (x1、y _n_) 、 (x2、y1) 、 (x2、y2) ,...,
(x2、y _n_) ,..., (x _n_ 、y1) 、 (x _n_ 、y2) ,..., (xn、y _n_) }
如果交叉联接中的集由同一维度中不同属性层次结构中的元组组成，此函数将只返回实际存在的那些元组。 有关详细信息，请参阅 MDX (Analysis Services) 中的关键概念 。
以下查询说明在查询的列轴和行轴上使用 Crossjoin 函数的简单示例：
```
SELECT  
[Customer].[Country].Members *  
[Customer].[State-Province].Members  
ON 0,  
Crossjoin(  
[Date].[Calendar Year].Members,  
[Product].[Category].[Category].Members)  
ON 1  
FROM [Adventure Works]  
WHERE Measures.[Internet Sales Amount]  

```

以下示例说明交叉联接同一维度中的不同层次结构时发生的自动筛选：
```
SELECT  
Measures.[Internet Sales Amount]  
ON 0,  
//Only the dates in Calendar Years 2003 and 2004 will be returned here  
Crossjoin(  
{[Date].[Calendar Year].&[2003], [Date].[Calendar Year].&[2004]},  
[Date].[Date].[Date].Members)  
ON 1  
FROM [Adventure Works]  

```

以下三个示例返回相同的结果 - United States 各州的 Internet Sales Amount（按州显示）。 前两个示例使用两个交叉联结语法，第三个示例演示了使用 WHERE 子句返回相同的信息。
```
SELECT CROSSJOIN  
   (  
      {[Customer].[Country].[United States]},  
       [Customer].[State-Province].Members  
   ) ON 0   
FROM [Adventure Works]  
WHERE Measures.[Internet Sales Amount]  

```
```
SELECT   
   [Customer].[Country].[United States] *   
      [Customer].[State-Province].Members  
ON 0   
FROM [Adventure Works]  
WHERE Measures.[Internet Sales Amount]  

```
```
SELECT   
   [Customer].[State-Province].Members  
ON 0   
FROM [Adventure Works]  
WHERE (Measures.[Internet Sales Amount],  
   [Customer].[Country].[United States])  

```

1月27日 15时 - 1月27日 15时 


