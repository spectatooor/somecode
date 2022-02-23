import network
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="关注徐州丰县拐卖案")#名称
ap.config(authmode=3, password='qwertyuiop')#密码
