# githubtest
参照http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000
学习git，以下记录弯路及想法
2016.6.22
1、新建这个仓库，测试以上教程。
2、解决git bash不能显示中文，以下不知道是那些起作用：
https://gist.github.com/nightire/5069597
$ git config --global core.quotepath false          # 显示 status 编码
$ git config --global gui.encoding utf-8            # 图形界面编码
$ git config --global i18n.commit.encoding utf-8    # 提交信息编码
$ git config --global i18n.logoutputencoding utf-8  # 输出 log 编码
$ export LESSCHARSET=utf-8
# 最后一条命令是因为 git log 默认使用 less 分页，所以需要 bash 对 less 命令进行 utf-8 编码
修改 git-completion.bash 文件：
# 在文件末尾处添加一行
alias ls="ls --show-control-chars --color"
文件全部UTF-8无BOM格式
大概以上吧
3、删除文件
4、克隆了SyncY，貌似成功了
2016.6.21
1、安装 https://git-for-windows.github.io/
时有一个选择是使用ssh链接还是plink链接，因为常用putty，没多想的选择了plink，但是教程上只讲到ssh密钥创建，并未牵扯到plink，以至于push卡在确认密钥步骤等不到相应。翻了几个教程，用puttygen重新保存了ssh的密钥，用pageant add key之后正常。

