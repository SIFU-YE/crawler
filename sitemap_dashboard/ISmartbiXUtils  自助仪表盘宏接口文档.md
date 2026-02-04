### Hierarchy 层级
  * ISmartbiXUtils


## Index 目录
###  Methods 方法 
  * decodeBase64
  * encodeBase64
  * formatDate
  * getJsonValue
  * setJsonValue
  * transferColor


##  Methods 方法 
###  decodeBase64 
  * decodeBase64(strstring)string


  * 将Base64编码的字符串进行解码 

version
    
9.7.0 

since
    
9.7.0
#### Parameters 参数
    * #####  str: string
Base64编码的字符串
####  Returns 返回值 string


###  deepClone 
  * deepClone(...paramsany[])any


  * 深拷贝一个或多个对象 

version
    
9.7.0 

since
    
9.7.0
```
// 深拷贝
SmartbiXMacro.utils.deepClone(true, obj1, obj2)
// 浅拷贝
SmartbiXMacro.utils.deepClone(false, obj1, obj2)
```

#### Parameters 参数
    * #####  Rest ...params: any[]
####  Returns 返回值 any
返回深拷贝后新的对象


###  encodeBase64 
  * encodeBase64(strstring)string


  * 将字符串进行Base64编码 

version
    
9.7.0 

since
    
9.7.0
#### Parameters 参数
    * #####  str: string
需要编码的字符串
####  Returns 返回值 string


###  equals 
  * equals(xany, yany)boolean


  * 比较两个对象是否相同 

version
    
9.7.0 

since
    
9.7.0
#### Parameters 参数
####  Returns 返回值 boolean
返回对比的界面，true-相同，false-不相同


###  formatDate 
  * formatDate(dateDate, fmtstring)string


  * 将 Date 转化为指定格式的String (月(M)、日(d)、12小时(h)、24小时(H)、分(m)、秒(s)、周(E)、季度(q)） 

version
    
9.7.0 

since
    
9.7.0
**示例代码**
```
可以用 1-2 个占位符 年(y)可以用 1-4 个占位符，毫秒(S)只能用 1 个占位符(是 1-3 位的数字)

// 输出效果：2006-07-02 08:09:04.423
SmartbiXMacro.utils.formatDate(new Date(), "yyyy-MM-dd hh:mm:ss.S")
// 输出效果：2009-03-10 二 20:09:04
SmartbiXMacro.utils.formatDate(new Date(), "yyyy-MM-dd E HH:mm:ss")
// 输出效果：2009-03-10 周二 08:09:04
SmartbiXMacro.utils.formatDate(new Date(), "yyyy-MM-dd EE hh:mm:ss")
// 输出效果：2009-03-10 星期二 08:09:04
SmartbiXMacro.utils.formatDate(new Date(), "yyyy-MM-dd EEE hh:mm:ss")
// 输出效果：2006-7-2 8:9:4.18
SmartbiXMacro.utils.formatDate(new Date(), "yyyy-M-d h:m:s.S")

```

#### Parameters 参数
    * #####  date: Date
需要格式化的时间
    * #####  fmt: string
格式字符串
####  Returns 返回值 string
返回格式化后的时间字符串


###  getJsonValue 
  * getJsonValue(objany, pathstringstring[])any


  * 获取对象的深层属性值 

version
    
9.7.0 

since
    
9.7.0
```
let obj = {chartDefine: {seriesConfig: {global: {markLine: 'line'}}}}

// 例如：需要获取对象obj中的markLine深层属性的值
let markLine = SmartbiXMacro.utils.getJsonValue(obj, ['chartDefine','seriesConfig','global','markLine'])
```

#### Parameters 参数
    * #####  path: stringstring[]
深层属性的路径
####  Returns 返回值 any
返回属性的值


###  setJsonValue 
  * setJsonValue(objany, pathstringstring[], valueany)any


  * 设置对象的深层属性值 

version
    
10.5.8 

since
    
10.5.8
```
let options = {
  series: [{
    data: [{
      itemStyle: { color: 'blue' }
    }]
  }]
}

// 例如：需要设置对象options中的第一个数据点的颜色
SmartbiXMacro.utils.setJsonValue(options, ['series', 0, 'data', 0, 'itemStyle', 'color'], 'red')
```

#### Parameters 参数
    * #####  path: stringstring[]
深层属性的路径
    * #####  value: any
深层属性的值
####  Returns 返回值 any
返回属性的值


###  transferColor 
  * transferColor(colorstring, targetTypeColorTypestring)string


  * 颜色转换方法 

version
    
10.5.0 

since
    
10.5.0
```
// 方法会自动识别当前的颜色类型，如果不能识别表示暂不支持转换
let orginColor = `rgba(255, 255, 255, 0.5)` // '#FFFFFF','rgb(255,255,255)'
// 转换成rgba
let color = transferColor(orginColor, ColorType.RGBA)
// 转换成rgb
let color = transferColor(orginColor, ColorType.RGB)
// 转换成hex
let color = transferColor(orginColor, ColorType.HEX)
// 转换成透明度
let color = transferColor(orginColor, ColorType.A)

```

#### Parameters 参数
    * #####  color: string
    * #####  targetType: ColorTypestring
目标颜色的格式
####  Returns 返回值 string


