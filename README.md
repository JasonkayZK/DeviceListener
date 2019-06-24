# Keylogger
> 一个简单的记录键鼠使用次数的python小工具

--------------------

## 项目初衷:
> 作为一个程序员, 每日使用键盘鼠标成了无法逃离的日常之一, 当然也少不了咖啡(笑). 所以希望写一个键盘鼠标统计的小工具, 记录每天使用的次数, 也算是大数据了吧(伪233).
>
> 其实记录每天的鼠标点击, 键盘使用频率, 不也是一种乐趣嘛!

--------------------

## 踩过的坑:
> 作为一个常年使用Java的程序员, 一开始的打算当然使用本命语言来写, 但后来发现Java的JVM屏蔽了操作系统层, 还需要导入**jna**包来实现, 而比较坑的是Maven中的Jar包存在examples代码缺少的问题~~(其实是自己不想看源码了)~~.
>
> 经过一番查看就找到了原来已经有PyUserInput库, 可以直接通过pip install安装!(Linux下!)
> 
> 在Ubuntu下开发基本上没出现什么问题, 配置环境, 写代码到配置, 再到测试, 一天都没用到, 但是切换到Win10(x86)下, 配置环境各种问题!
>
> win10(x86)下的坑:
> * 基本开发库问题:
	在linux下进行开发, python各种包基本都有, 写代码就完事了, 在Win10下基本上还要再来一遍(Docker真好用!) 
> * 依赖库问题:
	在linux下的依赖包是xlib, 通过pip即可直接安装.
	但是在win10下需要安装pywin32, 这个倒还好通过pip即可.
	~~到了pyHook: 各种报错, 原本需要的依赖是pyHook, 但实际需要的是pyHook3(python 3.6.8), 而且pyhook3并没有直接的whl!~~
	最终,经过测试, 仅仅在python2.7下, 通过pyhook + pyuserinput可以完美支持!
	(内存占用不超过20M)
>
> **注**: 推荐windows在python2.x下运行!


## ~~有关在Win10(x86)下安装pyHook3的方法:~~
> ~~项目下有require文件夹, 其中包括:~~
> * ~~pyhook_py3k-master.zip,~~
> * ~~swigwin-4.0.0.zip~~
> * ~~vs_buildtools.exe~~
>
> 0. ~~安装vs_buildtools.exe (C++ 编译工具)~~
> 
> 1. ~~解压缩两个*.zip文件~~
>
> 2. ~~在pyhook_py3k-master目录下输入命令:~~
> ``` bash
>   python setup.py build_ext --swig=../swigwin-4.0.0/swig.exe
>	pip install.
> ```
> 3. ~~安装pyHook3成功!~~
>
> **注**: ~~对于windows的其他版本操作系统, 处理方法类似!~~

--------------------

## 感谢: 
> 感谢github: SavinaRoja提供的PyUserInput库方便我个人的开发.
>
> PyUserInput代码库:  <https://github.com/SavinaRoja/PyUserInput/>
>

-------------------

## 目录结构:
> win: 存放windows下的项目;
>
> linux: 存放linux下的项目;

-------------------
## 使用前的注意事项:
> 0. 开发库: PyUserInput, pymysql
>
> 1. 依赖库:
> * Linux - Xlib
> * Mac - Quartz, AppKit
> * Windows - pywin32, pyHook (python2.x)
>
> 2. 已测试支持的操作系统有:
> * Linux: 
>	* CentOS7
>   * Ubuntu: 14.04以上
> * Windows(python2.7):
>   * windows7, windows10(运行环境python 2.x)
>
> 3. **安装**:
> * linux下安装依赖:
>	* pip install *
>
> * windows下安装:
>	1. pip install pywin32
> 	2. 在require下: pip install pyHook-1.5.1-cp27-cp27m-win_amd64.whl 即可!
>

-------------------

## 如何使用:
> 1. 实现了在本地/数据库记录鼠标、键盘输入:
> 具体记录内容:
> * 鼠标左键点击次数
> * 鼠标右键点击次数
> * 鼠标中间点击次数
> * 鼠标移动距离
> * 鼠标移动速度
> * 鼠标点击时鼠标所在坐标
> * 键盘点击数
> * 键盘点击按键分布统计
>
> **注**: 默认情况下采用每5分钟保存一次数据, 并清空缓存, 可以通过修改config.json来更改设置.
>
> 2. 配置文件config.json:
> config变量内容:
> ``` json
> {
>	"database":{
>		"host":"127.0.0.1",
>		"port": 3306,        
>		"dbname":"logger",
>		"username":"root",
>		"password":"password"
>	},
>  "save": {
>        "saveInterval":5,
>        "useMysql":false,
>        "useHttp":false,
>        "useLocal":false,
>        "filename":"logger.csv"
>   },
>   "sync":false, 
>   "datalog": "datalog.json"
> }
> ```
> * database: 数据库配置相关
> * save: 数据报错相关
> * sync: 远程通过mysql同步
> * datalog: 数据缓存文件
>
>
> 3. 数据保存(两种保存方式):
> * 采用本地csv保存:
>      数据被保存在项目根目录下的logger.csv中
> * 采用数据库保存:
>      可以修改配置文件config.json中的database配置保存
>
> 4. 数据提交(功能开发中):
> 本项目实现了数据提交的服务:
>   针对本项目开发了java后台, 可以显示您提交的数据!
> * 提交地址: <a>http://123.207.58.155:8080/keylistener/upload</a>
> * 提交格式: 
> ``` json
> {
>	"user_id": "localhost",
>	"left_mouse": 0,
>	"right_mouse": 0,
>	"middle_mouse": 0,
>	"mouse_distance": 0.0,
>	"mouse_speed": 0,
>	"key_stroke": 0,
>	"key_speed": 0,
>	"key_map": {"a": 5, "b": 6},
>	"ip": "127.0.0.1",
>	"click_position": ["123, 123"]
> }
> ```

-------------------

## 声明:
> 本仓库代码可以随意分发, 大家可以自由的进行二次开发!
> 感觉本项目不错的可以star, 点个关注!❤ 

-------------------
