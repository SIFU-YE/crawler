#### 通过
# Levels (MDX)
返回由数值表达式指定在维度或层次结构中的位置的级别，或返回由字符串表达式指定名称的级别。
```
  
Numeric expression syntax  
Hierarchy_Expression.Levels( Level_Number )  
  
String expression syntax  
Hierarchy_Expression.Levels( Level_Name )  

```

_Hierarchy_Expression_ 返回层次结构的有效多维表达式 (MDX)。
_Level_Number_ 指定级别号的有效数值表达式。
_Level_Name_ 指定级别名称的有效字符串表达式。
如果指定了级别编号， **则 Levels** 函数将返回与指定的从零开始的位置关联的级别。
如果指定了级别名称， **Levels** 函数将返回指定的级别。
将字符串表达式语法用于用户定义的函数。
以下示例演示了每个 **Levels** 函数语法。
以下示例返回国家（地区）级别：
```
SELECT [Geography].[Geography].Levels(1) ON 0  
FROM [Adventure Works]  

```

以下示例返回国家（地区）级别：
```
SELECT [Geography].[Geography].Levels('Country') ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


