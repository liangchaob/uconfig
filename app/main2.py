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

from classset import SetUser, SetNetwork, SetSystem, SetSoftware


VERSION = "v0.1.0"

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

     



# 缺少一个正则表达式匹配驱动的判断语句，用于匹配当前系统应该使用的翻译器

SYSID="unknow"

if "Ubuntu 14.04" in exeReturn(cmd_getversion):
    SYSID = "ubuntu-14.04"
elif "CentOS release 6.5" in exeReturn(cmd_getversion):
    SYSID = "centos-6.5"
else:
    SYSID = "linux"



# 获取一个元组结构的返回值
# s = subprocess.Popen(cmd_getversion, shell=True, stdout=subprocess.PIPE)
# s = s.communicate()[0]
print "*********************************"
print "当前系统版本为 : " + SYSID
print "*********************************"









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
            print 'Version '+ VERSION
        elif option=='help':
            print HELPINFO
        elif option=='init':
            print '初始化'
        # 设置用户
        elif option=='user':
            while True:
                print '''\
----------------------------------------------
                '''
                print '当前用户列表:'
                print '用户名 | 组id | 用户目录'
                p = SetUser()
                p.userList()
                print '''\
                用户设置:
                1.添加用户
                2.删除用户
                3.重置用户密码
                4.退出
                '''
                # 添加用户
                option2 = raw_input("输入设置项(1/2/3/4):")
                if option2 == '1':
                    new_user = raw_input("输入新的用户名:")
                    p = SetUser(username = new_user)
                    p.userAdd()
                    pass
                # 删除用户
                elif option2 == '2':
                    del_user = raw_input("输入即将删除的用户名:")
                    p = SetUser(username=del_user)
                    p.userDel()
                    pass
                elif option2 == '3':
                    reset_passwd = raw_input("输入重置密码的用户名:")
                    p = SetUser(username=reset_passwd)
                    p.userReset()
                    pass                 
                elif option2 == '4':
                    break
                else:
                    print "输入有误！重新输入"

        # 设置网络
        elif option=='network':
            while True:
                print '''\
----------------------------------------------
                '''
                print '当前网络设置:'
                p = SetNetwork()
                p.ethList()
                print '''\
                用户设置:
                1.修改ip设置
                2.设置dns
                3.退出
                '''
                option2 = raw_input("输入设置项(1/2/3/4):")
                # 设置新的ip
                if option2 == '1':
                    config_ethname = raw_input("输入需要修改的网卡名称:")
                    if config_ethname == '':
                        pass
                    else:
                        config_ip = raw_input("设置新的ip地址(为空则dhcp):")
                        if config_ip == '':
                            config_mode = 'dhcp'
                            p = SetNetwork(config_ethname=config_ethname,config_mode=config_mode)
                            p.ipSetDhcp()
                        else:
                            config_mode = 'static'
                            config_mask = raw_input("设置掩码:")
                            config_gateway = raw_input("设置网关:")
                            p = SetNetwork(config_ethname=config_ethname,config_ip=config_ip,config_mode=config_mode,config_mask=config_mask,config_gateway=config_gateway)
                            p.ipSetStatic()
                        config_writein = raw_input("是否立即重启网卡生效(y/n):")
                        if config_writein == 'y':
                            p = SetNetwork(config_ethname=config_ethname)
                            p.ethReset()
                        elif config_writein == 'n':
                            pass
                        else:
                            pass
                # 设置dns
                elif option2 == '2':
                    set_dns = raw_input("输入dns地址:")
                    p = SetNetwork(config_dns=set_dns)
                    p.dnsSet()
                    print '设置成功!'
                # 退出
                elif option2 == '3':
                    break
                else:
                    print "输入有误！重新输入"

        elif option=='system':
            while True:
                print '''\
----------------------------------------------
                系统设置:
                1.主机名
                2.时间设置
                3.开机启动项管理
                4.查看端口占用
                5.查看运行进程
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
                # 启动项管理   
                elif option2 == '3':
                    print '设置开机启动项'
                    p = SetSystem()
                    p.setSysInit()
                elif option2 == '4':
                    print '查看端口占用'
                    p = SetSystem()
                    p.setPort()
                elif option2 == '5':
                    print '查看运行进程'
                    p = SetSystem()
                    p.setPs()
                elif option2 == '6':
                    print '退出'
                    break
                else:
                    print "输入有误！重新输入"
        # 管理软件
        elif option=='software':
            while True:
                print '''\
----------------------------------------------
                '''
                print '设置当前软件:'

                print '''\
                用户设置:
                1.修改软件源
                2.安装软件
                3.卸载软件
                4.退出
                '''
                option2 = raw_input("输入设置项(1/2/3/4):")
                if option2 == '1':
                    set_source = raw_input("输入网络源选项(1.阿里云/2.163/3.本地光驱):")
                    pass
                    if set_source == '1':
                        source = "阿里云"
                    elif set_source == '2':
                        source = "163"
                    elif set_source == '3':
                        source = "本地光驱"
                    else:
                        source ="无效"
                    p = SetSoftware(sources=set_source)
                    p.setSource()
                    print "当前源设置为:" + source
                elif option2 == '2':
                    search_software = raw_input("输入要安装的软件名:")
                    print "搜索到的可用软件包:"
                    p = SetSoftware(search_software=search_software)
                    p.search()
                    install_software=raw_input("安装期望的软件包:")
                    p = SetSoftware(install_software=install_software)
                    p.install()
                elif option2 == '3':
                    remove_software = raw_input("输入要卸载的软件名:")
                    p = SetSoftware(remove_software=remove_software)
                    p.remove()
                    
                elif option2 == '4':
                    break
                else:
                    print "输入有误！重新输入"

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


# 运行主函数
if __name__ == '__main__':
    main()






        