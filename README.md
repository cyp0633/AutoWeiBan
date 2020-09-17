# 辅助麦课安全网课学习

![GitHub release](https://img.shields.io/github/release/WeiYuanStudio/AutoWeiBan.svg?style=flat-square)

![GitHub last commit](https://img.shields.io/github/last-commit/WeiYuanStudio/AutoWeiBan.svg?style=flat-square)

## 使用方法

双击打开 `start.bat` ，根据命令行的提示进行操作即可。

## 自定义

1. 院校码，这个没有深入研究如何获取到具体学校的tenantCode(院校码，用于发送请求时区分学校)。每个学校的都是不同的，如果你想获取自己学校的tenantCode的话，你可以自己试着登录一次，在浏览器开发者工具中的网络选项卡中查看网络请求信息抓取。或者实在不会操作可以提个Issues过来。（现已加入TODO，该信息可以在登录页面中请求到一个巨大的JSON）

2. 课程间的延迟时间，在 **WeiBanAPI.py文件** 的头部中有两个参数分别为 **baseDelayTime** 基础延时秒数和 **randomDelayDeviation** 叠加随机延时差。 **实际延迟时间 = 基础延时秒数 + 叠加随机延时差**
