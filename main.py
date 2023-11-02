# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from bs4 import BeautifulSoup as bs
import urllib.request
import re
import ssl
import pygal
import pygal_maps_world
import time



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # !/usr/bin/env python
    # coding: utf-8

    # In[2]:


    # 多维列表：【国家全称，该国GP排行页面网址，国家简称（供地图使用），GP排名】
    countryurls = [['United-states', 'https://appfigures.com/top-apps/google-play/united-states/top-overall', 'us', 0],
                   ['United-kingdom', 'https://appfigures.com/top-apps/google-play/united-kingdom/top-overall', 'gb',
                    0],
                   ['Canada', 'https://appfigures.com/top-apps/google-play/canada/top-overall', 'ca', 0],
                   ['Germany', 'https://appfigures.com/top-apps/google-play/germany/top-overall', 'de', 0],
                   ['Japan', 'https://appfigures.com/top-apps/google-play/japan/top-overall', 'jp', 0],
                   ['France', 'https://appfigures.com/top-apps/google-play/france/top-overall', 'fr', 0],
                   ['Italy', 'https://appfigures.com/top-apps/google-play/italy/top-overall', 'it', 0],
                   ['Australia', 'https://appfigures.com/top-apps/google-play/australia/top-overall', 'au', 0],
                   ['Algeria', 'https://appfigures.com/top-apps/google-play/algeria/top-overall', 'dz', 0],
                   #    ['Angola','https://appfigures.com/top-apps/google-play/angola/top-overall','ao',0],

                   #    ['Anguilla','https://appfigures.com/top-apps/google-play/anguilla/top-overall','',0],
                   #    ['Antigua-and-barbuda','https://appfigures.com/top-apps/google-play/antigua-and-barbuda/top-overall',''],

                   ['Argentina', 'https://appfigures.com/top-apps/google-play/argentina/top-overall', 'ar', 0],
                   ['Armenia', 'https://appfigures.com/top-apps/google-play/armenia/top-overall', 'am', 0],
                   ['Austria', 'https://appfigures.com/top-apps/google-play/austria/top-overall', 'at', 0],
                   ['Azerbaijan', 'https://appfigures.com/top-apps/google-play/azerbaijan/top-overall', 'az', 0],
                   #    ['Bahamas','https://appfigures.com/top-apps/google-play/bahamas/top-overall',''],
                   ['Bahrain', 'https://appfigures.com/top-apps/google-play/bahrain/top-overall', 'bh', 0],
                   #    ['Barbados','https://appfigures.com/top-apps/google-play/barbados/top-overall'],
                   ['Belarus', 'https://appfigures.com/top-apps/google-play/belarus/top-overall', 'by', 0],
                   ['Belgium', 'https://appfigures.com/top-apps/google-play/belgium/top-overall', 'be', 0],
                   ['Belize', 'https://appfigures.com/top-apps/google-play/belize/top-overall', 'bz', 0],
                   ['benin', 'https://appfigures.com/top-apps/google-play/benin/top-overall', 'bj', 0],
                   ['bolivia', 'https://appfigures.com/top-apps/google-play/bolivia/top-overall', 'bo', 0],
                   ['botswana', 'https://appfigures.com/top-apps/google-play/botswana/top-overall', 'bw', 0],
                   ['brazil', 'https://appfigures.com/top-apps/google-play/brazil/top-overall', 'br', 0],
                   ['bulgaria', 'https://appfigures.com/top-apps/google-play/bulgaria/top-overall', 'bg', 0],
                   ['burkina-faso', 'https://appfigures.com/top-apps/google-play/burkina-faso/top-overall', 'bf', 0],
                   ['cambodia', 'https://appfigures.com/top-apps/google-play/cambodia/top-overall', 'kh', 0],
                   ['cape-verde', 'https://appfigures.com/top-apps/google-play/cape-verde/top-overall', 'cv', 0],
                   ['chile', 'https://appfigures.com/top-apps/google-play/chile/top-overall', 'cl', 0],
                   ['colombia', 'https://appfigures.com/top-apps/google-play/colombia/top-overall', 'co', 0],
                   ['costa-rica', 'https://appfigures.com/top-apps/google-play/costa-rica/top-overall', 'cr', 0],
                   ['croatia', 'https://appfigures.com/top-apps/google-play/croatia/top-overall', 'hr', 0],
                   ['cyprus', 'https://appfigures.com/top-apps/google-play/cyprus/top-overall', 'cy', 0],
                   ['czech-republic', 'https://appfigures.com/top-apps/google-play/czech-republic/top-overall', 'cz',
                    0],
                   ['denmark', 'https://appfigures.com/top-apps/google-play/denmark/top-overall', 'dk', 0],
                   ['dominican-republic', 'https://appfigures.com/top-apps/google-play/dominican-republic/top-overall',
                    'do', 0],
                   ['ecuador', 'https://appfigures.com/top-apps/google-play/ecuador/top-overall', 'ec', 0],
                   ['egypt', 'https://appfigures.com/top-apps/google-play/egypt/top-overall', 'eg', 0],
                   ['el-salvador', 'https://appfigures.com/top-apps/google-play/el-salvador/top-overall', 'sv', 0],

                   ['estonia', 'https://appfigures.com/top-apps/google-play/estonia/top-overall', 'ee', 0],
                   #  ['fiji','https://appfigures.com/top-apps/google-play/fiji/top-overall'],
                   ['finland', 'https://appfigures.com/top-apps/google-play/finland/top-overall', 'fi', 0],
                   ['ghana', 'https://appfigures.com/top-apps/google-play/ghana/top-overall', 'gh', 0],
                   ['greece', 'https://appfigures.com/top-apps/google-play/greece/top-overall', 'gr', 0],
                   ['guatemala', 'https://appfigures.com/top-apps/google-play/guatemala/top-overall', 'gt', 0],
                   ['honduras', 'https://appfigures.com/top-apps/google-play/honduras/top-overall', 'hn', 0],
                   ['hongkongSAR', 'https://appfigures.com/top-apps/google-play/hong-kong/top-overall', 'hk', 0],
                   ['hungary', 'https://appfigures.com/top-apps/google-play/hungary/top-overall', 'hu', 0],
                   ['iceland', 'https://appfigures.com/top-apps/google-play/iceland/top-overall', 'ie', 0],
                   ['india', 'https://appfigures.com/top-apps/google-play/india/top-overall', 'in', 0],
                   ['indonesia', 'https://appfigures.com/top-apps/google-play/indonesia/top-overall', 'id', 0],
                   ['ireland', 'https://appfigures.com/top-apps/google-play/ireland/top-overall', 'ie', 0],
                   ['israel', 'https://appfigures.com/top-apps/google-play/israel/top-overall', 'il', 0],
                   ['jamaica', 'https://appfigures.com/top-apps/google-play/jamaica/top-overall', 'jm', 0],
                   ['jordan', 'https://appfigures.com/top-apps/google-play/jordan/top-overall', 'jo', 0],
                   ['kazakhstan', 'https://appfigures.com/top-apps/google-play/kazakhstan/top-overall', 'kz', 0],
                   ['kenya', 'https://appfigures.com/top-apps/google-play/kenya/top-overall', 'ke', 0],
                   ['kuwait', 'https://appfigures.com/top-apps/google-play/kuwait/top-overall', 'kw', 0],
                   ['kyrgyzstan', 'https://appfigures.com/top-apps/google-play/kyrgyzstan/top-overall', 'kg', 0],
                   ['laos', 'https://appfigures.com/top-apps/google-play/laos/top-overall', 'la', 0],
                   ['latvia', 'https://appfigures.com/top-apps/google-play/latvia/top-overall', 'lv', 0],
                   ['lebanon', 'https://appfigures.com/top-apps/google-play/lebanon/top-overall', 'lb', 0],
                   ['luxembourg', 'https://appfigures.com/top-apps/google-play/luxembourg/top-overall', 'lu', 0],
                   ['macedonia-fyrom', 'https://appfigures.com/top-apps/google-play/macedonia-fyrom/top-overall', 'mk',
                    0],
                   ['malaysia', 'https://appfigures.com/top-apps/google-play/malaysia/top-overall', 'my', 0],
                   ['mali', 'https://appfigures.com/top-apps/google-play/mali/top-overall', 'ml', 0],
                   ['malta', 'https://appfigures.com/top-apps/google-play/malta/top-overall', 'mt', 0],
                   ['mauritius', 'https://appfigures.com/top-apps/google-play/mauritius/top-overall', 'mu', 0],
                   ['mexico', 'https://appfigures.com/top-apps/google-play/mexico/top-overall', 'mx', 0],
                   ['moldova', 'https://appfigures.com/top-apps/google-play/moldova/top-overall', 'md', 0],
                   ['mozambique', 'https://appfigures.com/top-apps/google-play/mozambique/top-overall', 'mz', 0],
                   ['namibia', 'https://appfigures.com/top-apps/google-play/namibia/top-overall', 'na', 0],
                   ['nepal', 'https://appfigures.com/top-apps/google-play/nepal/top-overall', 'np', 0],
                   ['netherlands', 'https://appfigures.com/top-apps/google-play/netherlands/top-overall', 'nl', 0],
                   ['new-zealand', 'https://appfigures.com/top-apps/google-play/new-zealand/top-overall', 'nz', 0],
                   ['nicaragua', 'https://appfigures.com/top-apps/google-play/nicaragua/top-overall', 'ni', 0],
                   ['niger', 'https://appfigures.com/top-apps/google-play/niger/top-overall', 'ne', 0],
                   ['nigeria', 'https://appfigures.com/top-apps/google-play/nigeria/top-overall', 'ng', 0],
                   ['norway', 'https://appfigures.com/top-apps/google-play/norway/top-overall', 'no', 0],
                   ['oman', 'https://appfigures.com/top-apps/google-play/oman/top-overall', 'om', 0],
                   ['pakistan', 'https://appfigures.com/top-apps/google-play/pakistan/top-overall', 'pk', 0],
                   ['panama', 'https://appfigures.com/top-apps/google-play/panama/top-overall', 'pa', 0],
                   ['papua-new-guinea', 'https://appfigures.com/top-apps/google-play/papua-new-guinea/top-overall',
                    'pg', 0],
                   ['paraguay', 'https://appfigures.com/top-apps/google-play/paraguay/top-overall', 'py', 0],
                   ['peru', 'https://appfigures.com/top-apps/google-play/peru/top-overall', 'pe', 0],
                   ['philippines', 'https://appfigures.com/top-apps/google-play/philippines/top-overall', 'ph', 0],
                   ['poland', 'https://appfigures.com/top-apps/google-play/poland/top-overall', 'pl', 0],
                   ['portugal', 'https://appfigures.com/top-apps/google-play/portugal/top-overall', 'pt', 0],
                   # ['qatar','https://appfigures.com/top-apps/google-play/qatar/top-overall'],
                   ['romania', 'https://appfigures.com/top-apps/google-play/romania/top-overall', 'ro', 0],
                   ['russia', 'https://appfigures.com/top-apps/google-play/russia/top-overall', 'ru', 0],
                   ['saudi-arabia', 'https://appfigures.com/top-apps/google-play/saudi-arabia/top-overall', 'sa', 0],
                   ['senegal', 'https://appfigures.com/top-apps/google-play/senegal/top-overall', 'sn', 0],
                   ['singapore', 'https://appfigures.com/top-apps/google-play/singapore/top-overall', 'sg', 0],
                   ['slovakia', 'https://appfigures.com/top-apps/google-play/slovakia/top-overall', 'sk', 0],
                   ['slovenia', 'https://appfigures.com/top-apps/google-play/slovenia/top-overall', 'si', 0],
                   ['south-africa', 'https://appfigures.com/top-apps/google-play/south-africa/top-overall', 'za', 0],
                   ['south-korea', 'https://appfigures.com/top-apps/google-play/south-korea/top-overall', 'kr', 0],
                   ['sri-lanka', 'https://appfigures.com/top-apps/google-play/sri-lanka/top-overall', 'lk', 0],
                   ['sweden', 'https://appfigures.com/top-apps/google-play/sweden/top-overall', 'se', 0],
                   #   ['switzerland','https://appfigures.com/top-apps/google-play/switzerland/top-overall',],
                   ['tajikistan', 'https://appfigures.com/top-apps/google-play/tajikistan/top-overall', 'tj', 0],
                   ['tanzania', 'https://appfigures.com/top-apps/google-play/tanzania/top-overall', 'tz', 0],
                   ['thailand', 'https://appfigures.com/top-apps/google-play/thailand/top-overall', 'th', 0],
                   #  ['trinidad-and-tobago','https://appfigures.com/top-apps/google-play/trinidad-and-tobago/top-overall'],
                   ['tunisia', 'https://appfigures.com/top-apps/google-play/tunisia/top-overall', 'tn', 0],
                   ['turkey', 'https://appfigures.com/top-apps/google-play/turkey/top-overall', 'tr', 0],
                   ['turkmenistan', 'https://appfigures.com/top-apps/google-play/turkmenistan/top-overall', 'tm', 0],
                   #  ['uae','https://appfigures.com/top-apps/google-play/uae/top-overall','],
                   ['uganda', 'https://appfigures.com/top-apps/google-play/uganda/top-overall', 'ug', 0],
                   ['ukraine', 'https://appfigures.com/top-apps/google-play/ukraine/top-overall', 'ua', 0],
                   ['uruguay', 'https://appfigures.com/top-apps/google-play/uruguay/top-overall', 'uy', 0],
                   ['uzbekistan', 'https://appfigures.com/top-apps/google-play/uzbekistan/top-overall', 'uz', 0],
                   ['venezuela', 'https://appfigures.com/top-apps/google-play/venezuela/top-overall', 've', 0],
                   ['vietnam', 'https://appfigures.com/top-apps/google-play/vietnam/top-overall', 'vn', 0],
                   ['yemen', 'https://appfigures.com/top-apps/google-play/yemen/top-overall', 'ye', 0],
                   ['zimbabwe', 'https://appfigures.com/top-apps/google-play/zimbabwe/top-overall', 'zw', 0]]

    # In[ ]:

    # In[8]:

    ssl._create_default_https_context = ssl._create_unverified_context  # 全局取消证书验证

    counlen = len(countryurls)  # 列表的长度

    # In[9]:

    for index in range(counlen):
        country = countryurls[index][0]  # 国家全称
        url = countryurls[index][1]  # url地址
        response = urllib.request.urlopen(url)  # 访问url页面
        if response.status == 200:  # 访问成功
            print('%d.\tGP Rank of %s read OK' % (index + 1, country))
        else:  # 访问失败
            print('%d.\tGP Rank of %s read error' % (index + 1, country))

        soup = bs(response, "html.parser")  # HTML解析
        restr = re.compile("TikTok\w*")  # 从HTML页面的标题title中，寻找带TikTok开头的字符串
        ttag = soup.find(title=restr)  # 寻找符合条件的title
        if ttag == None:  # 没找到
            print('\tTikTok Rank Not found in TOP200 or website error!')
            countryurls[index][3] = -1  # 记录在列表中，-1代表无效
        else:
            place = ttag.text.find('.')  # 寻找符号.
            num = int(ttag.text[0:place])  # 符号.前面的数字 = GP排名
            print('\tTikTok Rank at: %d' % num)
            countryurls[index][3] = num  # 把GP排名记录在列表中

    # 画世界地图

    localtime = time.asctime(time.localtime(time.time()))
    worldmap_chart = pygal.maps.world.World()  # 世界地图初始化
    worldmap_chart.title = 'TikTok\'s Rank in GooglePlay Top Free Apps' + '   [BJ time: ' + localtime + ']'  # 标题

    for index in range(counlen):
        if countryurls[index][3] != -1:  # 判断是否是有效数据
            worldmap_chart.add(countryurls[index][0], {
                countryurls[index][2]: countryurls[index][3]  # 加入地图

            })

    worldmap_chart.render_to_file('TikTokRanksAtGP.svg')
    print('Finished successfully!')

