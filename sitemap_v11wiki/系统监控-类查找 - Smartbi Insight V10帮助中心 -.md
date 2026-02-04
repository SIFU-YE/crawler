
  *     * 

该页面通过输入类名，查看类所在路径。用于解决系统出现NoClassDefineFound之类的异常。
# 操作说明
将需要查询的类名拷贝到输入框中，点击“提交查询内容”进行查询。
下方即出现对应的类的相关信息，其中加载类的文件路径一般会包含类所在的jar名称。
**查询结果中相关项说明如下:**
classname  
---  
加载类的文件路径 | 显示该类实际在Smartbi服务器中存放的位置  
类加载器 | 显示加载该类的类加载器及其祖先类加载器，若显示为“Bootstrap加载器”则表示该类是由JVM的Bootstrap加载器加载的  
# 应用场景
  * #### **二次开发定位缺失类所在的jar**


在基于smartbi进行二次开发时，可能会遇到NoClassDefFoundError等异常，此时可以在上述类查找中定位相关类所在的jar名称，例如遇到找不到smartbi.net.sf.json.JSONObject类，可以在类查找中查找如下图：
通过查找结果可以确定，缺失的类关联的jar路径在 E:/soft/tomcat/apache-tomcat-8.5.51/webapps/smartbi/WEB-INF/lib/ 目录的 smartbi-Common.jar 中，就是说明，开发者需要到 smartbi 服务器的该路径下获取jar加入到其开发工具中的build path中才能解决smartbi.net.sf.json.JSONObject类找不到的问题。  
