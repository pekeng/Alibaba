# -*- coding: utf-8 -*-
import scrapy


class AlibabaSpider(scrapy.Spider):
    name = 'alibaba'
    allowed_domains = ['www.alibaba.com']
    start_urls = ['http://www.alibaba.com/']
    headers = {
        'Host': 'alibaba.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
        # 'Accept': 'application / json, text / javascript, * / *; q = 0.01',
        # 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.alibaba.com/trade/search?&keyword=BEIJING&viewType=L&indexArea=company_en&page=2&n=50',
        # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'X-Requested-With': 'XMLHttpRequest',
    }

    def start_requests(self):
        url_list = ['https://www.alibaba.com/trade/search?&keyword=BEIJING&viewType=L&indexArea=company_en&page=1&n=50']
        cook = '''ali_apache_id=171.118.182.10.1537407354274.411516.2; acs_usuc_t=acs_rt=e5a99755783c40df887755afacde9a5f; v=0; cna=IRVLE+LeeAACAd3No+iicZFT; _m_h5_tk=16ed577cf9f178a7fafc2612f385e940_1537417795569; _m_h5_tk_enc=83d0b843c112e77badadafd968016b11; t=42e91c13b2bc82e842593406f107cff5; cookie2=10aa3b93ed0321ff75879c44b25b9353; _tb_token_=e7138eee59e77; ali_ab=171.118.182.10.1537407355983.9; _hvn_login=4; xman_us_f=x_locale=zh_CN&x_l=1&last_popup_time=1537407654957&x_user=CN|jake|jake|cnfm|234690938&no_popup_today=n; intl_locale=zh_CN; gangesweb-buckettest=171.118.182.10.1537407800496.9; _csrf_token=1537407813954; _uab_collina=153740786388046324226593; acs_rt=e5a99755783c40df887755afacde9a5f; atm-whl=-1%260%260%260; atm-x=__ll%3D-1; csg=fa672243; xman_us_t=ctoken=fr4j1z6witt6&l_source=alibaba&x_user=xI+j/upS/oAnhH9vggj6jD0OHVO4xg8Pn2rzSAmyQfI=&x_lid=cn1524504097fbkr&sign=y&need_popup=y; intl_common_forever=PDtHO9EUbHUgZ79rE9aR/siZmaqhKOl9F9+U9SKEyUMnaGZZ56rT2w==; xman_f=VUGfJ++QhalkZ6/4N0FOGZRiAKFK3oAxIgeC3cTtJMI97ef0XjmQhZ87vaunUBcJDn/XEXRkQPy+6c2KEI/IDybUJARXbnfijkLmUm537MHz5hJlwgSUo+PAel1tQxmxxwCKXey63YumbZIaKE69q7jCljkdE5vZWSP/fLTBDmrnVMjDhk5j1/IsyWtORy1NHBSENtanGKspRwZC/8BWRhBd2SfpZg2FqubyQZxGUDXRN2EjQWDvPUu7z2adjXYBOfNVW71u+CzdIxOqVGbSQv7cvVKXg6ljLvCrMfnhKMieKIpHndEK9sHfArKBOTxrB0cHToYQ9lIQ3PD6BBovWu/W0gS57DOYkUcrz7BXuUlPEI/UR5AcT1tKVLlVS1W1weGgi+AVKwIZ6wdysOOYQQ==; JSESSIONID=441F33930B32DAC4E15004314FDB49CC; ali_apache_track="ms=|mt=2|mid=cn1524504097fbkr"; ali_apache_tracktmp="W_signed=Y"; isg=BFhY-hEEt5jJlJsdu5Vna32TKYYq6bxaolKNCpJLAxKCLf0XAFMQW-VPYSW4PXSj; xman_t=7ThLoHUA7lXPhj9yaL0wJHLxqvYI2g60XBz/6XCeM+OrqszIVIAsrtr1Rn73IhfXnfzuo78XUq2HSMh0mpsFfbhYeO+g0MYYXzX0jQVCjdfxjHx1QR3JwY94Axp9JzxFYw17SyjEi3bsHhvUTLRuGqYv+Fku2dqxfFNTINbew41S3tBIplvCVOH0r6jtyceVgVtrhE3JsycfPuwoutPdzGjXw1fR+fBTURlE8HvfohGtshXSt2bL1bxn2/rTK3X/um8xg65YoR09sZoizZIOAC966w2qAqqBDbarN+DFFus3SNMj4YhA3uz0frr5HCGfSu2KlNnIsCYmVe2A9Meh/rfdCcnqIB/cEZadBNgkOZ+9TEvn0awH63ykESumuIAOUL21/+z8vlOhrkIim5Chin0NqgaQ30e21rV7SPvA9esBLHU8HTnTbevSjXE0eJNyHiF2XbbGgZdRYHJvUDbaLqA6ptZEg45M9QixvTo4Ir7pzufVL7NZsPfuZkzzCtbZ2Pu5hK7xfxcWF5w+PKXpuDp+UzJRRj42j54eSwbLXMdAs+DBXPsLYy4RZymyW37x+9lXM5n94soQPBXzsBByBdfp0caOXgvdtRzztkNeluJLps4zfqBSilwKT4gLBhICTC4a6Ip3QB/NoJNhs1L6JdXi2L2X1AGGD+UOgOCuYyH0fx06tHiXWdwbme9GUGDJfG8uxkt4yMwAwzBK3O2QpVB2umzS3BOq'''
        cookies_success = dict()
        if cook:
            try:
                for coo in cook.split(';'):
                    cookies_success[coo.split('=')[0].replace(' ', '')] = coo.split('=')[1]
            except Exception as cook_err:
                print("处理数据表中cookie出错 请确保input表中cookie格式如以下：\
                sb=0XebWyZ78I13HE1qgaMzQTqY; datr=0XebW2gk9o3eZHJl3LXNMnQ7; c_user=100026552122704;"
                      "异常原因：{}".format(cook_err))
        for url in url_list:
            yield scrapy.Request(url=url,
                                 headers=self.headers,
                                 dont_filter=True,
                                 cookies=cookies_success,
                                 meta={"cookiejar": 1},
                                 callback=self.parse
                                 )

    def parse(self, response):
        href_list = response.xpath("//div[@class='company']/a[@class='cd']/@href").extract()
        print(href_list)
        if "".join(href_list):
            for url_detail in href_list:
                yield scrapy.Request(url=url_detail,
                                     headers=self.headers,
                                     dont_filter=True,
                                     meta={"cookiejar": response.meta["cookiejar"]},
                                     # callback=self.parse_detail
                                     )

    def parse_detail(self, response):
        company_name = "".join(response.xpath("//table[@class='contact-table']/tr[1]/td/text()").extract())
        print(company_name)
