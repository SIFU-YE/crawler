# 菜鸟教程 -- 学的不仅是技术，更是梦想！
TypeScript 教程
TypeScript 教程  TypeScript 安装  TypeScript 特性 TypeScript 基础语法  TypeScript 基本结构 TypeScript 基础类型  TypeScript 变量声明  TypeScript 运算符  TypeScript 条件语句  TypeScript 循环  TypeScript 函数  TypeScript Number  TypeScript String  TypeScript Array(数组)  TypeScript Map 对象 TypeScript 元组  TypeScript 接口  TypeScript 类  TypeScript 对象  TypeScript 泛型 TypeScript 命名空间  TypeScript 模块  TypeScript 声明文件  TypeScript 测验 
# TypeScript 联合类型
联合类型（Union Types）可以通过管道(|)将变量设置多种类型，赋值时可以根据设置的类型来赋值。
**注意** ：只能赋值指定的类型，如果赋值其它类型就会报错。
创建联合类型的语法格式如下：
```
Type1|Type2|Type3
```

### 实例
声明一个联合类型：
## TypeScript
varval:string|numberval12console.log("数字为 "val)val"Runoob"console.log("字符串为 "val)
编译以上代码，得到以下 JavaScript 代码：
## JavaScript
varvalval12console.log("数字为 "val)val"Runoob"console.log("字符串为 "val);
输出结果为：
```
数字为12字符串为Runoob
```

如果赋值其它类型就会报错：
```
var val:string|number 
val =true
```

也可以将联合类型作为函数参数使用：
## TypeScript
编译以上代码，得到以下 JavaScript 代码：
## JavaScript
输出结果为：
```
```

## 联合类型数组
我们也可以将数组声明为联合类型：
## TypeScript
vararr:number[]|string[]vari:numberarr[1,2,4]console.log("**数字数组**")for(i0;iarr.length;i++){console.log(arr[i])}arr["Runoob","Google","Taobao"]console.log("**字符串数组**")for(i0;iarr.length;i++){console.log(arr[i])}
编译以上代码，得到以下 JavaScript 代码：
## JavaScript
vararrvariarr[124]console.log("**数字数组**")for(i0iarr.lengthi++){console.log(arr[i])}arr["Runoob""Google""Taobao"]console.log("**字符串数组**")for(i0iarr.lengthi++){console.log(arr[i])}
输出结果为：
```
**数字数组**124**字符串数组**RunoobGoogleTaobao
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


