# 辅助麦课安全网课学习

**原作者：GitHub WeiYuanStudio。** 没有他的程序作为基础，就不可能有这个版本，在此感谢他。

本程序可以模拟浏览器行为，提交完成课程请求，快速自动完成课程。

## 使用方法

在右边的releases - source code(zip)下载安装包。

也可以在本页面点击下载代码按钮，选择下载zip。

在使用前，您必须自行获取学校代码，方法是打开新标签页，按F12打开开发者页面，切换到“Network”栏，按左上角的记录按钮，打开网课主页，在开发者页面的“name”栏中点击```list.do?timestamp=xxxx```，“表单数据”中的tenantCode即为学校代码。

湖南大学的代码为41008202，已经内置在```main.py```内。

您可以使用任何文本编辑器（VSCode、记事本、Notepad++、Vim都可以）打开main.py，修改```tenantCode=xxx```的值为学校代码，然后保存。

建议自行安装Python环境，并运行```pip install http```使用pip安装```http```库（也许不用安装库，可能已经内置了）。

如果使用Windows但没有Python，也可以直接运行目录中的.bat文件，使用内置的Python环境。

## 免责声明

本程序不含任何恶意代码，源代码全部开放，欢迎监督。

本程序仅供学习交流网络技术用途，出现任何后果开发者概不负责。

## 未来展望

“自选课程”的刷课可能不会再继续开发，实现难度有些大。也可以使用[这个Tampermonkey浏览器插件](https://greasyfork.org/zh-CN/scripts/413752-weiban-mycourse-cn刷课助手)来实现半自动刷课，不足之处就是需要手动点进来退出去，但是已经简化很多了。

如果有bug，欢迎提交Issue，应该会酌情修复；如果有什么使用上的问题，也欢迎发Discussion。

~~其实都是因为课业压力太繁重……要不然可能就都做了。~~

## 二次开发/帮助完善

您可以找到原作者留下的[API文档](./docs/APIDocs.md)以及我编写的[网页各值解析](./docs/ResponseDescription.md)来快速上手。

欢迎任何形式的二次开发，如果您想对本项目做出贡献，请提交Pull Request。

