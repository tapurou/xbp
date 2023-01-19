from symbol import namedexpr_test


name = int(input('閲覧する株価の種類の数字を選んでください。1,金融機関 2,マスメディア 3,通信サービス　4,システム・ソフトウェア 5,小売り'))
a = ["stock.py", "systemsoftware.py", "retail.py", "finamce.py", "massmedia.py"]
if name == 1:
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])
    print(a[4])

import webbrowser
webbrowser.open('https://www.nikkei.com/nkd/industry/stocklist/?n_m_code=121')  #金融機関

import webbrowser
webbrowser.open('https://www.nikkei.com/nkd/industry/stocklist/?n_m_code=141')  #マスメディア

import webbrowser
webbrowser.open('https://www.nikkei.com/nkd/industry/stocklist/?n_m_code=101')  #小売り

import webbrowser
webbrowser.open('https://www.nikkei.com/nkd/industry/stocklist/?n_m_code=146')  #システム・ソフトウェア

import webbrowser
webbrowser.open('https://www.nikkei.com/nkd/industry/stocklist/?n_m_code=142')  #通信サービス