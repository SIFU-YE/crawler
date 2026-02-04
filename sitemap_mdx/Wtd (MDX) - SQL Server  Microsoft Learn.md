#### 通过
# Wtd (MDX)
按照时间维度中的周级别的约束，从给定成员所在的级别返回一组同级成员，从第一个同级成员开始到给定成员为止。
```
  
Wtd( [ Member_Expression ] )  

```

_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
如果未指定成员表达式，则默认值为第一个层次结构的当前成员，其级别为“周”的第一个维度中，第一个维度的类型为 Time (**Time.CurrentMember**) 。
**Wtd** 函数是 PeriodsToDate 函数的快捷方式函数，其中级别设置为 _Weeks_ 。 也就是说，`Wtd(Member_Expression)` 等效于 `PeriodsToDate(Week_Level_Expression,Member_Expression)`。
Qtd (MDX) Mtd (MDX) Ytd (MDX) MDX 函数参考 (MDX)
1月27日 15时 - 1月27日 15时 


