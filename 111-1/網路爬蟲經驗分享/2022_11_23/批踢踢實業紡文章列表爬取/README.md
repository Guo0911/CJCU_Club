# **2022/11/23 網路爬蟲經驗分享 - 批踢踢實業紡文章標題爬取**

### **此為課堂教學題目，請學員自行依照講師所教學之步驟或自行以其他方式確實完成題目要求**

_請注意自身抓取資料的時間間隔，以**不造成他人伺服器或網站負擔**為原則_

***

## **套件安裝**
請於Python環境中安裝以下套件
```
pip install bs4
```

***

## **練習題目**
### **題目要求**
1. 讓使用者可以自行輸入網址，請輸出提示訊息「請輸入批踢踢實業紡看板網址:」
2. 抓取輸入的看板網址內所有文章標題及連結
3. 按照**原始畫面**及**輸出範例**的格式對應，並將相關訊息輸出

### **注意事項**
1. 批踢踢實業紡常有18+認證的按鈕，請按照講師教學方式或自行查找資料繞過認證
    * 在Cookie中加入`over18=1`
2. 批踢踢實業紡的文章若刪除，會導致標題的連結消失，需另外處理
    * 請依照**輸出範例**內的格式修改網址
3. 爬蟲所抓取的網址可能會缺少前墜(如:https://www.ptt.cc/)，請自行補上

### **原始畫面**
![Originial Information](./README/original%20information.png)

### **輸出範例**
```
請輸入批踢踢實業紡看板網址: https://www.ptt.cc/bbs/Gossiping/index38997.html
第1篇文章: (本文已被刪除) [melissalewis] - 文章已被刪除
第2篇文章: [問卦] 萬年里長落選後會去哪？ - https://www.ptt.cc//bbs/Gossiping/M.1668474251.A.E47.html
第3篇文章: [新聞] 拜習會長談3小時！拜登重申一中政策不變  - https://www.ptt.cc//bbs/Gossiping/M.1668474311.A.DCE.html
第4篇文章: [新聞] 批選舉成人格毀滅戰 陳時中：北市民眼睛 - https://www.ptt.cc//bbs/Gossiping/M.1668474311.A.1D8.html
第5篇文章: [問卦] 台積電自前低漲了近百點？？？ - https://www.ptt.cc//bbs/Gossiping/M.1668474507.A.827.html
第6篇文章: Re: [問卦] 美國沒有賣雞屁股嗎? - https://www.ptt.cc//bbs/Gossiping/M.1668474579.A.9C3.html
第7篇文章: [問卦] 台灣巴肥特的台gg賣了沒？ - https://www.ptt.cc//bbs/Gossiping/M.1668474656.A.B5A.html
第8篇文章: [問卦] 修機車請特休一天會很瞎嗎？ - https://www.ptt.cc//bbs/Gossiping/M.1668474713.A.068.html
第9篇文章: [問卦] 正妹喜歡下棋，大家可以嗎？ - https://www.ptt.cc//bbs/Gossiping/M.1668474770.A.73F.html
第10篇文章: [問卦] Rap是唱rap還是唸rap - https://www.ptt.cc//bbs/Gossiping/M.1668474801.A.EBA.html
第11篇文章: [問卦] 不打仗+波克夏加持 該allin台積了吧？ - https://www.ptt.cc//bbs/Gossiping/M.1668474826.A.B92.html
第12篇文章: [問卦] locklock水壺真的能耐熱100℃嗎 - https://www.ptt.cc//bbs/Gossiping/M.1668474901.A.44A.html
第13篇文章: [新聞] 巴菲特買進台積電ADR逾41億美元 罕見押注 - https://www.ptt.cc//bbs/Gossiping/M.1668474917.A.095.html
第14篇文章: [新聞] 護士空姐制服任選!人夫用感情吸爆小三做 - https://www.ptt.cc//bbs/Gossiping/M.1668475026.A.C52.html
第15篇文章: [問卦] 現在恐、危、怕等侵台新聞哪家最多? - https://www.ptt.cc//bbs/Gossiping/M.1668475140.A.E8F.html
第16篇文章: Re: [新聞] 北市封關民調！蔣萬安36%領先、黃珊珊27% - https://www.ptt.cc//bbs/Gossiping/M.1668475179.A.512.html
第17篇文章: [問卦] 龜仙人為什麼可以參加力之大會?? - https://www.ptt.cc//bbs/Gossiping/M.1668475195.A.094.html
第18篇文章: Re: [新聞] 巴菲特買進台積電ADR逾41億美元 罕見押注 - https://www.ptt.cc//bbs/Gossiping/M.1668475379.A.89B.html
第19篇文章: [問卦] 包養正妹 - https://www.ptt.cc//bbs/Gossiping/M.1668475477.A.F3E.html
第20篇文章: [新聞] 否認低薪高報詐領！高虹安扯「前立委吳 - https://www.ptt.cc//bbs/Gossiping/M.1668475667.A.9D9.html
```
