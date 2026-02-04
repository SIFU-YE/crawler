# 菜鸟教程 -- 学的不仅是技术，更是梦想！
TypeScript 教程
TypeScript 教程  TypeScript 安装  TypeScript 特性 TypeScript 基础语法  TypeScript 基本结构 TypeScript 基础类型  TypeScript 变量声明  TypeScript 运算符  TypeScript 条件语句  TypeScript 循环  TypeScript 函数  TypeScript Number  TypeScript String  TypeScript Array(数组)  TypeScript Map 对象 TypeScript 元组  TypeScript 联合类型  TypeScript 类  TypeScript 对象  TypeScript 泛型 TypeScript 命名空间  TypeScript 模块  TypeScript 声明文件  TypeScript 测验 
# TypeScript 接口
接口是一系列抽象方法的声明，是一些方法特征的集合，这些方法都应该是抽象的，需要由具体的类去实现，然后第三方就可以通过这组抽象方法调用，让具体的类执行具体的方法。
TypeScript 接口定义如下：
```
interface interface_name {}
```

### 实例
以下实例中，我们定义了一个接口 IPerson，接着定义了一个变量 customer，它的类型是 IPerson。
customer 实现了接口 IPerson 的属性和方法。
## TypeScript
interfaceIPerson{firstName:stringlastName:stringsayHi()string}varcustomer:IPerson{firstName:"Tom"lastName:"Hanks"sayHi():string{return"Hi there"}}console.log("Customer 对象 ")console.log(customer.firstName)console.log(customer.lastName)console.log(customer.sayHi())varemployee:IPerson{firstName:"Jim"lastName:"Blakes"sayHi():string{return"Hello!!!"}}console.log("Employee 对象 ")console.log(employee.firstName)console.log(employee.lastName)
需要注意接口不能转换为 JavaScript。 它只是 TypeScript 的一部分。
编译以上代码，得到以下 JavaScript 代码：
## JavaScript
varcustomer{firstName"Tom"lastName"Hanks"sayHifunction(){return"Hi there"}}console.log("Customer 对象 ")console.log(customer.firstName)console.log(customer.lastName)console.log(customer.sayHi())varemployee{firstName"Jim"lastName"Blakes"sayHifunction(){return"Hello!!!"}}console.log("Employee 对象 ")console.log(employee.firstName)console.log(employee.lastName);
输出结果为：
```
Customer对象TomHanksHi there
Employee对象JimBlakes
```

## 联合类型和接口
以下实例演示了如何在接口中使用联合类型：
## TypeScript
interfaceRunOptions{program:stringcommandline:string[]|string|(()string)}// commandline 是字符串varoptions:RunOptions{program:"test1",commandline:"Hello"}console.log(options.commandline)// commandline 是字符串数组options{program:"test1",commandline:["Hello","World"]}console.log(options.commandline[0])console.log(options.commandline[1])// commandline 是一个函数表达式options{program:"test1",commandline:(){return"**Hello World**";}}varfn:anyoptions.commandlineconsole.log(fn());
编译以上代码，得到以下 JavaScript 代码：
## JavaScript
// commandline 是字符串varoptions{program"test1"commandline"Hello"}console.log(options.commandline)// commandline 是字符串数组options{program"test1"commandline["Hello""World"]}console.log(options.commandline[0])console.log(options.commandline[1])// commandline 是一个函数表达式options{program"test1"commandlinefunction(){return"**Hello World**"}}varfnoptions.commandlineconsole.log(fn());
输出结果为：
```
HelloHelloWorld**HelloWorld**
```

## 接口和数组
接口中我们可以将数组的索引值和元素设置为不同类型，索引值可以是数字或字符串。
设置元素为字符串类型：
## 实例
interfacenamelist{[index:number]:string}// 类型一致，正确varlist2:namelist["Google","Runoob","Taobao"]// 错误元素 1 不是 string 类型// var list2:namelist = ["Runoob",1,"Taobao"]
如果使用了其他类型会报错：
## 实例
interfacenamelist{[index:number]:string}// 类型一致，正确// var list2:namelist = ["Google","Runoob","Taobao"]// 错误元素 1 不是 string 类型varlist2:namelist["John",1,"Bran"]
执行后报错如下，显示类型不一致： ```
test.ts:8:30- error TS2322:Type'number'isnot assignable to type 'string'.8var list2:namelist =["John",1,"Bran"]~

  test.ts:2:42[index:number]:string~~~~~~~~~~~~~~~~~~~~~The expected type comes fromthis index signature.Found1 error.
```

## TypeScript
interfaceages{[index:string]:number}varagelist:ages// 类型正确 agelist["runoob"]15// 类型错误，输出 error TS2322: Type '"google"' is not assignable to type 'number'.// agelist[2] = "google"
## 接口继承
接口继承就是说接口可以通过其他接口来扩展自己。
Typescript 允许接口继承多个接口。
继承使用关键字 extends。
单接口继承语法格式：
```
Child_interface_nameextends super_interface_name
```

多接口继承语法格式：
```
Child_interface_nameextends super_interface1_name, super_interface2_name,…,super_interfaceN_name
```

继承的各个接口使用逗号 , 分隔。
### 单继承实例
## TypeScript
interfacePerson{age:number}interfaceMusicianextendsPerson{instrument:string}vardrummerMusician{}drummer.age27drummer.instrument"Drums"console.log("年龄: "+drummer.age)console.log("喜欢的乐器: "+drummer.instrument)
编译以上代码，得到以下 JavaScript 代码：
## JavaScript
vardrummer{}drummer.age27drummer.instrument"Drums"console.log("年龄: "drummer.age)console.log("喜欢的乐器: "drummer.instrument);
输出结果为：
```
年龄:27喜欢的乐器:Drums
```

### 多继承实例
## TypeScript
interfaceIParent1{v1:number}interfaceIParent2{v2:number}interfaceChildextendsIParent1IParent2{}varIobj:Child{v1:12v2:23}console.log("value 1: "+Iobj.v1+" value 2: "+Iobj.v2)
编译以上代码，得到以下 JavaScript 代码：
## JavaScript
varIobj{v112v223}console.log("value 1: "Iobj.v1" value 2: "Iobj.v2);
输出结果为：
```
value 1:12 value 2:23
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


