#!/usr/bin/env python
# encoding: utf-8
'''
* liangchaob@163.com 
* 2016.4.17
'''
#设置中文字符
import sys
sys.path.append("./")
reload(sys)
sys.setdefaultencoding( "utf-8" )

# 导入os模块
import os

# 导入进程模块
import subprocess

# 导入json
import json

# 取得操作系统版本
cmd_getversion = "head -n 1 /etc/issue"


# 缺少一个正则表达式匹配驱动的判断语句，用于匹配当前系统应该使用的翻译器




# 定义和cli相关的函数，最终要注意放到包里面
# 直接执行命令行
def exe(command):
    subprocess.call(command,shell=True)

# 获取命令行的返回值
def exeReturn(command):
    s = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    s = s.communicate()[0]
    return s


# 用于提取json中指令的函数
def getDict(sys_id, opt1, opt2):
    # 读文件
    infile=open('/opt/uconfig/dict/'+sys_id+'/'+sys_id+'.json','r')
    content = infile.read()
    infile.close()
    # 格式化json
    content = content.replace("\n","").replace("\t","").replace("    ","")
    data = json.loads(content)
    # 提取命令字符并返回
    cmdstr = data[opt1][opt2]
    cmd = eval(repr(cmdstr)[1:])
    return cmd


SYSID="unknow"

if "Ubuntu 14.04" in exeReturn(cmd_getversion):
    SYSID = "ubuntu-14.04"
elif "CentOS release 6.5" in exeReturn(cmd_getversion):
    SYSID = "centos-6.5"
else:
    SYSID = "linux"







# 这里设置一些类，主要用于拼接命令与调用json

# 系统设置类
class SetUser(object):
    """用于做系统设置的类"""
    def __init__(self, username = ''):
        self.username = username
    # 设置查看用户返回的结果
    def userList(self):
        command = getDict(SYSID,'user','list_user')
        print exeReturn(command)
    # 添加用户
    def userAdd(self):
        set_var = "USERNAME=" + self.username +";"
        command = set_var+getDict(SYSID,'user','add_user')
        exe(command)
        exe(set_var+getDict(SYSID,'user','chg_passwd'))
    # 删除用户
    def userDel(self):
        # 设置变量
        set_var = "USERNAME=" + self.username +";"
        command = set_var+getDict(SYSID,'user','del_user')
        exe(command)
    # 重置用户密码
    def userReset(self):
        set_var = "USERNAME=" + self.username +";"
        exe(set_var+getDict(SYSID,'user','chg_passwd'))



# 系统设置类
class SetSystem(object):
    """用于做系统设置的类"""
    def __init__(self, hostname = '', init = '', time =''):
        self.hostname = hostname
        self.init = init
        self.time = time
    # 设置主机名
    def setHost(self):
        # 更改当前主机名
        set_var = "HOSTNAME=" + self.hostname +";"
        # 修改hostname文件
        command = set_var+getDict(SYSID,'system','change_hostname')
        exe(command)
        print "退出后重新登录生效!"
    # 设置系统开机启动脚本
    def setSysInit(self):
        print exeReturn("chkconfig --list | grep -E '3:on|3:启用'")
        # print exeReturn("egrep -v '^#' /etc/rc.local | grep -v '^$'")
    # 设置时间脚本
    def setTime(self):
        set_var = "TIME=" + self.time +";"
        command = set_var+getDict(SYSID,'system','set_data')
        exe(command)
        print '时间设置完成'


# 系统设置类
class SetSoftware(object):
    """用于做软件安装的类"""
    def __init__(self, sources = ''):
        self.sources = sources
    def setSource():
        if self.sources == '1':
            pass
        elif self.sources == '2':
            pass
        elif self.sources == '3':
            pass
        else:
            pass



