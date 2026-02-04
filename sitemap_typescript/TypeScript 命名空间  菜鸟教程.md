# 菜鸟教程 -- 学的不仅是技术，更是梦想！
TypeScript 教程
TypeScript 教程  TypeScript 安装  TypeScript 特性 TypeScript 基础语法  TypeScript 基本结构 TypeScript 基础类型  TypeScript 变量声明  TypeScript 运算符  TypeScript 条件语句  TypeScript 循环  TypeScript 函数  TypeScript Number  TypeScript String  TypeScript Array(数组)  TypeScript Map 对象 TypeScript 元组  TypeScript 联合类型  TypeScript 接口  TypeScript 类  TypeScript 对象  TypeScript 泛型 TypeScript 模块  TypeScript 声明文件  TypeScript 测验 
# TypeScript 命名空间 
命名空间一个最明确的目的就是解决重名问题。
假设这样一种情况，当一个班上有两个名叫小明的学生时，为了明确区分它们，我们在使用名字之外，不得不使用一些额外的信息，比如他们的姓（王小明，李小明），或者他们父母的名字等等。
命名空间定义了标识符的可见范围，一个标识符可在多个命名空间中定义，它在不同命名空间中的含义是互不相干的。这样，在一个新的命名空间中可定义任何标识符，它们不会与任何已有的标识符发生冲突，因为已有的定义都处于其他命名空间中。
TypeScript 中命名空间使用 namespace 来定义，语法格式如下：
namespaceSomeNameSpaceName{exportinterfaceISomeInterfaceName{}exportclassSomeClassName{}}
以上定义了一个命名空间 SomeNameSpaceName，如果我们需要在外部可以调用 SomeNameSpaceName 中的类和接口，则需要在类和接口添加 export 关键字。
要在另外一个命名空间调用语法格式为：
```
SomeNameSpaceName.SomeClassName;
```

如果一个命名空间在一个单独的 TypeScript 文件中，则应使用三斜杠 /// 引用它，语法格式如下：
```
/// <reference path = "SomeFileName.ts" />
```

以下实例演示了命名空间的使用，定义在不同文件中：
## IShape.ts 文件代码：
namespaceDrawing{exportinterfaceIShape{draw()}}
## Circle.ts 文件代码：
/// <reference path = "IShape.ts" /> namespaceDrawing{exportclassCircleimplementsIShape{publicdraw(){console.log("Circle is drawn")}}}
## Triangle.ts 文件代码：
/// <reference path = "IShape.ts" /> namespaceDrawing{exportclassTriangleimplementsIShape{publicdraw(){console.log("Triangle is drawn")}}}
## TestShape.ts 文件代码：
/// <reference path = "IShape.ts" /> /// <reference path = "Circle.ts" /> /// <reference path = "Triangle.ts" /> functiondrawAllShapes(shape:Drawing.IShape){shape.draw()}drawAllShapes(newDrawing.Circle())drawAllShapes(newDrawing.Triangle());
使用 tsc 命令编译以上代码：
```
tsc --out app.js TestShape.
```

得到以下 JavaScript 代码：
## JavaScript
/// <reference path = "IShape.ts" /> varDrawing(function(Drawing){varCircle/** @class */(function(){functionCircle(){}Circle.prototype.drawfunction(){console.log("Circle is drawn")}returnCircle}())Drawing.CircleCircle})(Drawing(Drawing{}))/// <reference path = "IShape.ts" /> varDrawing(function(Drawing){varTriangle/** @class */(function(){functionTriangle(){}Triangle.prototype.drawfunction(){console.log("Triangle is drawn")}returnTriangle}())Drawing.TriangleTriangle})(Drawing(Drawing{}))/// <reference path = "IShape.ts" /> /// <reference path = "Circle.ts" /> /// <reference path = "Triangle.ts" /> functiondrawAllShapes(shape){shape.draw()}drawAllShapes(newDrawing.Circle())drawAllShapes(newDrawing.Triangle());
使用 node 命令查看输出结果为：
```
$ node app.js
Circleis drawn
Triangleis drawn
```

##  嵌套命名空间
命名空间支持嵌套，即你可以将命名空间定义在另外一个命名空间里头。
namespacenamespace_name1{exportnamespacenamespace_name2{exportclassclass_name{}}}
成员的访问使用点号 . 来实现，如下实例：
## Invoice.ts 文件代码：
namespaceRunoob{exportnamespaceinvoiceApp{exportclassInvoice{publiccalculateDiscount(pricenumber){returnprice.40}}}}
## InvoiceTest.ts 文件代码：
/// <reference path = "Invoice.ts" />varinvoicenewRunoob.invoiceApp.Invoice()console.log(invoice.calculateDiscount(500));
使用 tsc 命令编译以上代码：
```
tsc --out app.js InvoiceTest.ts
```

得到以下 JavaScript 代码：
## JavaScript
varRunoob(function(Runoob){varinvoiceApp(function(invoiceApp){varInvoice/** @class */(function(){functionInvoice(){}Invoice.prototype.calculateDiscountfunction(price){returnprice.40}returnInvoice}())invoiceApp.InvoiceInvoice})(invoiceAppRunoob.invoiceApp(Runoob.invoiceApp{}))})(Runoob(Runoob{}))/// <reference path = "Invoice.ts" />varinvoicenewRunoob.invoiceApp.Invoice()console.log(invoice.calculateDiscount(500));
使用 node 命令查看输出结果为：
```
$ node app.js
200
```

  * HTML / CSS
  * JavaScript
  * 服务端
  * 数据库
  * AI & 数据分析
  * 移动端
  * 开发工具
  * XML 教程
  * ASP.NET
  * Web Service
  * 网站建设


