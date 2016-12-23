網樂通論壇爬蟲
===

## 目的
由於論壇目前為唯獨狀態，所以寫一隻爬蟲爬成 Json 節省資源。大家有空就寫前端來套吧！
- next.py : 爬出每篇文章的網址並存為 next.py
- getContent.py : 依據 next.json 的內容，依序爬出文章內容、留言、時間、作者，存為 data.json


