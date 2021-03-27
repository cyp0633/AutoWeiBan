# 猜测网站发回信息的意义

## loginResponse

- userId:用户的ID
- userName:用户的名字……为什么会是这样？
- tenantCode:学校代码
- batchCode:不知道
- gender:性别
- openid:应该是微信扫码登陆返回的ID？
- preUserProjectId:应该是上一个课程的ID
- normalUserProjectId:现在课程的ID
- preAlias:上个课程的名称
- normalAlias:现在课程的名称
- normalBanner:现在课程的banner图片地址
- specialAlias, specialBanner, militaryAlias, militaryBanner:以此类推

（或者，pre normal special military各自对应四个课程？）

- isLoginFromWechat:是否来自微信登陆
