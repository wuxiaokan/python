import  hmac
from decimal import Decimal
from urllib.parse import urlencode
class Util:
    @staticmethod
    def get_list_ele(list,ele_name,ele):
        for row in list:
            if row[ele_name] == ele:
                return row

    @staticmethod
    def url_encode(arr):
        str1 = ""
        for k in arr:
            str1 += k[0]
            str1 += "="
            str1 += str(k[1])
            str1 += "&"
        return str1[:-1]

    @staticmethod
    def sign_encrypt(m,secret):
        import hashlib

        ##key  字典排序
        res = sorted(m.items(), key=lambda x: x[0], reverse=False)
        str1 = Util.url_encode(res)[:-1]+secret

        return hmac.new(secret.encode(),str1.encode(), digestmod=hashlib.sha1).hexdigest()
    @staticmethod
    def sub_number(number,len):
        return format(Decimal(number),'.'+str(len)+'f')

    @staticmethod
    def add(one,two,len=12):
        return Decimal(Util.sub_number(Decimal(one)+Decimal(two),len))
    @staticmethod
    def mi(one,two,len=12):
        return Decimal(Util.sub_number(Decimal(one)-Decimal(two),len))
    @staticmethod
    def mu(one,two,len=12):
        return Decimal(Util.sub_number(Decimal(one)*Decimal(two),len))
    @staticmethod
    def di(one,two,len=12):
        return Decimal(Util.sub_number(Decimal(one) / Decimal(two), len))
    @staticmethod
    def eq(one,two,len=10):
        return Decimal(Util.sub_number(one,len))==Decimal(Util.sub_number(two,len))
    @staticmethod
    def rand_eq(one,two,len=10):
        return round(Decimal(one),len)==round(Decimal(two),10)
