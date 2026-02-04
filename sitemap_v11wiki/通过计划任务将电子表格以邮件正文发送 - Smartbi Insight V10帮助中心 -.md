
## 1.示例场景
通常我们可通过计划任务把电子表格报表内容或者报表导出的图片以邮件的正文形式发送。


## 2.发送电子表格报表内容
### 2.1效果
### 2.2操作步骤：
1、先创建好电子表格报表。
2、在【系统运维】-》【计划任务】-》【任务】创建任务，【任务类型】选择：“定制”。
JAVA代码如下：
**自定义任务**
```
importPackage(Packages.smartbi.sdk.service.spreadsheetreport);
importPackage(Packages.smartbi.scheduletask.task);
importPackage(Packages.smartbi.sdk.service.systemconfig);
importPackage(Packages.java.lang);
importPackage(Packages.java.util);
importPackage(Packages.java.text);
importPackage(Packages.java.io);
importPackage(Packages.org.apache.commons.lang);
importPackage(Packages.org.apache.commons.mail);
importPackage(Packages.smartbi.scheduletask.component);
importPackage(Packages.smartbi.util);

var report = null;
//定义email对象，初始化参数
var multiPartEmail = new SmartbiMultiPartEmail();
var systemConfigService = new SystemConfigService(connector);
var configList = systemConfigService.getSystemConfigs();

var mailServer = null;
var fromAddress = null;
var userName = null;
var password = null;
var encryptPassword = null;
var emailSSLEnabled = null;
var emailTLSEnabled = null;
var mailAlias = null;
var port = "";
for (var i = 0; i < configList.size(); i++) {
    var config = configList.get(i);
    if (config != null) {
        if (config.getKey().equals("EMAIL_SMTP_SERVER")) {
            mailServer = config.getValue();
        } else if (config.getKey().equals("EMAIL_USER_NAME")) {
            userName = config.getValue();
        } else if (config.getKey().equals("EMAIL_USER_ALIAS")) {
            mailAlias = config.getValue();
        } else if (config.getKey().equals("EMAIL_USER_ADDRESS")) {
            fromAddress = config.getValue();
        } else if (config.getKey().equals("EMAIL_USER_PASSWORD")) {
            password = config.getValue();
        } else if (config.getKey().equals("EMAIL_USER_PASSWORD_ENCRYPT")) {
            encryptPassword = config.getValue();
        } else if (config.getKey().equals("EMAIL_SSL_ENABLED")) {
            if (config.getValue().equals("true")) {
                emailSSLEnabled = true;
            }
        } else if (config.getKey().equals("EMAIL_TLS_ENABLED")) {
            if (config.getValue().equals("true")) {
                emailTLSEnabled = true;
            }
        } else if (config.getKey().equals("EMAIL_SMTP_PORT")) { //端口
            port = config.getValue().trim();
        }
    }
}
if (StringUtil.equals(encryptPassword, "true")) {
    password = AESCryption.decrypt(password);
}
System.out.println(mailServer);
System.out.println(fromAddress);
System.out.println(password);
multiPartEmail.setHostName(mailServer);
if (!StringUtil.isNullOrEmpty(password)) {
    multiPartEmail.setAuthentication(userName, password);
}
if (mailAlias) {
    multiPartEmail.setFrom(fromAddress, mailAlias);
} else {
    multiPartEmail.setFrom(fromAddress);
}
if (emailSSLEnabled) {
    multiPartEmail.setSSL(true);
    if (port != "") {
        multiPartEmail.setSslSmtpPort(port);
    }
}
if (emailTLSEnabled) {
    multiPartEmail.setTLS(true);
}
if (port != "" && !emailSSLEnabled) {
    multiPartEmail.setSmtpPort(port);
}
multiPartEmail.addTo("zhouya1@smartbi.com.cn"); //接收邮箱地址1
multiPartEmail.addTo("zhouya2@smartbi.com.cn"); //接收邮箱地址2
multiPartEmail.addTo("zhouya3@smartbi.com.cn"); //接收邮箱地址3
multiPartEmail.addTo("zhouya4@smartbi.com.cn"); //接收邮箱地址4

multiPartEmail.setCharset("GBK"); //邮件内容字符集
multiPartEmail.setSubject("测试邮件"); //邮件标题

// var sb = new StringBuffer();
// sb.append("<html><body><p>这是一个系统自动发送的邮件，请勿回复。</p></body></html>");
// sb.append("\n");

report = new SSReport(connector);
report.open("I4028812115561f6c01449562ca190067"); //报表资源ID
//report.setParamValue(String id, String value, String displayValue);//设置报表的参数默认值
var os = new ByteArrayOutputStream();
report.doExport("HTML", "", "", os, "", "", "");
var html = os.toString("utf8");
//logger.info(html);
report.close();
//发送邮件
multiPartEmail.setHtmlMsg(html);
multiPartEmail.send();
```

3、在左边资源树上的【系统运维】->【计划任务】->【计划】中新建一个计划，设置待执行任务为刚刚创建的任务，并设置计划运行的周期，如下图：
4、可参考示例资源 migrate(邮件发送电子表格报表内容).xml
## 3.发送电子表格导出图片
### 3.1效果
### 3.2操作步骤
1、在【分析展现】中创建电子表格报表。
2、在【系统运维】-》【计划任务】-》【任务】创建任务，【任务类型】选择：“定制”。
JAVA代码如下：
**自定义任务**
```
importPackage(Packages.smartbi.sdk.service.spreadsheetreport);
importPackage(Packages.smartbi.scheduletask.task);
importPackage(Packages.smartbi.sdk.service.systemconfig);
importPackage(Packages.java.lang);
importPackage(Packages.java.util);
importPackage(Packages.java.text);
importPackage(Packages.java.io);
importPackage(Packages.org.apache.commons.lang);
importPackage(Packages.org.apache.commons.mail);
importPackage(Packages.smartbi.scheduletask.component);
importPackage(Packages.smartbi.util);

var report = null;
//定义email对象，初始化参数
var multiPartEmail = new SmartbiMultiPartEmail();
var systemConfigService = new SystemConfigService(connector);
var configList = systemConfigService.getSystemConfigs();

//服务器地址，例如qq邮箱为smtp.qq.com
var mailServer = null;
//发送方邮箱
var fromAddress = null;
//发送方账号
var userName = null;
//发送方的SMTP密码，需要事先开通邮箱账号的SMTP服务
var password = null;
var encryptPassword = null;
var emailSSLEnabled = null;
var emailTLSEnabled = null;
var mailAlias = null;
var port = "";
for (var i = 0; i < configList.size(); i++) {
    var config = configList.get(i);
    if (config != null) {
        if (config.getKey().equals("EMAIL_SMTP_SERVER")) {
            mailServer = config.getValue();
        } else if (config.getKey().equals("EMAIL_USER_NAME")) {
            userName = config.getValue();
        } else if (config.getKey().equals("EMAIL_USER_ALIAS")) {
            mailAlias = config.getValue();
        } else if (config.getKey().equals("EMAIL_USER_ADDRESS")) {
            fromAddress = config.getValue();
        } else if (config.getKey().equals("EMAIL_USER_PASSWORD")) {
            password = config.getValue();
        } else if (config.getKey().equals("EMAIL_USER_PASSWORD_ENCRYPT")) {
            encryptPassword = config.getValue();
        } else if (config.getKey().equals("EMAIL_SSL_ENABLED")) {
            if (config.getValue().equals("true")) {
                emailSSLEnabled = true;
            }
        } else if (config.getKey().equals("EMAIL_TLS_ENABLED")) {
            if (config.getValue().equals("true")) {
                emailTLSEnabled = true;
            }
        } else if (config.getKey().equals("EMAIL_SMTP_PORT")) { //端口
            port = config.getValue().trim();
        }
    }
}
//   System.out.println(mailServer);
//   System.out.println(fromAddress);
//   System.out.println(password);
if (StringUtil.equals(encryptPassword, "true")) {
    password = AESCryption.decrypt(password);
}
multiPartEmail.setHostName(mailServer);
if (!StringUtil.isNullOrEmpty(password)) {
    multiPartEmail.setAuthentication(userName, password);
}
if (mailAlias) {
    multiPartEmail.setFrom(fromAddress, mailAlias);
} else {
    multiPartEmail.setFrom(fromAddress);
}
if (emailSSLEnabled) {
    multiPartEmail.setSSL(true);
    if (port != "") {
        multiPartEmail.setSslSmtpPort(port);
    }
}
if (emailTLSEnabled) {
    multiPartEmail.setTLS(true);
}
if (port != "" && !emailSSLEnabled) {
    multiPartEmail.setSmtpPort(port);
}

multiPartEmail.addTo("21206373@qq.com"); //接收邮箱地址1
multiPartEmail.addTo("21206374@qq.com"); //接收邮箱地址2
multiPartEmail.addTo("21206375@qq.com"); //接收邮箱地址3
multiPartEmail.addTo("21206376@qq.com"); //接收邮箱地址4
//multiPartEmail.addTo("zhouyan1@smartbi.com.cn");//再添加接收邮箱地址
multiPartEmail.setCharset("GBK"); //邮件内容字符集
multiPartEmail.setSubject("测试邮件"); //邮件标题

report = new SSReport(connector);
report.open("I8a87946850215270014d65ed454c1f6e"); //报表资源ID
report.setParamValue("OutputParameter.I40282124232b5300014d503ddc0b1401.p_year_curr", "2015", "2015"); //设置报表的参数默认值
//report.open("I8a87946850215270014d65ed454c1f6e"); //第二报表资源ID
//report.setParamValue("OutputParameter.I40282124232b5300014d503ddc0b1401.p_year_curr", "2015", "2015");//第二报表资源设置报表的参数默认值    

var pngFile = File.createTempFile("emailtask", ".png");
var os = new FileOutputStream(pngFile);
report.doExport("PNG", "", "", os, "", "", "");
os.flush();
os.close();
report.close();
var fileLen = pngFile.length();
//发送邮件
var cid = multiPartEmail.embed(pngFile);
var sb = new StringBuffer();
sb.append("<html><body>length:" + fileLen + "<img src=\"cid:" + cid + "\"></body></html>");
sb.append("\n");
var html = sb.toString();
multiPartEmail.setHtmlMsg(html);
multiPartEmail.send();

```

3、在左边资源树上的【系统运维】->【计划任务】->【计划】中新建一个计划，设置待执行任务为刚刚创建的任务，并设置计划运行的周期，如下图：
4、可参考示例资源 migrate(邮件发送电子表格导出图片).xml
## 4.注意事项
1、需要修改的部分如下图。
2、设置参数默认值可在【系统运维】->【数据集】中打开指定的数据集，参考以下方式：
3、发送报表内容到正文注意
（1）示例中接收邮箱建议使用foxmail客户端查看，使用网页版邮箱可能会产生格式丢失的问题（原因：网页版邮箱对部分html标签的解析不兼容，导致会屏蔽很多信息），使用outlook客户端可能存在正文被转换成html附件的情况（由于部分邮箱服务器的限制）。
（2）电子表格必须是纯表格（文本），不能存在图形，如果存在图形或其他非文本内容会存在发送的正文存在问题；
（3）不支持有多个sheet 页的电子表格。
（4）不能设置图片水印，否则会导致发送的正文出现乱码。
上述场景建议考虑使用导出图片的方式。
**注：如果代码遇到发送邮箱有问题，请先按照链接系统选项配置里配置邮箱信息！ ---邮件配置**  
