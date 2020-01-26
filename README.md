# You-Get 源码阅读

Clone 并阅读该项目用以优化自己的 cli 项目。克隆信息: Date: 2020-01-20, branch: master

## 我想要知道的

- [ ] python 终端命令行的组织形式
- [x] 进度条功能怎么实现
- [x] 该项目怎么获取视频信息的, 比如 cctv 视频，我自己到网页上找了下找不到╭(°A°`)╮

## 深入浅出了解该项目

1. 入口为根目录下的 `you-get` 文件，cd 到 root, 输入 `python3 you-get` 可以触发该脚本的运行
1. vscode 安装 python extension, 在 `you-get` 文件中打断点可进入 debug 模式
1. you-get 文件中会 parse src 文件路径, 并插入 sys.path 中, 所以能 import you_get

- 在 you_get module 下面并没有一个叫 main 的 file, 但是入口中却调用了 you_get.main(), 我猜这里的 main 是方法名, 家在module的时候自动把里面的方法都加载了

这里用到一个知识点是 package 的引入。python package 就是使用文件夹形式组织 python 文件，在 package 的根目录下会有一个 `__init__.py` 文件

- VSCode 中添加 `launch.json` 调试带参数的 cmd

- m.download 在 CNTV 这个文件中并没有 download 这个 method 而是选了一个名字很接近的 method, 是不是有什么加载机制做了这个匹配

仔细看了下，在 CNTV class 定义的时候，在末尾有一个声明将 `download = cntv_download`

- 主体中使用 ArgumentParser 来构造 cmd, 这是 python 自带的命令行工具

- 下载和打印 bar 的入口在 common.py 的 douwnload_urls 里面。line 978 会打印进度条，url_save 会下载视频并刷新进度条

- 下载的 URL 是哪里解析的，貌似每次下载解析的值都不一样

> 央视新闻查看页面源码然后搜索关键字 'var guid = "' 可以看到一串 guid，是每个视屏的识别码。然后结合 cntv.py 里面的 API 地址 query 一下就可以看到需要下载的视屏的具体信息了。比如: `http://vdn.apps.cntv.cn/api/getHttpVideoInfo.do?pid=0f8564b78b784bc98d10e7edb42e6c59`
>
> 视屏下载完后通过 ffmpeg 工具将下载的视屏片段做整合

- 原本我以为央视只提供了最高质量的视屏资源然后下载器在下载的时候怎么处理一下把他转成低质量类型的，实际上是央视在提供资源的时候就给出了各种不一样质量的视屏格式

- common.py 文件的 url_save 会批量获取视屏数据写入文件然后更新下载进度，做的很良心哦。这个分批下载一个文件的骚操作可以仔细看一看

- 更新 bar 的时候他是使用 `sys.stdout.write`, `sys.stdout.flush` 来写的，不是很清楚用法，可以查询一下

调试了一下 print = write + flush, 在 common.py 中输出 bar 都是用的后者。如果 write 输入参数前面加上 '\r' 的话还会把上一次的输入内容冲掉。`\r`表示回到行首。

- 而且这个东西还支持断点续传的，总感觉很神奇，逻辑应该在单个文件分 chunk 的那段代码里面可以仔细看看

断点续传和下载速度不是我理解的那样子。在 url_save 里面，是先发一个request，拿到对应的视屏数据，然后分批次写到文件中。所以那个速度更确切的应该是写到文件中的速度。
