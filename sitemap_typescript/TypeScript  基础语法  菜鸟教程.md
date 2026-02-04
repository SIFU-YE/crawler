# 菜鸟教程 -- 学的不仅是技术，更是梦想！
TypeScript 教程
TypeScript 教程  TypeScript 安装  TypeScript 特性 TypeScript 基本结构 TypeScript 基础类型  TypeScript 变量声明  TypeScript 运算符  TypeScript 条件语句  TypeScript 循环  TypeScript 函数  TypeScript Number  TypeScript String  TypeScript Array(数组)  TypeScript Map 对象 TypeScript 元组  TypeScript 联合类型  TypeScript 接口  TypeScript 类  TypeScript 对象  TypeScript 泛型 TypeScript 命名空间  TypeScript 模块  TypeScript 声明文件  TypeScript 测验 
深入探索
jQuery UI
Web 应用框架
# TypeScript 基础语法 
TypeScript 程序由以下几个部分组成：
  * 模块
  * 函数
  * 变量
  * 语句和表达式
  * 注释


###  第一个 TypeScript 程序 
我们可以使用以下 TypeScript 程序来输出 "Hello World" ：
## Runoob.ts 文件代码：
consthellostring"Hello World!"console.log(hello)
尝试一下 »
以上代码首先通过 **tsc** 命令编译：
```
tsc Runoob.ts
```

得到如下 js 代码：
## Runoob.js 文件代码：
varhello"Hello World!"console.log(hello);
最后我们使用 node 命令来执行该 js 代码。
```
$ node Runoob.js
HelloWorld
```

整个流程如下图所示：
我们可以同时编译多个 ts 文件：
```
tsc file1.ts file2.ts file3.ts
```

tsc 常用编译参数如下表所示：
序号 | 编译参数说明  
---|---  
1. |  **--help** 显示帮助信息  
2. |  **--module** 载入扩展模块  
3. |  **--target** 设置 ECMA 版本  
4. |  **--declaration** 额外生成一个 .d.ts 扩展名的文件。 ```
tsc ts-hw.ts --declaration
```
以上命令会生成 ts-hw.d.ts、ts-hw.js 两个文件。  
5. |  **--removeComments** 删除文件的注释  
6. |  **--out** 编译多个文件并合并到一个输出的文件  
7. |  **--sourcemap** 生成一个 sourcemap (.map) 文件。 sourcemap 是一个存储源代码与编译代码对应位置映射的信息文件。  
8. |  **--module noImplicitAny** 在表达式和声明上有隐含的 any 类型时报错  
9. |  **--watch** 在监视模式下运行编译器。会监视输出文件，在它们改变时重新编译。  
## TypeScript 保留关键字
TypeScript 保留关键字如下表所示：
`abstract` | 用于定义抽象类或抽象方法。  
---|---  
表示任意类型，禁用类型检查。  
类型断言，用于将某种类型转换为另一种类型。  
用于异步函数中，暂停代码执行直到 Promise 解决。  
`boolean` | 表示布尔类型。  
退出循环或 switch 语句。  
用于 switch 语句中的分支。  
用于捕获异常。  
用于定义类。  
定义常量变量。  
`continue` | 跳过当前循环，继续下一次循环。  
`debugger` | 启动调试器，暂停代码执行。  
`declare` | 声明一个变量或模块，通常用于类型声明文件。  
`default` | 定义 switch 语句的默认分支。  
`delete` | 删除对象的属性或数组的元素。  
用于 `do...while` 循环。  
定义条件语句中的 else 部分。  
定义枚举类型。  
`export` | 用于从模块中导出变量、函数或类。  
`extends` | 用于类的继承，表示类继承其他类。  
布尔值 `false`。  
`finally` | 定义 `try...catch` 语句中的最终执行代码块。  
用于 `for` 循环。  
用于模块导入语句，指定模块的来源。  
`function` | 定义函数。  
用于对象的 getter 方法。  
用于条件判断。  
`implements` | 用于类实现接口。  
`import` | 用于从模块中导入内容。  
用于检查对象中是否包含指定的属性，或用于 `for...in` 循环。  
用于条件类型中推断类型。  
`instanceof` | 检查对象是否是指定类的实例。  
`interface` | 用于定义接口。  
定义块级作用域的变量。  
`module` | 定义模块（在较早的 TypeScript 版本中使用）。  
`namespace` | 定义命名空间（在较早的 TypeScript 版本中使用）。  
创建类的实例。  
表示空值。  
`number` | 表示数字类型。  
`object` | 表示非原始类型。  
用于 `for...of` 循环。  
`package` | 用于模块系统，标识包。  
`private` | 用于类成员的访问修饰符，表示私有。  
`protected` | 用于类成员的访问修饰符，表示受保护的。  
`public` | 用于类成员的访问修饰符，表示公共的。  
`readonly` | 表示只读属性。  
`require` | 用于导入 CommonJS 模块。  
`return` | 退出函数并可返回值。  
用于对象的 setter 方法。  
`string` | 表示字符串类型。  
用于调用父类的方法或构造函数。  
`switch` | 用于 switch 语句。  
`symbol` | 表示符号类型。  
引用当前类或对象的实例。  
抛出异常。  
用于异常处理语句 `try...catch`。  
布尔值 `true`。  
用于定义类型别名。  
`typeof` | 获取变量或表达式的类型。  
`undefined` | 表示未定义的值。  
`unique` | 用于 `symbol` 类型的唯一标识符。  
用于声明变量（已不推荐使用）。  
表示没有返回值的类型。  
用于 `while` 循环。  
用于创建一个作用域，在该作用域内可以省略对象的引用（不推荐使用）。  
用于生成器函数中，暂停和恢复生成器的执行。  
###  空白和换行
TypeScript 会忽略程序中出现的空格、制表符和换行符。 
空格、制表符通常用来缩进代码，使代码易于阅读和理解。
### TypeScript 区分大小写
TypeScript 区分大写和小写字符。
### 分号是可选的
每行指令都是一段语句，你可以使用分号或不使用， 分号在 TypeScript 中是可选的，建议使用。
以下代码都是合法的：
```
console.log("Runoob")
console.log("Google");
```

如果语句写在同一行则一定需要使用分号来分隔，否则会报错，如：
```
console.log("Runoob");console.log("Google");
```

### TypeScript 注释
注释是一个良好的习惯，虽然很多程序员讨厌注释，但还是建议你在每段代码写上文字说明。
注释可以提高程序的可读性。 
注释可以包含有关程序一些信息，如代码的作者，有关函数的说明等。
编译器会忽略注释。
### TypeScript 支持两种类型的注释
  * **单行注释 ( // )** − 在 // 后面的文字都是注释内容。
  * **多行注释 (/* */)** − 这种注释可以跨越多行。


注释实例：
```
// 这是一个单行注释/* 
 这是一个多行注释 
 这是一个多行注释 
 这是一个多行注释 
*/
```

## TypeScript 与面向对象
面向对象是一种对现实世界理解和抽象的方法。
TypeScript 是一种面向对象的编程语言。 
面向对象主要有两个概念：对象和类。
  * **对象** ：对象是类的一个实例（**对象不是找个女朋友** ），有状态和行为。例如，一条狗是一个对象，它的状态有：颜色、名字、品种；行为有：摇尾巴、叫、吃等。
  * **类** ：类是一个模板，它描述一类对象的行为和状态。
  * **方法** ：方法是类的操作的实现步骤。


下图中 **girl、boy** 为类，而具体的每个人为该类的对象：
TypeScript 面向对象编程实例：
classSite{name():void{console.log("Runoob")}}varobjnewSite()obj.name();
以上实例定义了一个类 Site，该类有一个方法 name()，该方法在终端上输出字符串 Runoob。 
new 关键字创建类的对象，该对象调用方法 name()。
编译后生成的 JavaScript 代码如下：
varSite/** @class */(function(){functionSite(){}Site.prototype.namefunction(){console.log("Runoob")}returnSite}())varobjnewSite()obj.name();
执行以上 JavaScript 代码，输出结果如下:
```
Runoob
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


深入探索
Web应用框架
Web 应用框架
