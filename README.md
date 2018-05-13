# Linkedin_Sign_Up
Implement automatic registration for Linkedin (https://www.linkedin.com/).
实现领英的自动注册。
## 所用环境
python：2.7
浏览器：chrome
系统：win10 , MS Office
所用的库大部分都比较常用，如codecs，部分库可能需要单独安装，比如win32比如'win32com'与`selenium`
## `selenium`的安装与使用：
###  `selenium`的安装：
先安装selenium库（pip或者conda install等方法），再下载chrome驱动，放入chrome安装目录（一般是'..\Google\Chrome\Application')，注意驱动的版本要与浏览器相同（下附版本对照表），浏览器的版本可以在刚才的安装路径中看到一个文件夹的名称便是（一般为60.x-66.x），然后将该安装路径添加到系统变量 ，重启机器。
##### 附chrome与驱动版本对照表：
chrome的版本一般显示为6x.x，但是驱动的版本不是与其相同，而是以以下方式对应：
|chromedriver版本  |支持的Chrome版本
| :-------------:|:-------------:|
|v2.37|	v64-66|
|v2.36|	v63-65|
|v2.35|	v62-64|
|v2.34|	v61-63|
常用的是这些，更多的对照可以看这个网页:https://blog.csdn.net/huilan_same/article/details/51896672
驱动的下载官方网页是：'https://sites.google.com/a/chromium.org/chromedriver/downloads'，但是需要翻墙，也可以在'http://npm.taobao.org/mirrors/chromedriver/'这个镜像站下载。
###  `selenium`的使用：
安装`selenium`之后，可以运行以下代码进行尝试，若成功打开百度首页说明`selenium`库安装成功。
```
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://www.baidu.com")
print(browser.page_source)
browser.close()
```
## 程序

####  数据文档准备
将个人的"jionglu85889456993@126.com----jiao6735"的txt文档中的账户密码直接粘贴进data文件下的'mailbox_account_origin.txt'中，并运行一次code文件夹中的'account_preprocess.py'进行数据的预处理。
注意：只复制尚未申请过的账户密码！
处理后的数据位于'mailbox_account.txt'中，其后的数字代表申请与否。
申请的账户会自动写入'excel_file.xls'表格中。
####  个人信息
打开code文件夹中的test.py文件，将信息写入:
```
user = 'fzdwxxcl' #使用者的姓名缩写，为了写入excel文档中
username = ' '
password = ' '
```
其中第一个`user`为使用者的姓名缩写，后面的`username`与`password`为所使用的易码平台的账号密码。
####  运行
若已经运行过预处理程序，并写入了个人信息，则可以运行test.py。
程序只有在登陆邮箱的时候会需要手工拖动一次验证码图片，其它时候均可自动处理，最后结束之后会将申请的账号写入excel文件中（运行程序的时候excel文档需要处于关闭状态，否则会报错）。
####  建议
程序做了一些错误控制，但是还不是很稳。。建议在网比较好的环境使用，网速差的话会经常蜜汁错误。
