#### 通过
# 使用元组函数
元组函数从集中检索元组，或者通过解析元组的字符串表示形式来检索元组。
元组函数（如成员函数和 set 函数）对于协商 Analysis Services 中的多维结构至关重要。
MDX 中有三个元组函数： Current (MDX) 、 Item (元组) (MDX)  和 StrToTuple (MDX) 。 以下示例查询说明如何使用这三个函数：
```
WITH  
//Creates a set of tuples consisting of Years and Countries  
SET MyTuples AS  [Date].[Calendar Year].[Calendar Year].MEMBERS * [Customer].[Country].[Country].MEMBERS  
//Returns a string representation of that set using the Current and Generate functions  
MEMBER MEASURES.CURRENTDEMO AS GENERATE(MyTuples, TUPLETOSTR(MyTuples.CURRENT), ", ")  
//Retrieves the fourth tuple from that set and displays it as a string  
MEMBER MEASURES.ITEMDEMO AS TUPLETOSTR(MyTuples.ITEM(3))  
//Creates a tuple consisting of the measure Internet Sales Amount and the country Australia from a string  
MEMBER MEASURES.STRTOTUPLEDEMO AS STRTOTUPLE("([Measures].[Internet Sales Amount]" + ", [Customer].[Country].&[Australia])")  
SELECT{MEASURES.CURRENTDEMO,MEASURES.ITEMDEMO,MEASURES.STRTOTUPLEDEMO} ON COLUMNS  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


