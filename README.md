# V2exApp
V2ex App - 在Mac状态栏显示$v2ex实时价格



# 怎样使用
## 1. 安装第三方模块
### rumps
rumps 是一个 Python 模块，用于创建 Mac OS X 应用程序。它提供了一个简单的方式来创建带有菜单栏图标的应用程序。
```bash
pip3 install rumps
```



### 或者一键安装所需模块：

```bash
pip3 install -r requirements.txt
```

## 2. 开始运行

```bash
python3 v2ex.py &
```

注意：需科学上网
开始运行后即可获得一个位于Mac状态栏的$v2ex实时价格


## 自动退出问题
如果你使用Mac自带的终端，或你的终端设置为关闭当前会话后关闭进程，则需要使用nohup来运行。

```bash
nohup python3 v2ex.py &
```

这是因为使用终端运行时，你的V2ex APP是终端启动的，此时终端进程是V2ex APP的父进程。
在Linux/Unix系统中，当终端关闭后，V2ex APP进程作为终端进程的子进程也会被自动关闭。

使用nohup可以忽略操作系统的SIGHUP信号，实现父进程消失后，在该父进程中启动的子进程继续运行的效果。



## 3. 怎样退出
单击状态栏价格数字，Quit


## 4. 特别说明
部分代码实现参考抄袭了
<a href="https://github.com/Scorcsoft/MonkeyApp">MonkeyApp</a>


MIT License
