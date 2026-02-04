
  *   * 

通过使用电子表格的特殊字体，将单元格内容显示为条形码。
## Code39标准的条形码字体
### 示例效果
### 实现步骤
1、安装字体 |  从网上下载条形码字体包，将字体包后解压添加到 C:\Windows\Fonts 文件夹下，打开Excel字体即可看到安装的条形码。  
---|---  
2、新建电子表格 |  1）创建的电子表格如图： 2）设置条形码单元格的内容，条形码的单元格为：=【“*”】+【单元格地址】+【“*”】。 在C4单元格中输入【="*"&D4&"*"】，如图： 条形码引用的“单元格地址”只支持内容为“大写英文”和“0-9”的单元格。  
3、设置条形码 |  选中C4单元格，设置字体为“条形码字体”，并且相应调整字体大小，如图：  
4、保存查看  
##  Code128标准的条形码字体
由于 Code 128字体需要计算校验码，因此不可以直接输入一个字符串就生成符合规范的条码。
对应的介绍文档可参考网上的文档： http://www.cnblogs.com/ilookbo/p/4807112.html。
### 示例效果
### 实现步骤
1、安装字体 |  从网上下载条形码字体包，将字体包后解压添加到 C:\Windows\Fonts 文件夹下，打开Excel字体即可看到安装的条形码。  
---|---  
2、新建电子表格  
3、设置条形码 |  选中C3单元格，设置字体为“条形码字体”，并且相应调整字体大小，如图：  
4、设置服务端宏代码 |  1）点击工具栏的 **报表宏** 按钮，如图： 2）进入“宏编辑”界面，选中“服务端模块”，右键菜单选择**新建模块** ，如图： 3）弹出“新建模块”窗口，设置“名称、对象、事件”如下图： 4）点击 **确定** 后，输入如下代码： ```
function main(spreadsheetReport) {
    var list = spreadsheetReport.getSheetByName("Sheet1").getExpandedPositions("C3")//条形码字段所在单元格
    var cells = spreadsheetReport.workbook.worksheets.get("Sheet1").cells;
    for (var i = 0; i < list.length; i++) {
        var pos = list[i];
        var v = cells.get(pos.row, pos.column).value
        var check = 1;
        if (!v)
            continue;
        for (var j = 0; j < v.length(); j++) {
            var c = v.charCodeAt(j);
            if (c < 135) {
                c -= 32
            } else {
                c -= 100
            }
            check = (check + (j + 1) * c) % 103
        }
        if (check < 95 && check > 0) {
            check += 32
        } else if(check > 94) {
            check += 100
        }
        v = String.fromCharCode(204) + v + String.fromCharCode(check) + String.fromCharCode(206)
        cells.get(pos.row, pos.column).value = v;
    }
} 
```
  
下面的注意事项对code39和code128字体都适用。
1）如果按照以上的实现步骤操作，条形码无法正常显示，则需要将字体包添加到 \Smartbi\Tomcat\bin\Font-smartbi 文件夹下，并重启服务器，这样条形码就可在Smartbi中展示使用。
2）如果需要将条形码导出PDF文件，则服务器端一定要添加该字体包。  
