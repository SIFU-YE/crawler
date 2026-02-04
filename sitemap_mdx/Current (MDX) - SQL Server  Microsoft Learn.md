#### 通过
# Current (MDX)
返回迭代过程中集内的当前元组。
```
  
Set_Expression.Current   

```

_Set_Expression_ 返回集的有效多维表达式 (MDX)。
迭代过程的每一步中所操作的元组就是当前元组。 **Current** 函数返回该元组。 该函数仅在对集执行迭代的过程中有效。
循环访问集的 MDX 函数包括 Generate 函数。
该函数只能使用已命名的集（使用集别名或定义命名集）。
以下示例演示如何在 **Generate** 中使用 **Current** 函数：
```
WITH  
//Creates a set of tuples consisting of all Calendar Years crossjoined with  
//all Product Categories  
SET MyTuples AS CROSSJOIN(  
[Date].[Calendar Year].[Calendar Year].MEMBERS,  
[Product].[Category].[Category].MEMBERS)  
//Iterates through each tuple in the set and returns the name of the Calendar  
//Year in each tuple  
MEMBER MEASURES.CURRENTDEMO AS  
GENERATE(MyTuples, MyTuples.CURRENT.ITEM(0).NAME, ", ")  
SELECT MEASURES.CURRENTDEMO ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


