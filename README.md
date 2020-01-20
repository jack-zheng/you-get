# You-Get 源码阅读

Clone 并阅读该项目用以优化自己的 cli 项目。克隆信息: Date: 2020-01-20, branch: master

## 我想要知道的

- [] python 终端命令行的组织形式
- [] 进度条功能怎么实现
- [] 该项目怎么获取视频信息的, 比如 cctv 视频，我自己到网页上找了下找不到╭(°A°`)╮

## 深入浅出了解该项目

1. 入口为根目录下的 `you-get` 文件，cd 到 root, 输入 `python3 you-get` 可以触发该脚本的运行
1. vscode 安装 python extension, 在 `you-get` 文件中打断点可进入 debug 模式
1. you-get 文件中会 parse src 文件路径, 并插入 sys.path 中, 所以能 import you_get
1. 在 you_get module 下面并没有一个叫 main 的 file, 但是入口中却调用了 you_get.main(), 我猜这里的 main 是方法名, 家在module的时候自动把里面的方法都加载了
