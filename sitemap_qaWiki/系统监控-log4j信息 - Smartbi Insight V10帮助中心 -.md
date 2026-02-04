
该该页面用于获取服务器Log4j级别，可以临时修改级别配置，修改后配置信息直接生效；但在服务器重启后会重置，需要重新设置。
当用户在使用过程中遇到异常时，可在“**系统监控-日志** ”页面中查看到对应模块的日志，若无法获取到对自己有用的信息，可修改Log4j的级别配置，适当降低对应模块的Log4j日志输出级别。
日志配置模块说明
全局 | 控制全局日志的级别，优先级低于下方单独控制，对应config页面中服务器日志模块中全局日志级别配置。  
---|---  
AccessLog | 访问日志模块，控制access.log日志的输出级别。  
MaskRule | 脱敏规则模块，控制MaskRule.log日志的输出级别。  
com.tonbeller | jpivot第三方工具包模块，控制jpivot第三方工具包日志的输出级别。  
common.sql | SQL信息模块，控制sqls.log日志的输出级别。  
mdx | mdx信息模块，，控制smartbimdxs.log日志的输出级别。  
org.hibernate | hibernate第三方工具包模块，控制hibernate第三方工具包日志的输出级别  
org.quartz | quartz第三方工具包模块，控制quartz第三方工具包日志的输出级别  
smartbi | smartbi模块，控制smartbi相关代码日志的输出级别  
smartbi.trace | smartbi trace跟踪模块，控制smartbi trace相关代码日志的输出级别  
smartbix | smartbix模块，控制smartbix相关代码日志的输出级别  
注：可以添加**common.repository.sql** 下拉框选择用来输出知识库执行的SQL语句，详情见下方链接。
## log4j 日志输出级别说明
日志输出级别从高到低依次为：FATAL>ERROR>WARN>INFO>DEBUG>TRACE> ALL。
FATAL | 输出导致应用程序退出的严重错误、重大错误。  
---|---  
ERROR | 输出错误和异常信息，即虽然发生了错误事件但仍然不影响系统继续运行的信息。如果不想输出太多的日志，可以使用这个级别。  
WARN | 输出会出现潜在错误的情形信息。（有些信息不是错误信息，是给开发人员的一些提示）  
INFO | 在粗粒度级别上，突出强调应用程序的运行过程。输出一些对用户感兴趣的或者重要的信息，这个可以用于生产环境中输出程序运行的一些重要信息，但是不能滥用，避免打印过多的日志。  
DEBUG | 在细粒度级别上，对调试应用程序非常有帮助，主要用于开发过程中输出一些运行信息。  
TRACE | 很低的日志级别，一般用于追踪、程序推进。  
ALL | 日志级别最低的，用于输出所有级别的日志记录。  
程序只会输出**大于或等于当前日志级别** 的信息
例如：若将Log4j日志级别定义成INFO，则INFO、WARN、ERROR、FATAL级别的信息会打印出来，DEBUG、TRACE就不会被打印出来。  
