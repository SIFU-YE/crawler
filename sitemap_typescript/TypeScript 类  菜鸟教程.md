# 菜鸟教程 -- 学的不仅是技术，更是梦想！
TypeScript 教程
TypeScript 教程  TypeScript 安装  TypeScript 特性 TypeScript 基础语法  TypeScript 基本结构 TypeScript 基础类型  TypeScript 变量声明  TypeScript 运算符  TypeScript 条件语句  TypeScript 循环  TypeScript 函数  TypeScript Number  TypeScript String  TypeScript Array(数组)  TypeScript Map 对象 TypeScript 元组  TypeScript 联合类型  TypeScript 接口  TypeScript 对象  TypeScript 泛型 TypeScript 命名空间  TypeScript 模块  TypeScript 声明文件  TypeScript 测验 
# TypeScript 类
TypeScript 是面向对象的 JavaScript。
类描述了所创建的对象共同的属性和方法。
TypeScript 支持面向对象的所有特性，比如 类、接口等。
TypeScript 类定义方式如下：
```
class class_name {// 类作用域}
```

定义类的关键字为 class，后面紧跟类名，类可以包含以下几个模块（类的数据成员）：
  * **字段** − 字段是类里面声明的变量。字段表示对象的有关数据。
  * **构造函数** − 类实例化时调用，可以为类的对象分配内存。
  * **方法** − 方法为对象要执行的操作。


### 实例
创建一个 Person 类：
## TypeScript
classPerson{}
编译以上代码，得到以下 JavaScript 代码：
## JavaScript
varPerson/** @class */(function(){functionPerson(){}returnPerson}());
## 创建类的数据成员
以下实例我们声明了类 Car，包含字段为 engine，构造函数在类实例化后初始化字段 engine。
this 关键字表示当前类实例化的对象。注意构造函数的参数名与字段名相同，this.engine 表示类的字段。
此外我们也在类中定义了一个方法 disp()。
## TypeScript
classCar{//engine:string// 构造函数 constructor(engine:string){this.engineengine}//disp():void{console.log("发动机为 : "+this.engine)}}
编译以上代码，得到以下 JavaScript 代码：
## JavaScript
varCar/** @class */(function(){// 构造函数 functionCar(engine){this.engineengine}//Car.prototype.dispfunction(){console.log("发动机为 : "this.engine)}returnCar}());
## 创建实例化对象
我们使用 new 关键字来实例化类的对象，语法格式如下：
```
var object_name =new class_name([ arguments ])
```

类实例化时会调用构造函数，例如：
```
var obj =newCar("Engine 1")
```

类中的字段属性和方法可以使用 . 号来访问：
```
// 访问属性
obj.field_name 

// 访问方法
obj.function_name()
```

### 完整实例
以下实例创建来一个 Car 类，然后通过关键字 new 来创建一个对象并访问属性和方法：
## TypeScript
classCar{// 字段engine:string// 构造函数constructor(engine:string){this.engineengine}// 方法disp():void{console.log("函数中显示发动机型号 : "+this.engine)}}// 创建一个对象varobjnewCar("XXSY1")// 访问字段console.log("读取发动机型号 : "+obj.engine)// 访问方法obj.disp()
编译以上代码，得到以下 JavaScript 代码：
## JavaScript
varCar/** @class */(function(){// 构造函数functionCar(engine){this.engineengine}// 方法Car.prototype.dispfunction(){console.log("函数中显示发动机型号 : "this.engine)}returnCar}())// 创建一个对象varobjnewCar("XXSY1")// 访问字段console.log("读取发动机型号 : "obj.engine)// 访问方法obj.disp();
输出结果为：
```
读取发动机型号:  XXSY1
函数中显示发动机型号:   XXSY1
```

##  类的继承
TypeScript 支持继承类，即我们可以在创建类的时候继承一个已存在的类，这个已存在的类称为父类，继承它的类称为子类。
类继承使用关键字 extends，子类除了不能继承父类的私有成员(方法和属性)和构造函数，其他的都可以继承。
TypeScript 一次只能继承一个类，不支持继承多个类，但 TypeScript 支持多重继承（A 继承 B，B 继承 C）。
语法格式如下：
```
class child_class_name extends parent_class_name
```

### 实例
类的继承：实例中创建了 Shape 类，Circle 类继承了 Shape 类，Circle 类可以直接使用 Area 属性：
## TypeScript
classShape{Area:numberconstructor(a:number){this.Areaa}}classCircleextendsShape{disp():void{console.log("圆的面积: "+this.Area)}}varobjnewCircle(223)obj.disp()
编译以上代码，得到以下 JavaScript 代码：
## JavaScript
var__extends(thisthis.__extends)(function(){varextendStaticsfunction(db){extendStaticsObject.setPrototypeOf({__proto__[]}instanceofArrayfunction(db){d.__proto__b})function(db){for(varpinb)if(b.hasOwnProperty(p))d[p]b[p]}returnextendStatics(db)}returnfunction(db){extendStatics(db)function__(){this.constructord}d.prototypeb === nullObject.create(b)(__.prototypeb.prototypenew__())}})()varShape/** @class */(function(){functionShape(a){this.Areaa}returnShape}())varCircle/** @class */(function(_super){__extends(Circle_super)functionCircle(){return_super !== null_super.apply(thisarguments)this}Circle.prototype.dispfunction(){console.log("圆的面积: "this.Area)}returnCircle}(Shape))varobjnewCircle(223)obj.disp();
输出结果为：
```
圆的面积:223
```

需要注意的是子类只能继承一个父类，TypeScript 不支持继承多个类，但支持多重继承，如下实例：
## TypeScript
classRoot{str:string}classChildextendsRoot{}classLeafextendsChild{}// 多重继承，继承了 Child 和 Root 类varobjnewLeaf()obj.str"hello"console.log(obj.str)
编译以上代码，得到以下 JavaScript 代码：
## JavaScript
var__extends(thisthis.__extends)(function(){varextendStaticsfunction(db){extendStaticsObject.setPrototypeOf({__proto__[]}instanceofArrayfunction(db){d.__proto__b})function(db){for(varpinb)if(b.hasOwnProperty(p))d[p]b[p]}returnextendStatics(db)}returnfunction(db){extendStatics(db)function__(){this.constructord}d.prototypeb === nullObject.create(b)(__.prototypeb.prototypenew__())}})()varRoot/** @class */(function(){functionRoot(){}returnRoot}())varChild/** @class */(function(_super){__extends(Child_super)functionChild(){return_super !== null_super.apply(thisarguments)this}returnChild}(Root))varLeaf/** @class */(function(_super){__extends(Leaf_super)functionLeaf(){return_super !== null_super.apply(thisarguments)this}returnLeaf}(Child))// 多重继承，继承了 Child 和 Root 类varobjnewLeaf()obj.str"hello"console.log(obj.str);
输出结果为：
## 继承类的方法重写
类继承后，子类可以对父类的方法重新定义，这个过程称之为方法的重写。
其中 super 关键字是对父类的直接引用，该关键字可以引用父类的属性和方法。
## TypeScript
classPrinterClass{doPrint():void{console.log("父类的 doPrint() 方法。")}}classStringPrinterextendsPrinterClass{doPrint():void{super.doPrint()// 调用父类的函数console.log("子类的 doPrint()方法。")}}
编译以上代码，得到以下 JavaScript 代码：
## JavaScript
varobjnewStringPrinter()obj.doPrint()var__extends(thisthis.__extends)(function(){varextendStaticsfunction(db){extendStaticsObject.setPrototypeOf({__proto__[]}instanceofArrayfunction(db){d.__proto__b})function(db){for(varpinb)if(b.hasOwnProperty(p))d[p]b[p]}returnextendStatics(db)}returnfunction(db){extendStatics(db)function__(){this.constructord}d.prototypeb === nullObject.create(b)(__.prototypeb.prototypenew__())}})()varPrinterClass/** @class */(function(){functionPrinterClass(){}PrinterClass.prototype.doPrintfunction(){console.log("父类的 doPrint() 方法。")}returnPrinterClass}())varStringPrinter/** @class */(function(_super){__extends(StringPrinter_super)functionStringPrinter(){return_super !== null_super.apply(thisarguments)this}StringPrinter.prototype.doPrintfunction(){_super.prototype.doPrint.call(this)// 调用父类的函数console.log("子类的 doPrint()方法。")}returnStringPrinter}(PrinterClass))varobjnewStringPrinter()obj.doPrint();
输出结果为：
```
父类的 doPrint()方法。子类的 doPrint()方法。
```

## static 关键字
static 关键字用于定义类的数据成员（属性和方法）为静态的，静态成员可以直接通过类名调用。
## TypeScript
classStaticMem{staticnum:numberstaticdisp():void{console.log("num 值为 "StaticMem.num)}}StaticMem.num12// 初始化静态变量StaticMem.disp()// 调用静态方法
编译以上代码，得到以下 JavaScript 代码：
## JavaScript
varStaticMem/** @class */(function(){functionStaticMem(){}StaticMem.dispfunction(){console.log("num 值为 "StaticMem.num)}returnStaticMem}())StaticMem.num12// 初始化静态变量StaticMem.disp()// 调用静态方法
输出结果为：
## instanceof 运算符
instanceof 运算符用于判断对象是否是指定的类型，如果是返回 true，否则返回 false。
## TypeScript
classPerson{}varobjnewPerson()varisPersonobjinstanceofPersonconsole.log("obj 对象是 Person 类实例化来的吗？ "isPerson);
编译以上代码，得到以下 JavaScript 代码：
## JavaScript
varPerson/** @class */(function(){functionPerson(){}returnPerson}())varobjnewPerson()varisPersonobjinstanceofPersonconsole.log(" obj 对象是 Person 类实例化来的吗？ "isPerson);
输出结果为：
```
obj 对象是Person类实例化来的吗？true
```

##  访问控制修饰符 
TypeScript 中，可以使用访问控制符来保护对类、变量、方法和构造方法的访问。TypeScript 支持 3 种不同的访问权限。
  * **public（默认）** : 公有，可以在任何地方被访问。
  * **protected** : 受保护，可以被其自身以及其子类访问。
  * **private** : 私有，只能被其定义所在的类访问。


以下实例定义了两个变量 str1 和 str2，str1 为 public，str2 为 private，实例化后可以访问 str1，如果要访问 str2 则会编译错误。
## TypeScript
classEncapsulate{str1:string"hello"privatestr2:string"world"}varobjnewEncapsulate()console.log(obj.str1)// 可访问 console.log(obj.str2)// 编译错误， str2 是私有的
## 类和接口
类可以实现接口，使用关键字 implements，并将 interest 字段作为类的属性使用。
以下实例中 AgriLoan 类实现了 ILoan 接口：
## TypeScript
interfaceILoan{interest:number}classAgriLoanimplementsILoan{interest:numberrebate:numberconstructor(interest:number,rebate:number){this.interestinterestthis.rebaterebate}}varobjnewAgriLoan(10,1)console.log("利润为 : "+obj.interest+"，抽成为 : "+obj.rebate)
编译以上代码，得到以下 JavaScript 代码：
## JavaScript
varAgriLoan/** @class */(function(){functionAgriLoan(interestrebate){this.interestinterestthis.rebaterebate}returnAgriLoan}())varobjnewAgriLoan(101)console.log("利润为 : "obj.interest"，抽成为 : "obj.rebate);
输出结果为：
```
利润为:10，抽成为:1
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


