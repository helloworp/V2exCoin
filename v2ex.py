import sys

try:
    import rumps
except ModuleNotFoundError as e:
    print('缺少所需依赖，执行以下命令安装: ')
    if e.name == 'rumps':
        print('pip3 install rumps rumps')

    sys.exit(0)

import config as config

if sys.platform == 'darwin':
    import MacV2ex as MacV2ex
else:
    print('只支持MacOS')
    sys.exit()

# 设置代币token，更新频率
config.Settings = {"token_address":"9raUVuzeWUk53co63M4WXLWPWE4Xc6Lpn7RS9dnkpump",
                   "update_times":5}

v2exASCII = r'''
____    ____  ___    __________   ___ 
\   \  /   / |__ \  |   ____\  \ /  / 
 \   \/   /     ) | |  |__   \  V  /  
  \      /     / /  |   __|   >   <   
   \    /     / /_  |  |____ /  .  \  
    \__/     |____| |_______/__/ \__\ 
                                      
'''

if __name__ == '__main__':
    print(v2exASCII)
    v2ex = MacV2ex.V2exApp()
    v2ex.run()
