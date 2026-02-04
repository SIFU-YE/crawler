
将报表或页面嵌入到第三方系统中（资源集成），是系统集成中最为常见的一种方式。Smartbi 可以方便地集成到客户现有的门户系统中，或者是其它任意系统中。通常做法是在页面中放置一个 iframe 标签，然后通过 src 属性访问 Smartbi 的资源链接即可。详述如下。
在外部系统中集成 Smartbi 的资源，全部通过下面的 URL 地址来访问。Smartbi 将其所有类型资源的访问全部整合到了 openresource.jsp 之中。
折叠代码
```
http://localhost:18080/smartbi/vision/openresource.jsp

```

使用移动设备通过“openresource.jsp”打开交互式仪表盘、电子表格的资源时，访问页面将默认切换至移动端效果
目前支持被集成的资源类型有：交互式仪表盘、数据模型、指标模型、即席查询、透视分析、自助ETL、数据挖掘、ETL自动化、作业流、自助数据集、多维分析、即席查询（旧）、透视分析（旧）、Web链接、电子表格、WEB电子表格、可视化查询、SQL数据集、存储过程查询、原生SQL查询，以及Excel导入模版等。
下面这几个参数是集成任何类型资源时，都可以传入的参数。但如果已经单点登录过，就不需要在 URL 中再传递用户名和密码了，除非希望以一个新的用户去打开资源。
user | 登录 Smartbi 的用户名  
---|---  
password | 登录 Smartbi 的密码  
resid | Smartbi 资源唯一 ID 值。可以从任意资源的“资源属性”对话框上“节点ID”中获取该值  
传递上述参数，打开某个 Smartbi 资源的访问地址。
如何获取 Smartbi 资源的 resid 值。打开对应资源的“资源属性”对话框，将其上的“节点ID”拷贝出来即可。
除了基本参数外，各种资源类型还有一些其它参数可供设置。按照资源类型，分别说明如下。
paramsInfo | 参数信息，需要对查询参数对象(key为筛选器组件的标题)进行JSON序列化。 | JSON对象序列化后的字符串，JSON 结构见示例 | 单个参数：openresource.jsp?resid=e06fd037ef41336fe79908f60e961c95&paramsInfo={"OrderDate":{"values":["2016-01-03"]}}单个参数多个参数值：openresource.jsp?resid=e06fd037ef41336fe79908f60e961c95&paramsInfo={"OrderDate":{"values":["2016-01-03", "2016-01-06"]}}多个参数：openresource.jsp?resid=e06fd037ef41336fe79908f60e961c95&paramsInfo={"OrderDate":{"values":["2016-01-03"]},"OrderDate2":{"values":["2016-01-10"]}}注：上面例子的“OrderDate”为筛选器组件的标题，默认为对应的维度名称  
---|---|---|---  
paramsInfoBase64 | paramsInfo参数经过Base64编码后的格式，为了避免Base64编码后的结果存在一些特殊字符需要再用encodeURIComponent转化，用来解决参数中包含中文和特殊字符问题；与paramsInfo参数，两者选其一 | paramsInfo的Base64编码 | openresource.jsp?resid=e06fd037ef41336fe79908f60e961c95&paramsInfoBase64=eyJPcmRlckRhdGUiOnsidmFsdWVzIjpbIjIwMTYtMDEtMDMiXX19  
showtoolbar | 控制是否在报表上显示工具栏，默认为true。当设备为移动端且 “showheader=false” 时，隐藏标题栏，并显示右侧的按钮区 | true 或 false | 无  
operate | 操作方式，目前仅支持 operate=edit 或 operate=EDIT ，可选参数，传递该参数代表编辑交互式仪表盘 | edit 或 EDIT | 无  
paramsInfo | 参数信息，需要对即席查询的查询参数数组进行JSON序列化。同交互式仪表盘。 | JSON对象序列化后的字符串 | openresource.jsp?resid=e06fd037ef41336fe79908f60e961c95&paramsInfo={"OrderDate":{"values":["2016-01-03", "2016-01-06"]}}  
---|---|---|---  
paramsInfoBase64 | paramsInfo参数经过Base64编码后的格式，用来解决参数中包含中文和特殊字符问题。与paramsInfo参数，两者选其一。 | paramsInfo的Base64编码 | openresource.jsp?resid=e06fd037ef41336fe79908f60e961c95&paramsInfoBase64=eyJPcmRlckRhdGUiOnsidmFsdWVzIjpbIjIwMTYtMDEtMDMiXX19  
showtoolbar | 控制是否在报表的分析页面显示工具栏，默认为true。 | true 或 false | 无  
showSidebar | 控制是否显示侧边栏，默认为显示 | false | 无  
mode | 控制预览或者编辑模式 | PREVIEW 或 EDIT | 无  
showDataPanel | 显示/隐藏“数据”面板，默认为显示 | false | 无  
showSettingPanel | 显示/隐藏“设置”面板，默认为显示 | false | 无  
refresh | 打开报表是否刷新数据，默认为false。 | true 或 false | 无  
hidetoolbaritems | 控制报表工具栏中需要隐藏的按钮，其格式如下：REFRESH SAVE SAVEAS MYFAVORITE；中间以空格分割 | 
  * FALLBACK 撤销；
  * FORWARD 重做；
  * REFRESH 刷新；
  * SAVE 保存；
  * SAVEAS 另存为；
  * EXPORT 导出；
  * PREVIEW 浏览/编辑；
  * VIEWSQL 查看SQL
  * TIMECONSUMING 耗时分析 
  * ENTER_PIVOT_ANALYSIS_MODE 透视分析模式 
  * SHARE 分享；
  * COMMENT 评论；
  * MYFAVORITE 保存到收藏夹；
  * LIKE 点赞；
  * ALARM_MANAGEMENT 数据预警；

| 无  
paramsInfo | 参数信息，需要对即席查询的查询参数数组进行JSON序列化。同交互式仪表盘。 | JSON对象序列化后的字符串 | openresource.jsp?resid=e06fd037ef41336fe79908f60e961c95&paramsInfo={"OrderDate":{"values":["2016-01-03", "2016-01-06"]}}  
---|---|---|---  
paramsInfoBase64 | paramsInfo参数经过Base64编码后的格式，用来解决参数中包含中文和特殊字符问题。与paramsInfo参数，两者选其一。 | paramsInfo的Base64编码 | openresource.jsp?resid=e06fd037ef41336fe79908f60e961c95&paramsInfoBase64=eyJPcmRlckRhdGUiOnsidmFsdWVzIjpbIjIwMTYtMDEtMDMiXX19  
showtoolbar | 控制是否在报表的分析页面显示工具栏，默认为true。 | true 或 false | 无  
showSidebar | 控制是否显示侧边栏，默认为显示 | false | 无  
mode | 控制预览或者编辑模式 | PREVIEW 或 EDIT | 无  
showDataPanel | 显示/隐藏“数据”面板，默认为显示 | false | 无  
showSettingPanel | 显示/隐藏“设置”面板，默认为显示 | false | 无  
refresh | 打开报表是否刷新数据，默认为false。 | true 或 false | 无  
showFieldPopupMenu | 控制是否在右侧的工作区面板中显示右键菜单，默认为true。 | true 或 false | 无  
hidetoolbaritems | 控制报表工具栏中需要隐藏的按钮，其格式如下：REFRESH SAVE SAVEAS MYFAVORITE；中间以空格分割 | 
  * REFRESH 刷新；
  * SAVE 保存；
  * SAVEAS 另存为；
  * EXPORT 导出；
  * PREVIEW 浏览/编辑；
  * VIEWSQL 查看SQL
  * TIMECONSUMING 耗时分析 
  * ENTER_DETAIL_QUERY_MODE 即席查询模式 
  * SHARE 分享；
  * COMMENT 评论；
  * MYFAVORITE 保存到收藏夹；
  * LIKE 点赞；
  * ALARM_MANAGEMENT 数据预警；

| 无  
operate | 操作方式，可选参数，传递该参数代表编辑web电子表格 | edit | 无  
---|---|---|---  
paramsInfo | 参数信息，需要对电子表格的查询参数数组进行JSON序列化 | JSON对象序列化后的字符串 | openresource.jsp?paramsInfo=[{"name":"参数名称","value":"真实值","displayValue":"显示值"}]&resid=I2c949e8e1ac2d5e6011ac380971301b8  
---|---|---|---  
paramsInfoBase64 | paramsInfo参数经过Base64编码后的格式，用来解决参数中包含中文和特殊字符问题。与paramsInfo参数，两者选其一。 | paramsInfo的Base64编码 | openresource.jsp?resid=I8a86005c0195025902591ea901953c3c527f2723&paramsInfoBase64=W3sibmFtZSI6IlBfSU5WTUdfUFJBX0NVUl9PUkdfdGVzdCIsInZhbHVlIjoiMyIsImRpc3BsYXlWYWx1ZSI6IlwiM1wiIn1d  
showtoolbar | 控制是否在报表的分析页面显示工具栏，默认为true。当设备为移动端且 “showheader=false” 时，隐藏标题栏，并显示右侧的按钮区； | true 或 false | 无  
shorttoolbar | 控制是否在报表分析页面显示快速工具栏，默认为false。 | true 或 false | 无  
hiddenParamPanel | 控制是否在报表分析页面显示参数面版，默认为true。 | true 或 false | 无  
isWritable | 控制回写报表是否允许回写。 | true 或 false | 无  
hidetoolbaritems | 控制报表工具栏中需要隐藏的按钮；中间以空格分割 | REFRESH 刷新； MYFAVORITE 保存到收藏夹； EXPORT 导出； PRINT 打印。 SETUSERPARAM个人参数 | openresource.jsp?resid=I8a8af0a60172b58db58da4e40172b75dee4f1f19&hidetoolbaritems=REFRESH MYFAVORITE  
业务查询指的是 可视化数据集、SQL数据集、原生SQL数据集、存储过程数据集、多维数据集、 Java数据集
hidepropertypanel | 隐藏属性面板。 | true 或 false | 无  
---|---|---|---  
shorttoolbar | 控制是否显示快速工具栏，默认为false。 | true 或 false | 无  
type | 操作方式，仅支持type=edit或type=EDIT，可选参数，传递该参数代表编辑Excel导入模版 | edit 或 EDIT | 无  
---|---|---|---  
paramsInfo | 参数信息，需要对灵活分析的查询参数数组进行JSON序列化 | JSON对象序列化后的字符串 | openresource.jsp?paramsInfo=[{"name":"参数名称","value":"真实值","displayValue":"显示值"}]&resid=I2c949e8e1ac2d5e6011ac380971301b8  
---|---|---|---  
paramsInfoBase64 | paramsInfo参数经过Base64编码后的格式，用来解决参数中包含中文和特殊字符问题。与paramsInfo参数，两者选其一。 | paramsInfo的Base64编码 | openresource.jsp?resid=I8a86005c0195025902591ea901953c3c527f2723&paramsInfoBase64=W3sibmFtZSI6IlBfSU5WTUdfUFJBX0NVUl9PUkdfdGVzdCIsInZhbHVlIjoiMyIsImRpc3BsYXlWYWx1ZSI6IlwiM1wiIn1d  
showtoolbar | 控制是否在报表的分析页面显示工具栏，默认为true。 | true 或 false | 无  
shorttoolbar | 控制是否在报表分析页面显示快速工具栏，默认为false。 | true 或 false | 无  
refresh | 打开报表是否刷新数据，默认为false。 | true 或 false | 无  
shorttoolbaralign | 控制快速工具栏对齐方式 | center、left、right | 无  
hidetoolbaritems | 控制报表工具栏中需要隐藏的button；中间以空格分割 | REFRESH 刷新； SAVE 保存； SAVEAS 另存为； MYFAVORITE 保存到收藏夹； EXPORT 导出； VIEW 视图； SELECTFIELD 增加/删除字段； CHARTSETTING 图形设置； PRINT 打印 PARAMSETTING 参数设置； SUBTOTAL 分类汇总； REPORTSETTING 报表设置。 BACKWARD 后退 FORWARD 前进 CREATEINSIGHTINQUERY 透视分析 SETUSERPARAM 个人参数 | 无  
chartindex | 图形在报表中的位置，string 类型；从左至右、从上至下开始编号，编号从0开始。 | string | 无  
chartname | 图形名称，string 类型。如果通过chartname定位图形，必须确保图形没有重名；如果chartindex和chartname都有值，则以chartindex为准定位图形。 | 取值 | 无  
charttype | 图形类型，string 类型 | 线图（charttype=Line） 柱图（charttype= StackColumn） 2D饼图（charttype= Pie2D） 油量表（charttype= Gauge）  | 无  
paramsInfo | 参数信息，需要对多维分析的查询参数数组进行JSON序列化 | JSON对象序列化后的字符串 | openresource.jsp?paramsInfo=[{"name":"参数名称","value":"真实值","displayValue":"显示值"}]&resid=I2c949e8e1ac2d5e6011ac380971301b8  
---|---|---|---  
paramsInfoBase64 | paramsInfo参数经过Base64编码后的格式，用来解决参数中包含中文和特殊字符问题。与paramsInfo参数，两者选其一。 | paramsInfo的Base64编码 | openresource.jsp?resid=I8a86005c0195025902591ea901953c3c527f2723&paramsInfoBase64=W3sibmFtZSI6IlBfSU5WTUdfUFJBX0NVUl9PUkdfdGVzdCIsInZhbHVlIjoiMyIsImRpc3BsYXlWYWx1ZSI6IlwiM1wiIn1d  
showtoolbar | 控制是否在报表的分析页面显示工具栏，默认为true。 | true 或 false | 无  
shorttoolbar | 控制是否在报表分析页面显示快速工具栏，默认为false。 | true 或 false | 无  
refresh | 打开报表是否刷新数据，默认为false。 | true 或 false | 无  
shorttoolbaralign | 控制快速工具栏对齐方式 | center、left、right | 无  
operate | 多维分析的操作类型 | browse 浏览 discover 探索； custom 定制  | 无  
hidetoolbaritems | 控制报表工具栏中需要隐藏的button；中间以空格分割 | BACKWARD 后退 FORWARD 前进 REFRESH 刷新； SAVE 保存； SAVEAS 另存为； MYFAVORITE 保存到收藏夹； CHARTSETTING 图形设置； PANEL 面板； VIEW 视图； REPORTSETTING 报表设置。 ADVANCEDSETTING 高级设置； SUBTOTAL 分类汇总； PARAMSETTING 参数设置； MEMBERSETTING 成员属性设置 CLEARHIDDENSETTINGS 取消隐藏行列 PREVIEWMDX 查看MDX EXPORT 导出； PRINT 打印 | 无  
paramsInfo | 参数信息，需要对即席查询的查询参数数组进行JSON序列化 | JSON对象序列化后的字符串 | openresource.jsp?paramsInfo=[{"name":"参数名称","value":"真实值","displayValue":"显示值"}]&resid=I2c949e8e1ac2d5e6011ac380971301b8  
---|---|---|---  
paramsInfoBase64 | paramsInfo参数经过Base64编码后的格式，用来解决参数中包含中文和特殊字符问题。与paramsInfo参数，两者选其一。 | paramsInfo的Base64编码 | openresource.jsp?resid=I8a86005c0195025902591ea901953c3c527f2723&paramsInfoBase64=W3sibmFtZSI6IlBfSU5WTUdfUFJBX0NVUl9PUkdfdGVzdCIsInZhbHVlIjoiMyIsImRpc3BsYXlWYWx1ZSI6IlwiM1wiIn1d  
showtoolbar | 控制是否在报表的分析页面显示工具栏，默认为true。 | true 或 false | 无  
shorttoolbar | 控制是否在报表分析页面显示快速工具栏，默认为false。 | true 或 false | 无  
refresh | 打开报表是否刷新数据，默认为false。 | true 或 false | 无  
showLeftTree | 打开报表是否显示资源树，默认为false。 | true 或 false | 无  
hidetoolbaritems | 控制报表工具栏中需要隐藏的button；中间以空格分割 | REFRESH 刷新； SAVE 保存； SAVEAS 另存为； MYFAVORITE 保存到收藏夹； EXPORT 导出； VIEWSQL 查看SQL VIEW 视图 CHARTSETTING 图形设置； PRINT 打印 PARAMSETTING 参数设置； REPORTSETTING 报表设置。 FIELDSETTING 字段设置 CREATEINSIGHTINQUERY 透视分析 MPP 抽取 FILTERRELATIONSSETTING 过滤器关系 USERPARAM 个人参数 TIMECONSUMING 耗时分析 BLANK1 BLANK2 BLANK3 分割线 | 无  
paramsInfo | 参数信息，需要对透视分析的查询参数数组进行JSON序列化 | JSON对象序列化后的字符串 | openresource.jsp?paramsInfo=[{"name":"参数名称","value":"真实值","displayValue":"显示值"}]&resid=I2c949e8e1ac2d5e6011ac380971301b8  
---|---|---|---  
paramsInfoBase64 | paramsInfo参数经过Base64编码后的格式，用来解决参数中包含中文和特殊字符问题。与paramsInfo参数，两者选其一。 | paramsInfo的Base64编码 | openresource.jsp?resid=I8a86005c0195025902591ea901953c3c527f2723&paramsInfoBase64=W3sibmFtZSI6IlBfSU5WTUdfUFJBX0NVUl9PUkdfdGVzdCIsInZhbHVlIjoiMyIsImRpc3BsYXlWYWx1ZSI6IlwiM1wiIn1d  
showtoolbar | 控制是否在报表的分析页面显示工具栏，默认为true。 | true 或 false | 无  
showWorkspace | 控制是否显示右侧的工作区面板，默认为false。 | true 或 false | 无  
refresh | 打开报表是否刷新数据，如果不指定，以报表保存时的设置为准。 | true 或 false | 无  
showFieldPopupMenu | 控制是否在右侧的工作区面板中显示右键菜单，默认为true。 | true 或 false | 无  
hidetoolbaritems | 控制报表工具栏中需要隐藏的button；中间以空格分割 | SAVE 保存；SAVEAS 另存为； BTNPARAMSETTING 参数设置； PANEL 面板 REPORTSETTING 报表设置。 WARNING 告警 REFRESH 刷新； MYFAVORITE 保存到收藏夹； CHARTSETTING 图形设置； VIEW 视图 EXPORT 导出； PRINT 打印 SETUSERPARAM 个人参数 RESOURCETREE 资源树 FILTERRELATION 过滤 TIMECONSUMING 耗时分析 _space1、_space2、_space3、_space4、_space5 分割线 | 无  
fieldsConfig | 放行区列区度量区的字段信息数组，需要对字段信息数组进行JSON序列化 | 字段的内容包括： name : "字段名，和字段别名只需提供任意一个", alias : "字段别名，和字段名只需提供任意一个", pos : "row/column/measure中的一个，指定字段所在的区域", num : 字段在行区/列区/度量区中的顺序号 | 无  
下面仅介绍基本参数传递，不带任何可选参数。
  * 在外部系统中使用 IFrame 方式打开 Smartbi 资源。通常做法是在页面中放置一个 iframe 标签，然后通过 src 属性访问 Smartbi 的资源链接即可。
  * 可使用如下两种方法打开资源。
    * 方式一：每次打开资源时，都传递用户名、密码、资源ID过去。为了安全原因，也可以用 POST 方式传递上述参数值。
折叠代码
```
http://localhost:18080/smartbi/vision/openresource.jsp?resid=I2c949eaf1a942102011a9561f7e7015d&user=admin&password=manager

```

    * 方式二：系统初始化时采用单点登录方式登录 Smartbi，之后通过链接打开资源，就不需要再传递用户名和密码了。
折叠代码
```
http://localhost:18080/smartbi/vision/openresource.jsp?resid=I2c949eaf1a942102011a9561f7e7015d

```

  * gif演示示例源码请参考：打开资源示例（不带查询参数）.rar


在一些系统集成中，用户可能希望从外部传入参数值来打开 Smartbi 资源，动态刷新数据。动态传递参数的方法，说明如下。 
  * 将下面这段 JavaScript 代码拷贝到第三方系统的某个页面里，因为后面我们需要使用其中的 function toJSONString(obj) 方法对传递的参数值进行处理。


折叠代码
```




function parseJSON (jsonString) { //FROM: json.org,json.js

  
---  



    return eval('(' + jsonString + ')');
  






function toJSONString (obj) { //FROM: json.org,json.js

  



    var m = {   '\b': '\\b',
  



                        '\t': '\\t',
  



                        '\n': '\\n',
  



                        '\f': '\\f',
  



                        '\r': '\\r',
  




                        '\\': '\\\\'    };
  




        array: function (x) {
  



            var a = ['['], b, f, i, l = x.length, v;
  



            if(l == 0) {
  



                var isNull = true;
  



                for(var i in x) {
  



                    // Fenet's code begin

  



                    if ( i == "remove" || i == "indexOf" ) {
  



                        delete x[i];
  





                    if( x.toJSON)
  



                        return x.toJSON();
  



                    // Fenet's code end

  



                    isNull = false;
  





                if(!isNull) {
  



                    //throw null;

  



                    var a = ['{'], b, f, i, v;
  



                    for (i in x) {
  




                            f = s[typeof v];
  





                                if (typeof v == 'string') {
  




                                        a[a.length] = ',';
  




                                    a.push(s.string(i), ':', v);
  







                    a[a.length] = '}';
  



                    return a.join('');
  





                for (i = 0; i < l; i += 1) {
  



                    v = x[i];
  



                    f = s[typeof v];
  





                        if (typeof v == 'string') {
  




                                a[a.length] = ',';
  




                            a[a.length] = v;
  








            a[a.length] = ']';
  



            return a.join('');
  




        'boolean': function (x) {
  



            return String(x);
  




        'null': function (x) {
  



            return "null";
  




        number: function (x) {
  



            return isFinite(x) ? String(x) : 'null';
  




        object: function (x) {
  




                if (Object.prototype.toString.call(x) === "[object Array]") {
  



                    return s.array(x);
  




                var a = ['{'], b, f, i, v;
  



                for (i in x) {
  



                    v = x[i];
  



                        f = s[typeof v];
  





                            if (typeof v == 'string') {
  




                                    a[a.length] = ',';
  




                                a.push(s.string(i), ':', v);
  







                a[a.length] = '}';
  



                return a.join('');
  




            return 'null';
  




        string: function (x) {
  



            if (/["\\\x00-\x1f]/.test(x)) {
  



                x = x.replace(/([\x00-\x1f\\"])/g, function(a, b) {
  



                        var c = m[b];
  






                        c = b.charCodeAt();
  



                        return '\\u00' + Math.floor(c / 16).toString(16) + (c % 16).toString(16);
  





            return '"' + x + '"';
  





    return s[typeof obj](obj);
  



```

  * 构建参数信息对象数组。每个参数都是一个 JavaScript 对象，可设置如下属性。

id | 参数名称 | String类型 | 多维分析必选。  
---|---|---|---  
name | 参数名称 | String类型 | 必选，多维分析可不选用。  
value | 参数真实值 | String类型 | 必选。参数真实值可在参数定义中查看。  
displayValue | 参数显示值 | String类型 | 型 必选。  
standbyValue | 下拉列表参数的备选值 | String类型 | 可选项。当参数类型是下拉列表框时，可选择设置该属性值。 
  * 如果不设置，则会使用原有的参数设置；
  * 如果设置，系统中原有的参数备选值就会被忽略。
  * 用法："standbyValue":[["华南","华南"],["华北","华北"]]，注：每个中括号内的依次是备选值的真实值和显示值

  
  * 将参数列表对象转换成 JSON 字符串。通过调用步骤1中的 toJSONString() 函数可以将 JavaScript 对象序列化成 json 字符串，将此部分代码写在集成页面中。注意下图中红色矩形框内代码写法，如果一次传递多个参数就向 paramsInfo 数组中添加多个对象。


折叠代码
```



//生成Smartbi链接
  
---  




function generate({
  



    //生成待传递的参数数组对象

  



    var paramProductName = {
  



        "name": paramName.value,
  



        "value": realValue.value,
  



        "displayValue": displayValue.value
  




    var paramsInfo = [];
  



    paramsInfo.push(paramProductName);
  




    //生成form表单的action属性并赋值

  



    var urlStr = "http://" + address.value + "/smartbi/vision/openresource.jsp"

  



                + "?resid=" + resid.value
  



                + "&showtoolbar=true"

  



                + "&refresh=true"

  



                + "&user=" + user.value
  



                + "&password=" + password.value;
  



    url.value = urlStr + "\n以及form表单提交的参数：paramsInfo=" + toJSONString(paramsInfo);
  



    form.action = urlStr;
  




    //给form表单添加参数

  



    //传递的参数对象

  



    paramsInfoForm.value = toJSONString(paramsInfo);
  



```

  * 将user、password、resid、paramsInfo 等信息传递到 openresource.jsp 地址，即可打开相关资源。如下所示。


折叠代码
```
http://localhost:18080/smartbi/vision/openresource.jsp?paramsInfo=[{"name":"产品名称参数","value":"汽水","displayValue":"汽水"}]&resid=I2c949e8e1ac2d5e6011ac380971301b8&showtoolbar=true&refresh=true&user=admin&password=manager

```



注意：
  * 本示例不适用于交互式仪表盘。
  * 上述这种将 paramsInfo 放在URL链接中的方式，一定要将其放到 ？后面作为第一个参数。否则在某些浏览器上会出错，&p 被显示成了一个乱码。
  * 另外需要用 encodeURIComponent() 函数对 paramsInfo 进行编码，对其中的中文、特殊符号进行处理。Smartbi 小工具用来生成 paramsInfo 并编码：http://localhost:18080/smartbi/vision/getparamsinfo.html
  * 这种将参数直接放到URL中的方式，在实际项目上不太合适的，一方面 URL 长度有限制；再者如果参数中有中文和特殊符号时，就很容易出错。因此建议：最好通过 POST 的方式将参数值传递到 URL 地址上。
  * 在Tomcat高版本部署smartbi时，如果请求的URL在编码后的中文字符串带反斜杠，根据RFC文档中规定反斜杠是不安全字符，Tomcat在高版本中增加的安全验证，凡是RFC 3986中非URL可携带的字符，都会返回400错误，详细说明文档请看：Tomcat高版本部署smartbi通过URL拼接参数打开报表报400


**paramsInfo** 在实际项目中使用时稍显麻烦，需要构造参数对象数组，并生成 json 字符串。因此在 Smartbi 2.5 以后版本上提供了新的简易参数传递方式，以**param.** 作前缀表示参数实际值，**paramDisplay.** 前缀作为参数显示值。（打开自助仪表盘资源时，参数名（查询参数**对象key** ）对应为筛选器组件的标题）
  * 后台表单如下所示。


折叠代码
```



<form action="http://localhost:18080/smartbi/vision/openresource.jsp?resid=I2c90903e114f6f9601114f70e09d000e&refresh=true" method="POST">
  
---  



    <input type="text" name="param.开始日期" value="1996-03-17">

  



    <input type="text" name="paramDisplay.开始日期" value="1996-03-17">

  



    <input type="text" name="param.结束日期" value="1996-09-19">

  



    <input type="text" name="paramDisplay.结束日期" value="1996-09-19">

  



    <input type="text" name="param.产品目录" value="8">

  



    <input type="text" name="paramDisplay.产品目录" value="饮料">

  



    <input type="submit">

  



```



这样就比较简单了，也无需在项目中使用 JSON 作为类库，调用其中的 toJSONString() 方法了。但是需要注意，如果在URL中直接传递参数，参数值和名称等存在中文时容易出现问题。最好使用 POST 方式，或者在URL中以UTF-8编码传递，并修改 tomcat/conf/server.xml 中Connector 中添加URIEncoding="UTF-8" 属性。
  * 可参考资源集成传参异常排查指南解决参数传递异常、登录闪退等问题；
  * 在Chrome内核浏览器中遇到跨域问题，可参考单点登录集成，通过谷歌浏览器80版本及以上访问Smartbi报表，有时会跳转到Smartbi登录界面，其中使用nginx代理解决方案参考 nginx解决跨域问题方案参考


当Smartbi环境与第三方系统集成环境的域名、端口、协议有任意一个不同，那么就有可能发生跨域问题  
