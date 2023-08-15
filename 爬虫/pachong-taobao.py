# -*- coding:utf-8 -*-
# import urllib.request as req 
import bs4 
# import requests
import time
import html5lib
import pymysql
import ssl
import datetime
import re
import urllib3
import time
import pycurl
from io import BytesIO
urllib3.disable_warnings()
import http.client
http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'
# import sys
# import imp
# imp.reload(sys)
# sys.setdefaultencoding("utf-8")
# db = pymysql.connect(
#     host = '47.107.80.166',user = 'root',passwd = 'Jiayi.888',
#     port = 3306,db = 'yp',charset = 'utf8'
#     )
# cur = db.cursor()
ssl._create_default_https_context = ssl._create_unverified_context
yesNum=0
noNum=0
def getUrl(url):
    # 定义请求�?    # headerss = {
    # "Transfer-Encoding":"chunked",
    # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",  
    # "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    # "Cookie":"_gcl_au=1.1.148363253.1583152525; FT_utm_campaign=Direct; FT_utm_source=Direct; FT_utm_medium=Direct; _ga=GA1.2.462251101.1583152526; _mkto_trk=id:233-KML-790&token:_mch-bstock.com-1583152526015-22918; _fbp=fb.1.1583152526546.1928743364; __zlcmid=x1ixEBXHuOpSv4; cookie-notice-policy=cookie-notice-policy; __utma=37839676.462251101.1583152526.1585682081.1585682081.1; __utmc=37839676; __utmz=37839676.1585682081.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); LT_utm_source=Direct; LT_utm_medium=Direct; LT_utm_campaign=Direct; LT_utm_content=Direct; LT_utm_term=Direct; frontend_cid=CJsGpo2gY2fnKPMP; frontend=f056065ca26faea0249a76160576eb82; bstock_access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNudkc3R0haM3NROWJmQi1LWndmQm9hek1wSSJ9.eyJhdWQiOiIxYjA5NGM1Zi1jOGE2LTQxNmMtOGM2Mi00ZGM3N2NhODhjZTkiLCJleHAiOjE1ODYwOTM1MzQsImlhdCI6MTU4NjA4OTkzNCwiaXNzIjoiYnN0b2NrLmNvbSIsInN1YiI6IjRiY2E3NzYwLTMzNzktNGJhNC05YzVkLTc5YjUzZjJiYzQ5OSIsImF1dGhlbnRpY2F0aW9uVHlwZSI6IlBBU1NXT1JEIiwiZW1haWwiOiJyZWZvbmV0cmFkaW5nMUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXBwbGljYXRpb25JZCI6IjFiMDk0YzVmLWM4YTYtNDE2Yy04YzYyLTRkYzc3Y2E4OGNlOSIsInJvbGVzIjpbImJ1eWVyIl0sInVhX2lkIjoiNThhYzVlNzA0MjFhYTkwZDEzYWQzMTMzIn0.V82_rQQyxpGOfuidQHSxM5E_nZ8xVXxvh8l9WGAcO_t1lGddqiLwl6XH1SvfqsQ1MJY1ChfDgbPlnVrSO_tKt7VfAhfxObkWRedT_9M9CR5xbHVMxzXjisQuzNdUvT4IVN1xU6pDG1WLEe6AMka5gAopEtVEBKfxl1MkKiue-rDVAcLN8Rd2LUmFlxjV0JigLZiKM13AOK3hC0yI6iJtOXY363_7MuiB2G7pGRrNz6ZcMe9mKfuAS8RXWfk-nJQQzRMf-BcvjCrq-fHd31cpArgYGAM77LQOWfQziuQkcdOC465inkz2eQGZsE6GzFXJZUGvG3yGw-hW2gq6_gLPZA; bstock_refresh_token=Pq86HuMiYZp35t-PKtNVx0wjGqPpuH4KAg1z_6ASl0sNz9WZ4DxuMA; _gid=GA1.2.517762985.1586089958; mp_b328da9ac03c4952e524c40fbb0ab0ad_mixpanel=%7B%22distinct_id%22%3A%20%2258ac5e70421aa90d13ad3133%22%2C%22%24device_id%22%3A%20%221709b3e718baca-0d5a9e4168dcfe-39697407-232800-1709b3e718ca13%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22%24user_id%22%3A%20%2258ac5e70421aa90d13ad3133%22%7D"}
    # r = requests.get(url=url,headers=headerss,verify = False,stream=True,timeout=15) 
    
    c=pycurl.Curl()
    c.setopt(pycurl.URL,url)
#    c.setopt(pycurl.TIMEOUT,30)
    c.setopt(pycurl.USERAGENT,"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36") 
    c.setopt(pycurl.REFERER,"https://s.taobao.com/search/_____tmd_____/page/login_jump?rand=S3WxGHAgAt756EpznwfNzJq2AFA2qBNla3j6EINUS8We9dazM_iKElp8DwVSHZUevpC41Bx7RzivXIj9RnZgdg&_lgt_=658658ec3bf229afdf371eed024f918f___215918___29861be8fd57512ebc792221bbc21b30___837b211a0c5c4d0311617da5fff37e257cad377890b4c45ccdf2cb0fd662949d0f671beae3225249f15a6f3a3482050da4620a65df4ca2ccd360f91c978d4836f2a8f58ca2ad61782752ae44ed8bce37dabbcdb62234b8ada9d0be5ccb7b7978157572d3deff3dce8c7b34c31eb86485caae31b5c6a324a81d532bfa89bbc73f518da506315934e59cdb9242f9001de59f91d46101e7de9aa49cdefac09023e2c12732e2944b35025f85c5a0803f0c66aa592e58d9f76e0d8aae6347e1b43863254facd14bb5207b2f4873ebc10a73c154ca108f5af14608caea993432e6050d53b8568a3b95049b3641155db964afbdbd1ca290b8dcdb475a166232a82573f8f74e9970c1432e542a05d1f12eed775d")
    c.setopt(pycurl.COOKIE,"cna=TbFWHfOh7mABASQOA7YW/8fb; _m_h5_tk=eea337262f931c4bcac4c396a9a657d6_1691346549065; _m_h5_tk_enc=a1f741e51b2efb7de1db551ad8fbb3c0; _samesite_flag_=true; cookie2=1f71caf39e818702a779433ff486c00f; t=193cba27db3abd77b845e84e8555c8d4; _tb_token_=55e33eb1de330; xlly_s=1; sgcookie=E100vDjpP6NKdxkzWSodn0SJycajGLXJOjfWUChdLFUwNB25gEakVNb61RcKu1dVy9xzRbFpTNKUoljYEGuCxGe6rX0TwykhBtbgpcg79ZkPE1H%2ByXC22fIidYN2RrbPSBjT; unb=922358777; uc1=cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&existShop=true&cookie21=UIHiLt3xSixwG45%2Bs3wzsA%3D%3D&cookie14=Uoe9bFn1JWlUSQ%3D%3D&pas=0; uc3=vt3=F8dCsGCoAPiwTk3IhRs%3D&lg2=UIHiLt3xD8xYTw%3D%3D&nk2=rpuzM%2Bh0aPzU&id2=WvKVvtpRSb0p; csg=2bb61573; lgc=%5Cu5A01%5Cu5A01veivy; cancelledSubSites=empty; cookie17=WvKVvtpRSb0p; dnk=%5Cu5A01%5Cu5A01veivy; skt=21c89aea5f438472; existShop=MTY5MTMzNzU3NQ%3D%3D; uc4=id4=0%40WDWmtmZFpLgbg0rnEVaYVRwBQWs%3D&nk4=0%40rMGrnZNJrNT4Nb%2Fwpkx4I6v8V2Q%3D; tracknick=%5Cu5A01%5Cu5A01veivy; _cc_=Vq8l%2BKCLiw%3D%3D; _l_g_=Ug%3D%3D; sg=y75; _nk_=%5Cu5A01%5Cu5A01veivy; cookie1=UUGnmdW7WOjwL%2BMceY3IxSfbQXM047FlQPh8Vav8XZY%3D; JSESSIONID=07212D9573D9958ADB4E354B9CDB3ADE; tfstk=dg4yHfbd422bH6Z-gcgUgqKNXK3-RVB1zyMItWVnNYDoFWcn8-2CwYNheJzEnWE5wD6JTQU4QeT5egFH82ghCO_157d-J2Xs2_b_wTOm8Z615NNRqYJ64O6KkFQfUlNPpd_EmOVtnz7BX3EfDSH2-FAta0D1Wx8H-rlrtAXZJph0Mo4L4pxEqjhqCs5qwvWLX; l=fBO-Ub5PNDDVfRkbBOfZourza779IIRAWuPzaNbMi9fP_V1p5IJfW1On_LL9CnhVF6VwR3S7jpCMBeYBcIccSQLy2j-la_Hmnm9SIEf..; isg=BICAe8Tf8IxzhIyIaU2lFCYFUQhSCWTT3iMDv_oRXhsvdSCfohpcYkdHjN21CByr")
    buffer = BytesIO()
    c.setopt(c.WRITEDATA, buffer)
    c.perform()   
    r=buffer.getvalue()
    buffer.close()
    c.close()
    # 请求成功后建立数据库
    # cur = db.cursor()
    # 开始解析并且插入库
    # times=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day)
    # upTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(r)
    root= bs4.BeautifulSoup(r,"html5lib")
    tr = root.find_all('a',class_="Card--doubleCardWrapper--L2XFE73")#.find定位到所需数据位置  .find_all查找所有的tr（表格）
    # temp = 1
    # for j in tr:
    #     k = j.find_all('span',class_="price-tag-fraction")
    #     w = j.find_all('div',class_="ui-search-item__group ui-search-item__group--title")
    #     print(k[0].get_text().strip()+"");
    #     print(w[0].get_text().strip()+"");
        # td = j.find_all('td')
        # Name = td[0].get_text().strip() 
        # Lot = td[1].get_text().strip() 
        # GRADE = td[3].get_text().strip()
        # UNITS=td[4].get_text().strip()
        # GOLD=td[7].get_text().replace(',', '').strip()
        # RMB=float(GOLD[1:])*7.78
        # RMBALL=round(RMB)
        # try:
        #     timeStr =td[5].find_all('span',class_="countdown")[0]['data-end-time']
        #     GMT_FORMAT = '%a, %d %b %Y %H:%M:%S -0700'
        #     _endDate = datetime.datetime.strptime(timeStr, GMT_FORMAT)
        #     endDate=(_endDate-datetime.timedelta(minutes=1)+datetime.timedelta(hours=15)).strftime("%Y%m%d%H%M%S")
        # except Exception as e:
        #     continue
        # sqlTemp="insert into goodsinfo ( goodsname, disno, percentage, quantity, amount,dropprice, goodstyle, state, reserved1, intime, validitydate ) values ( '"+Name+"', '2', '"+GRADE+"', '"+UNITS+"','"+str(RMBALL)+"','"+str(RMBALL)+"', '1', '1', '"+Lot+"', '"+times+"' , '"+endDate+"')  ON DUPLICATE KEY UPDATE amount= '"+str(RMBALL)+"' ,modtime= '"+upTime+"' ,validitydate= '"+endDate+"'"
        # cur.execute(sqlTemp)
    # cur.connection.commit()   
    # cur.close()
#    db.close()
    # temp=temp+48
    print(tr)
    for j in tr:
        print(""+j)
    # time.sleep(30)
    # getUrl()
#    yesNum=yesNum+1
    # getUrl("https://carros.mercadolibre.com.ve/corolla/_Desde_"+temp+"_NoIndex_True")
    
     
getUrl("https://s.taobao.com/search?_input_charset=utf-8&commend=all&ie=utf8&initiative_id=tbindexz_20170306&page=1&q=%E7%89%9B%E4%BB%94%E8%A3%A4&search_type=item&source=suggest&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.2&ssid=s5-e&suggest=0_1&suggest_query=&wq=")
# while True:    
#    try: 	
#        getUrl("https://www.microchipdirect.com/api/Product/ProductInfo?CPN=MCP4451T-503E/ML&start=0&rows=15")
#        yesNum=yesNum+49
#        time.sleep(30)
#        print("爬取成功")
#    except OSError:
#        noNum=noNum+1
#        time.sleep(10)
#     #    getUrl("https://carros.mercadolibre.com.ve/corolla/_Desde_"+noNum+"_NoIndex_True")
#        print("爬取失败")
#        pass
#    continue
 