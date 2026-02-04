# 菜鸟教程 -- 学的不仅是技术，更是梦想！
TypeScript 教程
TypeScript 教程  TypeScript 安装  TypeScript 特性 TypeScript 基础语法  TypeScript 基本结构 TypeScript 基础类型  TypeScript 变量声明  TypeScript 运算符  TypeScript 条件语句  TypeScript 循环  TypeScript 函数  TypeScript Number  TypeScript String  TypeScript Array(数组)  TypeScript Map 对象 TypeScript 元组  TypeScript 联合类型  TypeScript 接口  TypeScript 类  TypeScript 泛型 TypeScript 命名空间  TypeScript 模块  TypeScript 声明文件  TypeScript 测验 
# TypeScript 对象 
对象是包含一组键值对的实例。 值可以是标量、函数、数组、对象等，如下实例：
varobject_name{key1"value1"// 标量key2"value"key3function(){// 函数}key4:["content1""content2"]//集合}
以上对象包含了标量，函数，集合(数组或元组)。
### 对象实例
## TypeScript
varsites{site1:"Runoob"site2:"Google"}// 访问对象的值console.log(sites.site1)console.log(sites.site2)
编译以上代码，得到以下 JavaScript 代码：
## JavaScript
varsites{site1:"Runoob"site2:"Google"}// 访问对象的值console.log(sites.site1)console.log(sites.site2)
输出结果为：
```
RunoobGoogle
```

## TypeScript 类型模板
假如我们在 JavaScript 定义了一个对象：
varsites{site1:"Runoob"site2:"Google"};
这时如果我们想在对象中添加方法，可以做以下修改：
```
sites.sayHello =function(){return"hello";}
```

如果在 TypeScript 中使用以上方式则会出现编译错误，因为Typescript 中的对象必须是特定类型的实例。
## TypeScript
varsites{site1"Runoob"site2"Google"sayHellofunction(){}// 类型模板}sites.sayHellofunction(){console.log("hello "sites.site1)}sites.sayHello();
编译以上代码，得到以下 JavaScript 代码：
## JavaScript
varsites{site1"Runoob"site2"Google"sayHellofunction(){}// 类型模板}sites.sayHellofunction(){console.log("hello "sites.site1)}sites.sayHello();
输出结果为：
```
hello Runoob
```

此外对象也可以作为一个参数传递给函数，如下实例：
## TypeScript
varsites{site1:"Runoob"site2:"Google"}varinvokesitesfunction(obj{site1:stringsite2string}){console.log("site1 :"+obj.site1)console.log("site2 :"+obj.site2)}invokesites(sites)
编译以上代码，得到以下 JavaScript 代码：
## JavaScript
varsites{site1"Runoob"site2"Google"}varinvokesitesfunction(obj){console.log("site1 :"obj.site1)console.log("site2 :"obj.site2)}invokesites(sites);
输出结果为：
```
site1 :Runoob
site2 :Google
```

##  鸭子类型(Duck Typing)
鸭子类型（英语：duck typing）是动态类型的一种风格，是多态(polymorphism)的一种形式。
在这种风格中，一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由"当前方法和属性的集合"决定。
> 可以这样表述：
> "当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。"
在鸭子类型中，关注点在于对象的行为能做什么，而不是关注对象所属的类型。例如，在不使用鸭子类型的语言中，我们可以编写一个函数，它接受一个类型为"鸭子"的对象，并调用它的"走"和"叫"方法。在使用鸭子类型的语言中，这样的一个函数可以接受一个任意类型的对象，并调用它的"走"和"叫"方法。如果这些需要被调用的方法不存在，那么将引发一个运行时错误。任何拥有这样的正确的"走"和"叫"方法的对象都可被函数接受的这种行为引出了以上表述，这种决定类型的方式因此得名。
interfaceIPoint{x:numbery:number}functionaddPoints(p1:IPoint,p2:IPoint):IPoint{varxp1.xp2.xvaryp1.yp2.yreturn{x:x,y:y}}// 正确varnewPointaddPoints({x:3,y:4},{x:5,y:1})//varnewPoint2addPoints({x:1},{x:4,y:3})
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


