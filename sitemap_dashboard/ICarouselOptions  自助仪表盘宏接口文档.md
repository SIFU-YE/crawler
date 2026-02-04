轮播选项接口对象 

version
    
10.1.0 

since
    
10.1.0
默认配置如下
```
timeout: 3,
standByValues: (当前筛选器的备选值),
infinite: true,
disabledOnEdit: true,
beforeChangeValue: () => {}
```

### Hierarchy 层级
  * ICarouselOptions


## Index 目录
###  Properties 
  * disabledOnEdit
  * standByValues


###  Methods 方法 
  * beforeChangeValue


##  Properties 
###  Optional disabledOnEdit 
disabledOnEdit: boolean
###  Optional infinite 
infinite: boolean
是否开启无限循环，默认为true
###  Optional standByValues 
standByValues: ArrayIStandByValue
轮播备选值，如果不传递，自动获取当前筛选器的备选值
###  Optional timeout 
timeout: number
轮播时间间隔，单位秒，默认值3秒
##  Methods 方法 
###  Optional beforeChangeValue 
  * beforeChangeValue(valueIStandByValue, indexnumber)void


  * 切换筛选器值之前的回调函数
#### Parameters 参数
    * #####  value: IStandByValue
即将切换的备选值
    * #####  index: number
即将切换的备选值的索引
####  Returns 返回值 void


