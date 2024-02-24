# toolkit
一些在抖音上看到的小工具集合

# 工具类
1接口:

  public-apis
  
  awesome_APIs(有中文注释，更好用)
  
2开发工具类:

  Mica(签名加密工具类，常用工具类，类，反射工具等，基于jdk8，没第三方依赖)
  
  Hutool(最强大的工具库)
  
  SMS4J(动态配置切换发送短信)
  
  Forest(api框架，可以简化调用接口逻辑，更加方便)
  
  powerJob(分布式任务调度与计算框架)
  
  WxJava，Jeepay，wxPay(集合微信支付宝支付代码)
  
  GoPay(go语言的，支付宝微信有一些官方没有的支付这个有)
  
  justAuth(快速实现第三方平台登录功能)
  
  Final2x(可以把图片超分到任意大小，图片修复，提升图像质量)
  
  DataV(大屏数据可视化组件库，适合做统计数据报表等)
  
  EasyOCR(开源OCR,识别多种语言和字体)
  
  bytebase或者Archery(数据库管理平台)
  
  pake(一行命令把网站打包成桌面端app)
  
  NATAPP(内网穿透)
  
  NPS(内网穿透)
  
  easy-es(搜索引擎傻瓜式orm框架)  
  
  idea插件Alibaba Java Coding Guidelines 一键生成代码注释
  
3爬虫类:
  WebMagic(java爬虫)
  
# 聊天(cim)
  http://159.138.121.249:5700/

# 游戏类
  FXGC-https://github.com/AlmasB/FXGL

# 运维类型

1.处理服务器cpu占用高:

  通过top找出cpu耗用最高进程的PID
  
  top -H -p 进程PID 找到最高的线程PID
  
  把线程ID转化成16进制 printf '0x%x\n' 线程PID
  
  jstack 进程PID | grep 16进程线程PID -A 20
  
2.监控数据库状态:

  霜之哀伤
  
3.Hippo-4J线程池监控

4.Arthas(线上问题排查，阿里出品)

5.Nconfig(Nginx可视化一键生成配置)

6.Ghidra软件逆向工程

7.hackingTool(黑客工具)

  
#开源系统

1.培训系统-PlayEdu

#大数据方案

1.阿里云datahub+AnalyticDB(分析型数据库)

2.ruoyi-TPS/QPS大概800左右、优化可以上1000

3.独角数卡，开源自动售货系统

4.mysql单表数据应该小于2000w

5.smsBoom短信轰炸机

#备份独角兽卡：
选择最新版本是可以发邮件的，实在不行换回2.02版本，按php+宝塔的模式来部署，也可以用docker来部署

V免签的回调有问题，记得用自己本地的代码

  
