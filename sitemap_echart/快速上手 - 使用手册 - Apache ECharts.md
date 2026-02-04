  *     *   *   *     * 常用图表类型
      *       *       *     *       * 地理坐标系（Geo）
    *   * 

#### 本页目录


# 快速上手
## 获取 Apache ECharts
Apache ECharts 支持多种下载方式，可以在下一篇教程安装中查看所有方式。这里，我们以从 jsDelivr CDN 上获取为例，介绍如何快速安装。
在 https://www.jsdelivr.com/package/npm/echarts 选择 `dist/echarts.js`，点击并保存为 `echarts.js` 文件。
> 关于这些文件的介绍，可以在下一篇教程安装中了解更多信息。
## 引入 Apache ECharts
在刚才保存 `echarts.js` 的目录新建一个 `index.html` 文件，内容如下：
```
DOCTYPE html

  
     charset 
    <!-- 引入刚刚下载的 ECharts 文件 -->
     src="echarts.js"
  

```

打开这个 `index.html`，你会看到一片空白。但是不要担心，打开控制台确认没有报错信息，就可以进行下一步。
## 绘制一个简单的图表
在绘图前我们需要为 ECharts 准备一个定义了高宽的 DOM 容器。在刚才的例子 `</head>` 之后，添加：
```

  <!-- 为 ECharts 准备一个定义了宽高的 DOM -->
   id style="width: 600px;height:400px;"

```

然后就可以通过 echarts.init 方法初始化一个 echarts 实例并通过 setOption 方法生成一个简单的柱状图，下面是完整代码。
```
DOCTYPE html

  
     charset 
    ECharts
    <!-- 引入刚刚下载的 ECharts 文件 -->
     src="echarts.js"
  
  
    <!-- 为 ECharts 准备一个定义了宽高的 DOM -->
     id style="width: 600px;height:400px;"
     type="text/javascript"
      // 基于准备好的dom，初始化echarts实例
      var myChart = echarts.init(document.getElementById('main'));

      // 指定图表的配置项和数据
      var option = {
        title: {
          text: 'ECharts 入门示例'
        },
        tooltip: {},
        legend: {
          data: ['销量']
        },
        xAxis: {
          data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
        },
        yAxis: {},
        series: [
          {
            name: '销量',
            type: 'bar',
            data: [5, 20, 36, 10, 10, 20]
          }
        ]
      };

      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option);
    
  

```

这样你的第一个图表就诞生了！
###  本文贡献者 在 GitHub 上编辑本页
zxx0006
