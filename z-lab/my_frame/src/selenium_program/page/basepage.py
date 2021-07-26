import json
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:
    path = os.path.dirname(__file__).strip("page").__add__("data/cookie.txt")

    def __init__(self, base_drievr=None):
        base_drievr: webdriver
        if base_drievr == None:
            self.driver = webdriver.Chrome()
            self._loginByCookie()
        else:
            self.driver = base_drievr

    def _getCookies(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=chrome_args)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies = driver.get_cookies()
        # 以文件流的形式打开文件
        with open(self.path, "w") as f:
            # 存储 cookie 到 cookie.json
            json.dump(cookies, f)
        f.close()

    # def _loginByCookie(self):
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
    #     # 以文件流的形式打开文件
    #     with open(self.path, "r") as f:
    #         # 读取 cookies
    #         cookies = json.load(f)
    #         print(cookies)
    #     # 注入 cookies
    #     f.close()
    #     for cookie in cookies:
    #         print(cookie)
    #         # print(cookie["domain"])
    #         try:
    #             if cookie["expiry"] != "":
    #                 del cookie["expiry"]
    #         except:
    #             pass
    #         self.driver.add_cookie(cookie)
    #
    #     # cookies = "wwrtx.i18n_lan=zh; wwrtx.c_gdpr=0; wwrtx.ref=direct; wwrtx.refid=10009762451962441; _ga=GA1.2.139286144.1626244364; _gid=GA1.2.1819626163.1626244364; ww_rtkey=1cfe05h; wxpay.vid=1688849972135637; wxpay.corpid=1970325126440285; wwrtx.d2st=a7138747; wwrtx.sid=3UCMNSpUT9hVMAm0RJmEMtoQM1M_9CO8k_FNJ_cGIVFwr-xRAydhW4frlCEpVVQh; wwrtx.ltype=1; wwrtx.vst=GP4wRqdi8rxb_7ZBpjSTTGOD-b38lLXSoQ0rDyqfC-CohsPZhK6UzIugILAaHtQqjjfSdbWE6KjLx8X3xNXCx34drxrn5aF8Wik17SSXDTiyjkH9N_QJ6DS9KvmQKpK---ys_uxKFn1EkV-nIFaKXuax7Uap3wibtJDq9Qivob4tgYCZNxTrUbVXZvZ90Jv1M4X7Ljl7bu42q0KAKvl4XLQjin7o_tg9IGvC1h4SEZlrB1Aol1qGTwK_ctl_so2PbRnpvaYWTrniMCGxcv0KAA; wwrtx.vid=1688849972135637; wwrtx.cs_ind="
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    #     sleep(3)

    def _loginByCookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 以文件流的形式打开文件
        with open(self.path, "r") as f:
            # 读取 cookies
            cookies = f.readline()
            # print(cookies)
        # 注入 cookies
        f.close()
        js = 'window.localStorage.setItem("token","%s")' % cookies
        self.driver.execute_script(js)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def finds(self, locator):
        return self.driver.find_elements(*locator)

    def findAndClick(self, locator):
        self.find(locator).click()

    def findAndSendkey(self, locator, key):
        self.find(locator).sendkeys(key)

    def teardown(self):
        self.driver.quit()