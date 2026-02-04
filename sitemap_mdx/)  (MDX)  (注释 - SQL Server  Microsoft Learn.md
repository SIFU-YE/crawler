#### 通过
# 注释 MDX 双斜杠
表示用户提供的文本。
```
  
// Comment_Text   

```

_Comment_Text_ 包含注释文本的字符串。
注释可以在单独的一行插入，也可以在多维表达式 (MDX) 脚本行的结尾处嵌入，还可以嵌入在 MDX 语句中。 服务器不对注释进行计算。
只将 // 用于单行注释。 用 // 插入的注释由换行符分隔。
注释没有最大长度限制。
下面的示例演示了此运算符的用法。
```
// This member returns the gross profit margin for product types  
// and reseller types crossjoined by year.  
SELECT   
    [Date].[Calendar].[Calendar Year].Members *  
      [Reseller].[Reseller Type].Children ON 0,  
    [Product].[Category].[Category].Members ON 1  
FROM // Select from the Adventure Works cube.  
    [Adventure Works]  
WHERE  
    [Measures].[Gross Profit Margin]  

```

1月27日 15时 - 1月27日 15时 


