
  *     *     * 

## 应用说明
演示基于SQL2008的多维数据源和基于mondrian的多维数据源，实现数据显示当前年及前后两年的效果：通过多维分析的自定义命名集实现。
下面以Cube 【Sales】为例，演示如何使用自定义命名集实现当前年及前后两年分析。
## 实现方案
### SQL2008多维数据源
1、新建多维分析。选择Cube 【Sales】构建多维分析。其中行区选择"时间"。
2、sql2008当前年及前后两年。在左侧资源树的【自定义命名集】>【全局】下新建一个全局自定义命名集。
在其MDX表达式中输入如下：
`{StrToMember(``"[Time].["` `+ trim(str(``int``(``year``(now())) )) +``"年]"``).PrevMember.PrevMember,StrToMember(``"[Time].["``+trim(str(``int``(``year``(now()))))+``"年]"``).PrevMember,StrToMember(``"[Time].["``+trim(str(``int``(``year``(now()))))+``"年]"``),StrToMember(``"[Time].["``+trim(str(``int``(``year``(now()))))+``"年]"``).NextMember,StrToMember(``"[Time].["``+trim(str(``int``(``year``(now()))))+``"年]"``).NextMember.NextMember}`  
---  
具体设置如下图： 
### Mondrian多维数据源
1、新建多维分析。选择Cube 【Sales】构建多维分析。其中行区选择"时间"维。
2、mondrian当前年及前后两年。在左侧资源树的【自定义命名集】-》【全局】下新建一个全局自定义命名集。
在其MDX表达式中输入如下：
`{StrToMember(``"[时间].["``||trim(str(``int``(``year``(now()))))||``"年]"``).PrevMember.PrevMember,StrToMember(``"[时间].["``||trim(str(``int``(``year``(now()))))||``"年]"``).PrevMember,StrToMember(``"[时间].["``||trim(str(``int``(``year``(now()))))||``"年]"``),StrToMember(``"[时间].["``||trim(str(``int``(``year``(now()))))||``"年]"``).NextMember,StrToMember(``"[时间].["``||trim(str(``int``(``year``(now()))))||``"年]"``).NextMember.NextMember}`  
---  
具体设置如下图：   
