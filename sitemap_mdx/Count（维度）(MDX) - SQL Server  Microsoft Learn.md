#### 通过
# Count（维度）(MDX)
返回多维数据集中的层次结构数。
```
  
Dimensions.Count   

```

返回多维数据集中的层次结构数，包括 `[Measures].[Measures]` 层次结构。
下面的示例返回 Adventure Works 多维数据集中的层次结构数。
```
WITH MEMBER measures.X AS  
  dimensions.count   
SELECT Measures.X ON 0  
FROM [Adventure Works]  

```

Count（元组）(MDX) Count（层次结构级别）(MDX) Count（集）(MDX) MDX 函数参考 (MDX)
1月27日 15时 - 1月27日 15时 


