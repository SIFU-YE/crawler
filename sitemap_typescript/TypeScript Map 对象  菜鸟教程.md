# 菜鸟教程 -- 学的不仅是技术，更是梦想！
TypeScript 教程
TypeScript 教程  TypeScript 安装  TypeScript 特性 TypeScript 基础语法  TypeScript 基本结构 TypeScript 基础类型  TypeScript 变量声明  TypeScript 运算符  TypeScript 条件语句  TypeScript 循环  TypeScript 函数  TypeScript Number  TypeScript String  TypeScript Array(数组)  TypeScript 元组  TypeScript 联合类型  TypeScript 接口  TypeScript 类  TypeScript 对象  TypeScript 泛型 TypeScript 命名空间  TypeScript 模块  TypeScript 声明文件  TypeScript 测验 
# TypeScript Map 对象
Map 对象保存键值对，并且能够记住键的原始插入顺序。
任何值(对象或者原始值) 都可以作为一个键或一个值。
Map 是 ES6 中引入的一种新的数据结构，可以参考 ES6 Map 与 Set。
## 创建 Map
TypeScript 使用 Map 类型和 new 关键字来创建 Map：
```
let myMap =newMap();
```

初始化 Map，可以以数组的格式来传入键值对：
```
let myMap =newMap([["key1","value1"],["key2","value2"]]);
```

Map 相关的函数与属性：
  * map.clear() – 移除 Map 对象的所有键/值对 。
  * map.set() – 设置键值对，返回该 Map 对象。
  * map.get() – 返回键对应的值，如果不存在，则返回 undefined。
  * map.has() – 返回一个布尔值，用于判断 Map 中是否包含键对应的值。
  * map.delete() – 删除 Map 中的元素，删除成功返回 true，失败返回 false。
  * map.size – 返回 Map 对象键/值对的数量。
  * map.keys() - 返回一个 Iterator 对象， 包含了 Map 对象中每个元素的键 。
  * map.values() – 返回一个新的Iterator对象，包含了Map对象中每个元素的值 。
  * map.entries() – 返回一个包含 Map 中所有键值对的迭代器 。


### 常用函数
**set(key: K, value: V): this** - 向 Map 中添加或更新键值对。
```
map.set('key1','value1');
```

**get(key: K): V | undefined** - 根据键获取值，如果键不存在则返回 undefined。
```
const value = map.get('key1');
```

**has(key: K): boolean** - 检查 Map 中是否存在指定的键。
```
const exists = map.has('key1');
```

**delete(key: K): boolean** - 删除指定键的键值对，成功删除返回 true，否则返回 false。
```
const removed = map.delete('key1');
```

**clear(): void** - 清空 Map 中的所有键值对。
```
map.clear();
```

**size: number** - 返回 Map 中键值对的数量。
```
const size = map.size;
```

### 迭代方法
keys(): IterableIterator<K> - 返回一个包含 Map 中所有键的迭代器。 ```
for(const key of map.keys()){
  console.log(key);}
```

**values(): IterableIterator <V>** - 返回一个包含 Map 中所有值的迭代器。
```
for(const value of map.values()){
  console.log(value);}
```

**entries(): IterableIterator <[K, V]>** - 返回一个包含 Map 中所有键值对的迭代器，每个元素是一个 [key, value] 数组。
```
for(const[key, value] of map.entries()){
  console.log(key, value);}
```

**forEach(callbackfn: (value: V, key: K, map: Map <K, V>) => void, thisArg?: any): void** - 对 Map 中的每个键值对执行一次提供的回调函数。
```
map.forEach((value, key){
  console.log(key, value);});
```

### 实例
## 实例
const map = new Mapstring, number(); map.set('one', 1); map.set('two', 2); console.log(map.get('one')); // 输出: 1 console.log(map.has('two')); // 输出: true map.delete('one'); console.log(map.size); // 输出: 1 map.forEach((value, key) { console.log(key, value); // 输出: two 2 }); map.clear(); console.log(map.size); // 输出: 0
## 实例 - test.ts 文件
letnameSiteMappingnewMap()// 设置 Map 对象nameSiteMapping.set("Google"1)nameSiteMapping.set("Runoob"2)nameSiteMapping.set("Taobao"3)// 获取键对应的值console.log(nameSiteMapping.get("Runoob"))//// 判断 Map 中是否包含键对应的值console.log(nameSiteMapping.has("Taobao"))// trueconsole.log(nameSiteMapping.has("Zhihu"))// false// 返回 Map 对象键/值对的数量console.log(nameSiteMapping.size)//// 删除 Runoobconsole.log(nameSiteMapping.delete("Runoob"))// trueconsole.log(nameSiteMapping)// 移除 Map 对象的所有键/值对nameSiteMapping.clear()// 清除 Mapconsole.log(nameSiteMapping);
使用 **es6** 编译：
```
tsc --target es6 test.ts
```

编译以上代码得到如下 JavaScript 代码：
## 实例 - test.js 文件
letnameSiteMappingnewMap()// 设置 Map 对象nameSiteMapping.set("Google"1)nameSiteMapping.set("Runoob"2)nameSiteMapping.set("Taobao"3)// 获取键对应的值console.log(nameSiteMapping.get("Runoob"))//40// 判断 Map 中是否包含键对应的值console.log(nameSiteMapping.has("Taobao"))//trueconsole.log(nameSiteMapping.has("Zhihu"))//false// 返回 Map 对象键/值对的数量console.log(nameSiteMapping.size)//3// 删除 Runoobconsole.log(nameSiteMapping.delete("Runoob"))// trueconsole.log(nameSiteMapping)// 移除 Map 对象的所有键/值对nameSiteMapping.clear()//清除 Mapconsole.log(nameSiteMapping);
执行以上 JavaScript 代码，输出结果为：
```
2truefalse3trueMap{'Google'1,'Taobao'3}Map{}
```

### 迭代 Map
Map 对象中的元素是按顺序插入的，我们可以迭代 Map 对象，每一次迭代返回 [key, value] 数组。
TypeScript使用 for...of 来实现迭代：
## 实例 -test.ts 文件
letnameSiteMappingnewMap()nameSiteMapping.set("Google"1)nameSiteMapping.set("Runoob"2)nameSiteMapping.set("Taobao"3)// 迭代 Map 中的 keyfor(letkeyofnameSiteMapping.keys()){console.log(key)}// 迭代 Map 中的 valuefor(letvalueofnameSiteMapping.values()){console.log(value)}// 迭代 Map 中的 key => valuefor(letentryofnameSiteMapping.entries()){console.log(entry[0]entry[1])}// 使用对象解析for(let[keyvalue]ofnameSiteMapping){console.log(keyvalue)}
使用 **es6** 编译：
```
tsc --target es6 test.ts
```

编译以上代码得到如下 JavaScript 代码：
## 实例
letnameSiteMappingnewMap()nameSiteMapping.set("Google"1)nameSiteMapping.set("Runoob"2)nameSiteMapping.set("Taobao"3)// 迭代 Map 中的 keyfor(letkeyofnameSiteMapping.keys()){console.log(key)}// 迭代 Map 中的 valuefor(letvalueofnameSiteMapping.values()){console.log(value)}// 迭代 Map 中的 key => valuefor(letentryofnameSiteMapping.entries()){console.log(entry[0]entry[1])}// 使用对象解析for(let[keyvalue]ofnameSiteMapping){console.log(keyvalue)}
执行以上 JavaScript 代码，输出结果为：
```
GoogleRunoobTaobao123Google1Runoob2Taobao3Google1Runoob2Taobao3
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


