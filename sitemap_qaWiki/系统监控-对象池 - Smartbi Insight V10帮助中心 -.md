
对象池用于查看系统对象的使用情况，使用后是否被释放，辅助分析系统性能问题。
对象缓冲池可以增强系统在并发时的性能，减少服务器的压力，提高用户报表查询速度。
对象池中相关属性项说明如下：
JVM BusinessViewBOMap |  JVM中数据集定义对象缓冲池 Size：数据集定义对象个数  Values： 内存地址+数据集定义名称列表  
---|---  
JVM CellElementMap |  JVM中复杂报表单元格对象缓冲池  Size：复杂报表单元格对象个数  Values：CE[532,1,1,1]厦门  
JVM DBSQLResultStoreMap |  JVM中业务数据缓冲池  Size：业务数据对象个数  Values：业务数据对象基本信息，如：数据集ID、参数等  
FixedReportPoolCacheMap |  JVM业务报表对象缓冲池  Size：业务报表对象个数  
ExecutedReportPoolCacheMap |  JVM复杂报表运行时对象缓冲池  Size：复杂报表运行时对象个数 Keys：  
FixedReportPool |  业务报表对象池，用于缓存复杂报表表样对象，减少重复创建次数  Active：当前活动的业务报表对象个数  Idle：已释放的业务报表对象个数  
ExecutedReportPool |  复杂报表运行时对象池，用于缓存复杂报表的数据对象，减少重复访问数据库获取数据。 复杂报表在没有设置回写规则的情形下，才存在复杂报表运行时对象池  Active：当前活动的复杂报表运行时对象个数  Idle：已释放的复杂报表运行时对象个数  
BusinessViewBOPool |  数据集定义对象池，用于缓存报表所依赖的数据集对象，减少重复创建次数  Active：当前活动的数据集定义对象个数  Idle：已释放的数据集定义对象个数  
DBSQLResultStorePool |  业务数据对象缓存池，根据报表中的条件（如参数、排序等）缓存业务数据，减少重复访问数据库获取数据  Active：当前活动的业务数据对象个数  Idle：已释放的业务数据对象个数  
BaseBofKeyedPoolableObjectFactory |  BOF_OBJECT_POOL_CACHE size：当前所有的对象连接池的总的Key个数（包括本机直接创建的对象和其他服务器创建通知同步过来的） CacheIdentity2KeyMap size：仅仅只包含由本服务器创建的对象的Key集合  
ConnectionPool |  数据库连接池（res为知识库）  Name：数据源名称  Active：当前活动的连接个数  Idle：已关闭连接个数  
