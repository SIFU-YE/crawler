# 菜鸟教程 -- 学的不仅是技术，更是梦想！
TypeScript 教程
TypeScript 教程  TypeScript 安装  TypeScript 特性 TypeScript 基础语法  TypeScript 基本结构 TypeScript 基础类型  TypeScript 变量声明  TypeScript 运算符  TypeScript 条件语句  TypeScript 循环  TypeScript 函数  TypeScript Number  TypeScript String  TypeScript Array(数组)  TypeScript Map 对象 TypeScript 元组  TypeScript 联合类型  TypeScript 接口  TypeScript 类  TypeScript 对象  TypeScript 泛型 TypeScript 命名空间  TypeScript 声明文件  TypeScript 测验 
# TypeScript 模块
TypeScript 模块的设计理念是可以更换的组织代码。
模块是在其自身的作用域里执行，并不是在全局作用域，这意味着定义在模块里面的变量、函数和类等在模块外部是不可见的，除非明确地使用 export 导出它们。类似地，我们必须通过 import 导入其他模块导出的变量、函数、类等。
两个模块之间的关系是通过在文件级别上使用 import 和 export 建立的。
模块使用模块加载器去导入其它的模块。 在运行时，模块加载器的作用是在执行此模块代码前去查找并执行这个模块的所有依赖。 大家最熟知的JavaScript模块加载器是服务于 Node.js 的 CommonJS 和服务于 Web 应用的 Require.js。
此外还有有 SystemJs 和 Webpack。
模块导出使用关键字 export 关键字，语法格式如下：
// 文件名 : SomeInterface.ts exportinterfaceSomeInterface{// 代码部分}
要在另外一个文件使用该模块就需要使用 import 关键字来导入:
importsomeInterfaceRefrequire("./SomeInterface");
### 实例
## IShape.ts 文件代码：
/// <reference path = "IShape.ts" /> exportinterfaceIShape{draw()}
## Circle.ts 文件代码：
importshaperequire("./IShape")exportclassCircleimplementsshape.IShape{publicdraw(){console.log("Cirlce is drawn (external module)")}}
## Triangle.ts 文件代码：
importshaperequire("./IShape")exportclassTriangleimplementsshape.IShape{publicdraw(){console.log("Triangle is drawn (external module)")}}
## TestShape.ts 文件代码：
importshaperequire("./IShape")importcirclerequire("./Circle")importtrianglerequire("./Triangle")functiondrawAllShapes(shapeToDrawshape.IShape){shapeToDraw.draw()}drawAllShapes(newcircle.Circle())drawAllShapes(newtriangle.Triangle());
使用 tsc 命令编译以上代码（AMD）：
```
tsc --module amd TestShape.ts 
```

得到以下 JavaScript 代码：
## IShape.js 文件代码：
define(["require""exports"]function(requireexports){});
## Circle.js 文件代码：
define(["require""exports"]function(requireexports){varCircle(function(){functionCircle(){}Circle.prototype.drawfunction(){console.log("Cirlce is drawn (external module)")}returnCircle})()exports.CircleCircle});
## Triangle.js 文件代码：
define(["require""exports"]function(requireexports){varTriangle(function(){functionTriangle(){}Triangle.prototype.drawfunction(){console.log("Triangle is drawn (external module)")}returnTriangle})()exports.TriangleTriangle});
## TestShape.js 文件代码：
define(["require""exports""./Circle""./Triangle"]function(requireexportscircletriangle){functiondrawAllShapes(shapeToDraw){shapeToDraw.draw()}drawAllShapes(newcircle.Circle())drawAllShapes(newtriangle.Triangle())});
使用 tsc 命令编译以上代码（Commonjs）：
```
tsc --module commonjs TestShape.ts
```

得到以下 JavaScript 代码：
## Circle.js 文件代码：
varCircle(function(){functionCircle(){}Circle.prototype.drawfunction(){console.log("Cirlce is drawn")}returnCircle})()exports.CircleCircle;
## Triangle.js 文件代码：
varTriangle(function(){functionTriangle(){}Triangle.prototype.drawfunction(){console.log("Triangle is drawn (external module)")}returnTriangle})()exports.TriangleTriangle;
## TestShape.js 文件代码：
varcirclerequire("./Circle")vartrianglerequire("./Triangle")functiondrawAllShapes(shapeToDraw){shapeToDraw.draw()}drawAllShapes(newcircle.Circle())drawAllShapes(newtriangle.Triangle());
输出结果为：
```
Cirlceis drawn (external module)Triangleis drawn (external module)
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


