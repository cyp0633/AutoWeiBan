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

## listCourse

## getInfo

对应变量 stuInfoResponse

- realName:姓名
- studentNumber:学号
- examNumber:高考考号（要这个干啥？）
- gender:性别
- tenantName:学校名称
- orgName:院系名称
- specialtyName:专业名称

## listCourse

对应变量 courseList

- finished:是否已完成。1代表已完成，2代表未完成
- imageUrl:预览图链接，似乎能提取courseId。
- isPraise:怀疑是是否可赞
- isShare:怀疑是是否可分享
- praiseNum:赞数
- resourceId:资源ID，不知道有什么用。
- resourceName:视频名称。
- shareNum:分享数量。
- userCourseId:视频ID，不知道和CourseId有什么区别，但是肯定不一样。
