import rumps
import config as config
import requests


class NSApplicationDelegate:
    def applicationSupportsSecureRestorableState(self, app):
        print(app)
        return True

class V2exApp(rumps.App):
    def __init__(self):
        if len(config.Settings) == 0:
            self.title = config.errors['no time setup']
        super(V2exApp, self).__init__('正在获取价格信息')

        # 更新时间，秒
        times = 5   #config.Settings['update_times']
        rumps.Timer(self.update, times).start()



    # @rumps.clicked('设置')
    # def setStartTime(self, sender):
    #     settings.setting()

    def update(self, sender):
        if len(config.Settings) == 0:
            self.title = config.errors['no time setup']
            return

        
        self.title = self.get_sol_token_price()


    def get_sol_token_price(self):
        """
        获取Solana代币实时价格 (USD)
        返回: 价格 (float) 或错误信息 (str)
        """
        api_url = f"https://api.dexscreener.com/latest/dex/tokens/{config.Settings['token_address']}"
        
        try:
            response = requests.get(api_url, timeout=10)
            response.raise_for_status()  # 检查HTTP错误
            data = response.json()
            
            # print(data)

            # 检查是否有交易对数据
            if "pairs" not in data or not data["pairs"]:
                return "No trading pairs found for this token"
            
            # 获取第一个交易对的美元价格
            first_pair = data["pairs"][0]
            if "priceUsd" not in first_pair:
                return "Price data not available in API response"
                
            return first_pair["priceUsd"]
            
        except requests.exceptions.RequestException as e:
            return f" {self.title}(历史价格，网络异常)"
        except (ValueError, KeyError, TypeError) as e:
            return f" {self.title}(历史价格，网络异常)"
