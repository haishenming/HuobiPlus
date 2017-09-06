"""
配置文件
"""

#### 变量名使用规范 ####
# 连接地址
HUOBI_SERVICE_API = "https://api.huobi.com/apiv3"
# 获取用户信息
ACCOUNT_INFO = "get_account_info"
# 当前委托
GET_ORDERS = "get_orders"
# 委托详情
ORDER_INFO = "order_info"
# 买入
BUY = "buy"
# 市价买入
BUY_MARKET = "buy_market"
# 取消委托
CANCEL_ORDER = "cancel_order"
# 查询个人最新10条成交订单
NEW_DEAL_ORDERS = "get_new_deal_orders"
# 根据trade_id查询oder_id
ORDER_ID_BY_TRADE_ID = "get_order_id_by_trade_id"
# 卖出
SELL = "sell"
# 市价卖出
SELL_MARKET = "sell_market"

#### 不需要验证的url ####
# B-R实时交易详情
BTC_CNY_TAS = "ttp://api.huobi.com/staticmarket/detail_btc_json.js"
# L-R实时交易详情
LTC_CNY_TAS = "http://api.huobi.com/staticmarket/detail_ltc_json.js"
