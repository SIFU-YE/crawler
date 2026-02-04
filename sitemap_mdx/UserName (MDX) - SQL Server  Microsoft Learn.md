#### 通过
# UserName (MDX)
返回当前连接的域名和用户名。
```
  
UserName [ ( ) ]  

```

返回值为以下格式的字符串：
_domain-name\user-name_
下例将返回正在执行查询的用户的用户名。
```
WITH MEMBER Measures.x AS UserName  
SELECT Measures.x ON COLUMNS  
FROM [Adventure Works]  
  

```

1月27日 15时 - 1月27日 15时 


