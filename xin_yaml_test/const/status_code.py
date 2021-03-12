import const
import sys

const.EXCEPT_SUCCESS = {"code": 200, "msg": "ok"}
const.NETWORK_EX = {"code": 201, "msg": "网络异常"}

const.ADER_NOT_EXIST = {"code": 100, "msg": "用户不存在"}
const.IDENTIFY_FAILED = {"code": 101, "msg": "认证失败"}
const.GOOGLE_AUTH_OFF = {"code": 102, "msg": "没有开启谷歌验证"}
const.PAY_INFO_EX = {"code": 103, "msg": "支付方式添加异常"}
const.PAY_INFO_LIST_CHECK_EX = {"code": 104, "msg": "支付方式列表校验异常"}
const.ADER_CREATE_FAILED = {"code": 105, "msg": "用户注册失败"}
const.IDENTIFY_LV1_OFF = {"code": 106, "msg": "没有进行初级认证"}

const.DRAW_FAILED = {"code": 301, "msg": "提币发起失败"}
const.DRAW_ASSETS_EX = {"code": 302, "msg": "提币资产校验异常"}
const.ASSETS_EX = {"code": 303, "msg": "资产校验失败"}
const.TRAN_EX = {"code": 304, "msg": "划转账号资产异常"}
const.TRAN_ED_EX = {"code": 305, "msg": "被划转账号资产异常"}
const.TRAN_ASSETS_EX = {"code": 306, "msg": "划转账号历史记录异常"}
const.TRAN_ED_ASSETS_EX = {"code": 307, "msg": "被划转账号历史记录异常"}
const.AD_LIST_EX = {"code": 350, "msg": "获取广告列表异常"}
const.CREATE_AD_FAILED = {"code": 351, "msg": "创建广告失败"}
const.ORDER_NOT_FOUND = {"code": 352, "msg": "没有找到订单"}
const.ORDER_STATUS_EX = {"code": 353, "msg": "订单状态异常"}
const.ORDER_ROB_EX = {"code": 354, "msg": "商户抢单异常"}
const.ORDER_FINISH_EX = {"code": 355, "msg": "放币异常"}
const.FINANCE_EX = {"code": 356, "msg": "资产校验异常"}
const.TARGET_AD_NOT_FOUND = {"code": 357, "msg": "没有找到对应广告"}
const.CONFIRM_ORDER_EX = {"code": 358, "msg": "确认付款异常"}
const.AD_SURPLUS_EX = {"code": 359, "msg": "广告剩余校验失败"}

const.MERCHANT_CREATE_OR_FAILED = {"code": 500, "msg": "企业平台发起订单失败"}
const.MERCHANT_CONFIRM_ORDER_EX = {"code": 501, "msg": "企业平台确认订单失败"}
const.MERCHANT_FINANCE_EX = {"code": 502, "msg": "企业平台资产校验异常"}
const.MERCHANT_PAY_INFO_ADD_EX = {"code": 503, "msg": "企业平台添加资产校验异常"}

const.ADMIN_DRAW_GET_FAILED = {"code": 801, "msg": "总后台获取提币申请失败"}
const.ADMIN_SET_DRAW_FAILED = {"code": 802, "msg": "修改提币订单状态失败"}
const.ADMIN_GET_MERCHANT_INFO_FAILED = {"code": 803, "msg": "总后台获取商户信息失败"}

const.OTC_UPDATA_PASSWD = {"code": 804, "msg": "密码修改失败"}

sys.modules[__name__] = const
