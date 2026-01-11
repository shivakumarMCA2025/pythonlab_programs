from idlelib.debugger_r import DictProxy

import pandas as pd
author=['shivu','nikil','abhi','ammu']
article=[20,30,405,68]


auth_series=pd.Series(author)
article_series=pd.Series(article)

frame={'Author':auth_series,'Article':article_series}

result=pd.DataFrame(frame)
result["book"] = ["A","B","C","D"]
result["price"]=[20,30,40,220]
print(result)