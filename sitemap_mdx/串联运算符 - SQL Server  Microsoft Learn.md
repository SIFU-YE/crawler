#### 通过
# 串联运算符
串联运算符为加号 (+)。 可以将两个或更多个字符串合并或串联成一个字符串， 还可以串联二进制字符串。
下列代码是串联运算符的一个示例，在此示例中，用串联运算符将产品名称与产品的唯一名称连接起来：
```
WITH MEMBER Measures.ProductName AS   
   Product.Product.CurrentMember.Name + " (" + Product.Product.CurrentMember.UniqueName + ")"  
SELECT   
   {Measures.ProductName} ON COLUMNS,  
   Product.Product.Members ON ROWS  
FROM [Adventure Works]  

```

当串联中使用的字符串具有相同的排序规则时，生成的串联字符串具有与输入字符串相同的排序规则。 当串联中使用的字符串具有不同的排序规则时，生成的串联字符串的排序规则由排序规则的优先顺序规则确定。 有关详细信息，请参阅 Analysis Services) (语言和排序规则 。
1月27日 15时 - 1月27日 15时 


