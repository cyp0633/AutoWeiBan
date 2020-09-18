# 辅助麦课安全网课学习

## 下载

[点击进入下载页](https://gitee.com/WeiYuanStudio/AutoWeiBan/releases)

## 使用方法

Windows平台: 将 release 页中下载 `AutoWeiBan.zip`，在本地创建一个文件夹，将压缩包解压到文件夹里，双击打开 `start.bat` ，根据命令行的提示进行操作即可。

全平台: 都可以在安装完Python3环境后，到项目路径下执行`python main.py`运行。

## 可以自定义的地方

1. 院校码，这个没有深入研究如何获取到具体学校的tenantCode(院校码，用于发送请求时区分学校)。每个学校的都是不同的，如果你想获取自己学校的tenantCode的话，你可以自己试着登录一次，在浏览器开发者工具中的网络选项卡中查看网络请求信息抓取。或者实在不会操作可以提个Issues过来。（现已加入TODO，该信息可以在登录页面中请求到一个巨大的JSON）

2. 课程间的延迟时间，在 **WeiBanAPI.py文件** 的头部中有两个参数分别为 **baseDelayTime** 基础延时秒数和 **randomDelayDeviation** 叠加随机延时差。 **实际延迟时间 = 基础延时秒数 + 叠加随机延时差**
