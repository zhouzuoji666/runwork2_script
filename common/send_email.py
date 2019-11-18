#!/usr/bin/env python

# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os
import re

# 获取失败数（Failures）
def get_failures(getreport):
    report = getreport()  # 获取测试报告的位置
    with open(report, 'r', encoding='UTF-8') as f:
        web_data = f.read()  # 读取测试报告内容
    pattern = re.compile(r"</td><td align=\"center\">(.*?)</td>")  # 使用正则表达式设置匹配规则
    failures = pattern.findall(web_data)[0]  # 获取第一个Failures对应的数值
    # print(failures)
    return failures

# 发送邮件
def send_mail(getreport):
    # 华润使用自己的系统，未使用第三方的SMTP服务设置。
    mail_host = 'mail.crc.com.hk'  # 华润smtp服务器：mail.crc.com.hk
    mail_user = 'rst_test_ios_zy@crhd0a.crc.hk'  # 用户名
    mail_pass = 'Mttp3666'  # 口令

    sender = 'rst_test_ios_zy@crc.com.hk'  # 邮件发送方邮箱地址
    wrong_receivers = ['lzg@crc.com.hk', 'wubei11@crc.com.hk', 'szoperators@crc.com.hk', 'gongyuan@crc.com.hk',
                       'yangxiaoran@crc.com.hk', 'lixulian1@crc.com.hk', 'longjun15@crc.com.hk', 'liumin373@crc.com.hk',
                       'pactera-347@crc.com.hk', 'CHINASIE-19@crc.com.hk', 'luweimiao1@crc.com.hk',
                       'simayu1@crc.com.hk', 'pactera-423@crc.com.hk', 'oujuntian@crc.com.hk', 'pactera-318@crc.com.hk',
                       'PACTERA-400@crc.com.hk', 'vivebest-34@crc.com.hk', 'HAND-323@crc.com.hk']  # 报错邮件-邮件接收方地址

    right_receivers = ['wubei11@crc.com.hk', 'gongyuan@crc.com.hk', 'yangxiaoran@crc.com.hk', 'szoperators@crc.com.hk',
                       'pactera-423@crc.com.hk', 'lixulian1@crc.com.hk', 'liumin373@crc.com.hk',
                       'pactera-347@crc.com.hk', 'CHINASIE-19@crc.com.hk', 'pactera-318@crc.com.hk',
                       'PACTERA-400@crc.com.hk', 'vivebest-34@crc.com.hk', 'HAND-323@crc.com.hk']  # 未报错邮件-邮件接收方地址
    '''
    receivers = ['lxj@crc.com.hk', 'lzg@crc.com.hk', 'tala3@crc.com.hk', 'gongyuan@crc.com.hk', 'lishihan@crc.com.hk',
                 'pyn@crc.com.hk', 'machenzhao@crc.com.hk', 'qiaoxin16@crc.com.hk', 'yangxiaoran@crc.com.hk',
                 'lixulian1@crc.com.hk', 'huangtongling1@crc.com.hk', 'huangkelin5@crc.com.hk', 'liyini3@crc.com.hk',
                 'luweimiao1@crc.com.hk', 'luyang30@crc.com.hk', 'zhoulin59@crc.com.hk', 'chenyihong4@crc.com.hk',
                 'longjun15@crc.com.hk', 'zhengjia@crc.com.hk', 'huangyuying16@crc.com.hk', 'weixing56@crc.com.hk',
                 'hujie132@crc.com.hk', 'yuanqiaolin@crc.com.hk', 'yujinghao@crc.com.hk', 'dengsuxia6@crc.com.hk',
                 'PACTERA-401@crc.com.hk', 'PACTERA-376@crc.com.hk', 'whz@crc.com.hk', 'oujinfu1@crc.com.hk',
                 'cn_pactera53@crc.com.hk', 'pactera-335@crc.com.hk', 'zhoushuai2@crc.com.hk', 'simayu1@crc.com.hk',
                 'yinshujun@crc.com.hk', 'lilinian@crc.com.hk', 'liumin373@crc.com.hk', 'zhangqian485@crc.com.hk',
                 'caitaotao2@crc.com.hk', 'pactera-318@crc.com.hk', 'PACTERA-400@crc.com.hk', 'VIVEBEST-2@crc.com.hk',
                 'VIVEBEST-8@crc.com.hk', 'pactera-366@crc.com.hk', 'pactera-211@crc.com.hk']  # 全体成员-邮件接收方地址

    tester_receivers = ['pactera-318@crc.com.hk', 'PACTERA-400@crc.com.hk', 'VIVEBEST-2@crc.com.hk',
                       'VIVEBEST-8@crc.com.hk', 'pactera-366@crc.com.hk', 'pactera-211@crc.com.hk',
                       'yangxiaoran@crc.com.hk']  # 测试组成员-邮件接收方地址
    '''
    # receivers = ['yangxiaoran@crc.com.hk']

    # 根据生成的接口监控报告中接口报错数决定邮件接收方地址（接口未报错时，发送给right_receivers；接口有报错时，发送给wrong_receivers）
    if int(get_failures(getreport)) == 0:
        receivers = right_receivers
        subject = '【办公门户-系统监控】【接口监控：' + get_failures(getreport) + '个接口报错】'
    else:
        receivers = wrong_receivers
        subject = '【办公门户-系统监控】【接口监控：' + get_failures(getreport) + '个接口报错】'

    # 创建一个带附件的实例
    message = MIMEMultipart()
    # subject = '接口自动化测试报告'
    message['Subject'] = Header(subject, "utf-8")  # 邮件主题
    message['To'] = ';'.join(receivers)  # 接收方信息

    # 邮件正文内容
    with open(getreport(), 'rb') as f:
        file_content = f.read()
    part1 = MIMEText(file_content, 'html', 'utf-8')
    message.attach(part1)  # 将附件内容写到正文

    # 添加附件
    part2 = MIMEText(file_content, 'base64', 'utf-8')
    part2['Content-Type'] = 'application/octet-stream'  # 设置内容类型
    part2['Content-Disposition'] = 'attachment; filename="runWork_testReport.html"'  # 设置附件名
    message.attach(part2)

    # 登录并发送邮件
    try:
        smtp_obj = smtplib.SMTP()
        smtp_obj.connect(mail_host, 25)  # 连接服务器，25为SMTP端口号
        smtp_obj.login(mail_user, mail_pass)  # 登入到服务器
        smtp_obj.sendmail(sender, receivers, message.as_string())  # 发送邮件
        smtp_obj.quit()  # 关闭连接
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("邮件发送失败")