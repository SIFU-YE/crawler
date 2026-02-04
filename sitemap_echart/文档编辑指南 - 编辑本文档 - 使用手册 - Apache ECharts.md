  *     *   *   *     * 常用图表类型
      *       *       *     *       * 地理坐标系（Geo）
    *   * 

#### 本页目录


# 文档编辑指南
## 新增一个 markdown 文件
在 `contents/zh/`（中文文章）或 `contents/en/`（英文文章）目录下新增一个 markdown 文件，最多支持三级目录。将路径及标题信息更新在 `contents/zh/posts.yml` 或 `contents/en/posts.yml`。将作者信息添加在 `components/helper/contributors.ts`。（注意，此文件中 `en` 和 `zh` 是不同的条目。）
markdown 文件名称小写。
## 使用 prettier 来自动格式化代码
在开始之前，我们推荐安装`prettier`的 VSCode 插件，该插件可以在你保存的时候自动帮你格式化代码。
如果你觉得自动的格式化破坏了你的代码块，你可以在在代码块外面加上下面代码阻止`prettier`格式化该部分代码
```
<!-- prettier-ignore-start -->
<!-- prettier-ignore-end -->
```

如果你发现有的代码块并没有被格式化，请先检查该代码是否存在语法上的错误。
## 内置变量
  * `optionPath`: 例如，链接 xAxis.type 能这么写而得到：
```
[xAxis.type](${optionPath}xAxis.type)
```

  * `apiPath`: 例如，链接 echarts.init 能这么写而得到：
```
[echarts.init](${apiPath}echarts.init)
```

  * `mainSitePath`: 例如，链接 echarts.init 能这么写而得到：
```
[echarts.init](${mainSitePath}api.html#echarts.init)
```

  * `exampleEditorPath`: 例如，链接 line-simple 能这么写而得到：
```
[line-simple](${exampleEditorPath}line-simple&edit=1&reset=1)
```

  * `exampleViewPath`: 例如，链接 line-simple 能这么写而得到：
```
[line-simple](${exampleViewPath}scatter-exponential-regression&edit=1&reset=1)
```

  * `lang`: 例如，链接 Get Started 能这么写而得到：
```
[Get Started](${lang}/get-started)
```



## 段落标题/子标题
The syntax:
```
## 某段落标题 [[[#a-unique-id-for-link]]]

```

> id 用于外链到此段落。强烈建议为每个段落标题声明唯一 id ，并且保持不变。否则，会自动根据段落标题文字生成一个 id ，但是当标题修改时，生成的 id 也会变，导致外链失效。并且，不同语言的文档中生成的 id 也不同，很不方便引用。 
注：文章主标题不必声明 id ，因为文章的链接就是文件路径（在 `posts.yml` 中定义）。
## 引用其它文章
```
[获取 Apache ECharts](${lang}/basics/download)

```

效果为： 获取 Apache ECharts
## 嵌入代码
### 基础使用
写法为：
```
```js
option = {
    series: [{
        type: 'bar',
        data: [23, 24, 18, 25, 27, 28, 25]
    }]
};
```

```

效果为： 
```
option = {
  series: [
    {
      type: 'bar',
      data: [23, 24, 18, 25, 27, 28, 25]
    }
  ]
};
```

### 代码推荐写法
为了可以让工具帮助我们对代码进行格式化，我们应该尽量避免有语法问题的写法。
比如注释 `...`
```
option = {
  series: [
    {
      type: 'bar'
      // ...
    }
  ]
};
```

### 实时预览和编辑
> 目前只支持对 ECharts option 代码的预览（执行代码绘制图表）
写法为：
```
```js live
option = {
  xAxis: {
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  },
  yAxis: {},
  series: [
    {
      type: 'bar',
      data: [23, 24, 18, 25, 27, 28, 25]
    }
  ]
};
```

```

效果为： 
```
option = {
  xAxis: {
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  },
  yAxis: {},
  series: [
    {
      type: 'bar',
      data: [23, 24, 18, 25, 27, 28, 25]
    }
  ]
};
```

live
### 更多预览布局
#### 左右
写法为：
```
```js live {layout: 'lr'}
option = {
  ...
};
```

```

效果为： 
```
option = {
  xAxis: {
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  },
  yAxis: {},
  series: [
    {
      type: 'bar',
      data: [23, 24, 18, 25, 27, 28, 25]
    }
  ]
};
```

live
#### 右左
写法为：
```
```js live {layout: 'rl'}
option = {
  ...
};
```

```

效果为： 
```
option = {
  xAxis: {
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  },
  yAxis: {},
  series: [
    {
      type: 'bar',
      data: [23, 24, 18, 25, 27, 28, 25]
    }
  ]
};
```

live
#### 下上
写法为：
```
```js live {layout: 'bt'}
option = {
  ...
};

```

效果为： 
```
option = {
  xAxis: {
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  },
  yAxis: {},
  series: [
    {
      type: 'bar',
      data: [23, 24, 18, 25, 27, 28, 25]
    }
  ]
};
```

live
### 高亮指定代码行以及设置文件名
写法为：
```
```js {1,3-5}[option.js]
option = {
  series: [
    {
      type: 'bar',
      data: [23, 24, 18, 25, 27, 28, 25]
    }
  ]
};
```

```

效果为： 
```
option = {
  series: [
    {
      type: 'bar',
      data: [23, 24, 18, 25, 27, 28, 25]
    }
  ]
};
```

## 嵌入图片
图片实际存放地址在 `static/images/` 下。
写法为：
```
![图片说明](images/demo.png)

```

### 设置图片高宽
对于当前页面的临时样式，可以直接写 html：
```
<img data-src="images/demo.png" style="width: 50px" />

```

## 嵌入示例（iframe）
写法为：
```
<md-example src="doc-example/getting-started" width="100%" height="300" />

```

其中，`src` 为 https://echarts.apache.org/examples/zh/editor.html?c=line-simple 地址中 `?c=` 后面这一串。
效果为： 
## 添加示例链接
写法为：
```
[line-simple](${exampleEditorPath}line-simple&edit=1&reset=1)
```

## 添加 ECharts 配置项链接
写法为：
```
[xAxis.type](${optionPath}xAxis.type)
```

写法为：
```
[echarts.init](${apiPath}echarts.init)
```

效果为： echarts.init
## 更多组件使用
文档支持使用全局注册的`markdown`组件，除了刚才介绍的`md-example`组件，还有下面几种组件
### md-alert
提示组件
```
<md-alert type="info">
This is an info alert.
</md-alert>

```

> This is an info alert. 
```
<md-alert type="success">
This is a success alert.
</md-alert>

```

> This is a success alert. 
```
<md-alert type="warning">
This is a warning alert.
</md-alert>

```

> This is a warning alert. 
```
<md-alert type="danger">
This is a danger alert.
</md-alert>

```

> This is a danger alert. 
suisuiz
