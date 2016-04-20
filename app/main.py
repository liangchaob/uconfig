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


HELPINFO = '''\
    参数如下:
      -init    : 按步骤全部重新配置
      -user    : 用户配置,负责用户的添加、删除、用户密码、用户权限等设置
      -network : 网络配置,负责网络接口、IP地址、防火墙、dns等网络相关设置
      -system  : 系统配置,负责主机名、时间、启动脚本、程序与进程等系统相关设置
      -software: 软件配置,负责软件源、安装、更新、卸载等设置
      -update  : 更新uconfig自身
      -version : 显示当前uconfig版本号
      -help    : 显示帮助信息\
      '''

# 导入os模块
import os

# 导入进程模块
import subprocess

# 导入json
import json

# 用户密码模块
import getpass

# 取得操作系统版本
cmd_getversion = "head -n 1 /etc/issue"


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


        








# 获取一个元组结构的返回值
# s = subprocess.Popen(cmd_getversion, shell=True, stdout=subprocess.PIPE)
# s = s.communicate()[0]
print "*********************************"
print "当前系统版本为 : " + exeReturn(cmd_getversion)
print "*********************************"

# 缺少一个正则表达式匹配驱动的判断语句，用于匹配当前系统应该使用的翻译器

SYSID="unknow"

if "Ubuntu 14.04" in exeReturn(cmd_getversion):
    SYSID = "ubuntu-14.04"
elif "CentOS release 6.5" in exeReturn(cmd_getversion):
    SYSID = "centos-6.5"
else:
    SYSID = "linux"







# 假设确定好了对应ubuntu的话

# 主函数
def main():
    # 设置参数
    # 如果没参数
    if len(sys.argv)<2:
        print HELPINFO
        sys.exit()

    #如果设置的第一个参数以'--'开始
    if sys.argv[1].startswith('-'):
        option=sys.argv[1][1:]
        # 匹配opt选择的各个参数
        if option=='version':
            print 'Version 0.1'
        elif option=='help':
            print HELPINFO
        elif option=='init':
            print '初始化'
        elif option=='user':
            while True:
                print '''\
----------------------------------------------
                '''
                print '当前用户列表:'
                print '用户名 | 组id | 用户目录'
                p = SetUser()
                p.userList()
                break
                print '''\
                用户设置:
                1.添加用户
                2.删除用户
                3.修改用户密码
                4.退出
                '''
                option2 = raw_input("输入设置项(1/2/3/4):")
                if option2 == '1':
                    new_user == raw_input("输入新的用户名:")
                    pass
        elif option=='network':
            print '网络'
        elif option=='system':
            while True:
                print '''\
----------------------------------------------
                系统设置:
                1.主机名
                2.时间设置
                3.开机启动项管理
                4.管理运行程序
                5.管理运行进程
                6.退出
                '''
                option2 = raw_input("输入设置项(1/2/3/4/5/6):")
                # 主机名选项
                if option2 == '1':
                    host_name = raw_input("输入主机名:")
                    print '新的主机名将为:' + host_name
                    # 设置新的主机名具体操作
                    p = SetSystem(hostname=host_name)
                    p.setHost()
                # 时间设置选项
                elif option2 == '2':
                    print '设置时间'
                    year = raw_input("输入年(四位整数):")
                    year = str(int(year))
                    print year + '年'
                    month = raw_input("输入月份(1~12):")
                    print year + '年' + month + '月'
                    date = raw_input("输入日期(1~31):")
                    print year + '年' + month + '月' + date +'日'
                    hour = raw_input("输入小时(1~24):")
                    print year + '年' + month + '月' + date +'日'+ hour + '点'
                    second = raw_input("输入分(0~59):")
                    print year + '年' + month + '月' + date +'日'+ hour + '点' + second + '分'
                    date_set = "\"" + year + "-" + month.zfill(2) + "-" + date.zfill(2) + " " + hour.zfill(2) + ":" + second.zfill(2) +":00\""
                    print date_set
                    p = SetSystem(time=date_set)
                    p.setTime()    
                elif option2 == '3':
                    print '设置开机启动项'
                elif option2 == '4':
                    print '管理当前运行程序'
                elif option2 == '5':
                    print '管理运行进程'
                elif option2 == '6':
                    print '退出'
                    break
                else:
                    print "输入有误！重新输入"

        elif option=='software':
            print '软件'
        elif option=='update':
            print '更新'
        else:
            print '无该选项!'
        sys.exit()
    else:
        for filename in sys.argv[1:]:
            readfile(filename)












# 读文件测试
def readfile(filename):
    '''Print a file to the standard output.'''
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line, # notice comma
    f.close()


# 这里设置一些类，主要用于拼接命令与调用json

# 系统设置类
class SetUser(object):
    """用于做系统设置的类"""
    def __init__(self, useradd = '', userlist = '', userdel ='', chgpasswd =''):
        self.useradd = useradd
        self.userlist = userlist
        self.userdel = userdel
        self.chgpasswd = chgpasswd
    # 设置查看用户返回的结果
    def userList(self):
        command = getDict(SYSID,'user','list_user')
        print exeReturn(command)
    def userAdd(self):
        command = getDict(SYSID,'user','add_user')




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
        # print command
        # print exeReturn(command)

        print '时间设置完成'


        











# 运行主函数
if __name__ == '__main__':
    main()






        