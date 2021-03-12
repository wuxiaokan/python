import requests
import json
import allure
from urllib.parse import urlencode
import time
from common.read_yaml import ReadYaml

data = ReadYaml("data.yml").get_yaml_data()  # 读取数据


class HttpClient:
    def __init__(self):
        self.host = data['otc_app_host']

    default_header = {
        "Content-Type": "application/json",
        "sd_origin": "shendu-dev1.sdpjw.cn"
    }

    def send(self, url, body={}, method='get', headers={}, sessions=0, x_token=0, need_rsp=True):

        headers.update(self.default_header)
        if sessions:
            headers["Session"] = sessions
        if x_token:
            headers["token"] = x_token.strip('"')  # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
        self.create_request_log(url, method, body, headers)

        if method == "get":
            result = requests.get(url, params=body, headers=headers)
        elif method == "post":
            result = requests.post(url, data=json.dumps(body), headers=headers)
        elif method == "patch":
            result = requests.patch(url, data=json.dumps(body), headers=headers)

        if not need_rsp:
            return

        self.create_response_log(result.status_code, result.text)
        # print("headersaaaaaaaaaaaaaaaaaaaaaaaaa",headers)

        return {"status_code": result.status_code, "data": result.json()}

    def get_full_url(self, url, etc={}, replace={}, h=""):
        if h:
            host = h.rstrip('/')  # rstrip() 删除 string 字符串末尾的指定字符（默认为空格）.
        else:
            host = self.host.rstrip('/')

        url = url.lstrip('/')  # lstrip() 方法用于截掉字符串左边的空格或指定字符。
        full_url = host + "/" + url
        full_url += "?platform=zhengshi&time=" + str(int(round(time.time() * 1000)))
        if len(etc):
            s = urlencode(etc)  # urlencode  urllib库里面有个urlencode函数，可以把key-value这样的键值对转换成我们想要的格式，返回的是a=1&b=2这样的字符串
            full_url += "&" + s
        if len(replace):
            full_url = str.format(full_url,
                                  *replace)  # str.format() 方法通过字符串中的花括号 {} 来识别替换字段 replacement field，从而完成字符串的格式化。
        return full_url

    @allure.step("请求日志")
    def create_request_log(self, url, method, body, header):
        pass

    @allure.step('响应日志')
    def create_response_log(self, status_code, body):
        pass
