#### 通过
# Error (MDX)
引发错误，根据需要可以选择提供指定的错误消息。
```
  
Error( [ Error_Text ] )  

```

_Error_Text_ 包含要返回的错误消息的有效字符串表达式。
以下查询演示如何在计算度量值中使用 **Error** 函数：
```
WITH MEMBER MEASURES.ERRORDEMO AS ERROR("THIS IS AN ERROR")  
SELECT  
MEASURES.ERRORDEMO ON 0  
FROM [Adventure Works]  

```

1月27日 15时 - 1月27日 15时 


