#### 通过
# Cousin (MDX)
返回与指定的子成员在父成员下方具有相同的相对位置的子成员。
```
  
Cousin( Member_Expression , Ancestor_Member_Expression )  

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
_Ancestor_Member_Expression_ 返回祖先成员的有效多维表达式 (MDX) 成员表达式。
此函数按各级别内的成员的顺序和位置进行操作。 如果有两个层次结构，第一个层次结构有四个级别，第二个层次结构有五个级别，则第一个层次结构的第三个级别与第二个层次结构的第三个级别是同级。
下面的示例根据 2002 会计年度第四季度在 2003 会计年度中年级别上的祖先检索它的同级。 检索到的同级是 2003 会计年度第四季度。
```
SELECT Cousin   
   ( [Date].[Fiscal].[Fiscal Quarter].[Q4 FY 2002],  
     [Date].[Fiscal].[FY 2003]  
   ) ON 0  
FROM [Adventure Works]  

```

下面的示例根据 2002 会计年度 7 月在 2004 会计年度第二季度中季度级别上的祖先检索它的同级。 检索到的同级是 2003 年 10 月。
```
SELECT Cousin   
   ([Date].[Fiscal].[Month].[July 2002] ,  
    [Date].[Fiscal].[Fiscal Quarter].[Q2 FY 2004]  
   ) ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


