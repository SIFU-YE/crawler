
会话页面以XML的方式显示当前服务器上所有的会话信息，并列出各个会话中已经保存的会话属性（sessionAttribute）。可以通过该页面列出的会话信息确定是否存在存内泄漏（即资源没有正常释放，导致会话属性一直增加）。
会话信息中相关节点属性说明如下：
Sessions | Count | 会话总数  
---|---|---  
maxMemory | JVM最大可以申请的内存数  
totalMemory | JVM当前已经申请的内存数  
freeMemory | JVM当前空闲的内存数  
Session（会话） | 会话ID  
maxInactiveInterval | 最大允许空闲的时间（秒）  
最后访问的客户端IP地址  
user | Smartbi登录用户名，NotLogin表示未登录  
Item（属性） | name | 属性名称  
className | 属性类型  
