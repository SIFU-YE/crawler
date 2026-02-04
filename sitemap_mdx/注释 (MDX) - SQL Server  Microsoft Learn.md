#### 通过
# 注释 (MDX)
表示用户提供的注释文本。
```
  
/* Comment_Text */      

```

_Comment_Text_ 包含注释文本的字符串。
服务器不计算注释字符 /* 和 */之间的文本。 注释可以插入到单独一行中，也可以插入到多维表达式 (MDX) 语句中。 多行的注释必须用 /* 和 */ 指明。
注释没有最大长度限制。 注释可以嵌套，例如，`/* Test /*Comment*/ Text*/` 就是一个嵌套注释的例子。
下面的示例演示了此运算符的用法。
```
/* This member returns the gross profit margin for product types  
  and reseller types crossjoined by year. */  
SELECT   
    [Date].[Calendar].[Calendar Year].Members *  
    [Reseller].[Reseller Type].Children ON 0,  
    [Product].[Category].[Category].Members ON 1  
FROM /* Select from the Adventure Works cube. */  
    [Adventure Works]  
WHERE  
    [Measures].[Gross Profit Margin]  

```

) (MDX) (注释  -- （注释）(MDX) MDX 运算符参考 (MDX)
1月27日 15时 - 1月27日 15时 


