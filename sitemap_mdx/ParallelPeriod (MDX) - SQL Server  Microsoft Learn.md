#### 通过
# ParallelPeriod (MDX)
返回上一期间中与指定成员具有相同的相对位置的成员。
```
  
ParallelPeriod( [ Level_Expression [ ,Index [ , Member_Expression ] ] ] )  

```

_Level_Expression_ 返回级别的有效多维表达式 (MDX)。
_Index_ 指定要滞后的并行期间数的有效数值表达式。
_Member_Expression_ 返回成员的有效多维表达式 (MDX)。
虽然与 Cousin 函数类似， **但 ParallelPeriod** 函数与时序关系更密切。 **ParallelPeriod** 函数采用指定级别的指定成员的上级，查找具有指定延迟的上级同级，最后返回指定成员在同级后代中的并行周期。
**ParallelPeriod** 函数具有以下默认值：
  * 如果未指定级别表达式和成员表达式，则默认成员值是第一个维度上第一个层次结构的当前成员，度量值组中的类型为 _Time_ 。
  * 如果指定了级别表达式，但未指定成员表达式，则默认成员值为 _Level_Expression_ 。**Hierarchy.CurrentMember** 。
  * 默认索引值为 1。
  * 默认级别为指定成员的父级别。


**ParallelPeriod** 函数等效于以下 MDX 语句：
`Cousin(Member_Expression, Ancestor(Member_Expression, Level_Expression) .Lag(Numeric_Expression))`
下面的示例以季度级别为基准并以三个期间为间隔，返回了 October 2003（2003 年 10 月）的并行期间，即 2003 年 1 月。
```
SELECT ParallelPeriod ([Date].[Calendar].[Calendar Quarter]  
   , 3  
   , [Date].[Calendar].[Month].[October 2003])  
   ON 0  
   FROM [Adventure Works]  

```

下面的示例以半期级别为基准并以三个期间为间隔，返回了 October 2003（2002 年 10 月）的并行期间，即 2002 年 4 月。
```
SELECT ParallelPeriod ([Date].[Calendar].[Calendar Semester]  
   , 3  
   , [Date].[Calendar].[Month].[October 2003])  
   ON 0  
   FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


