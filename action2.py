#Action2: 统计全班的成绩
#班里有5名同学，现在需要你用Python来统计下这些人在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。
#然后把这些人的总成绩排序，得出名次进行成绩输出（可以用numpy或pandas）

import pandas as pd
from pandas import Series,DataFrame
data = {"语文":[68,95,98,90,80],"数学":[65,76,86,88,90],"英语":[30,98,88,77,90]}
df1 = DataFrame(data)
df2 = DataFrame(data,index=["张飞","关羽","刘备","典韦","许褚"],columns=["语文","数学","英语"])
df2 = df2.rename_axis("姓名",axis=0)
#求平均成绩
print("语文平均成绩:",df2["语文"].mean())
print("数学平均成绩:",df2["数学"].mean())
print("英语平均成绩:",df2["英语"].mean())
#求最小成绩
print("语文最小成绩:",df2["语文"].min())
print("数学最小成绩:",df2["数学"].min())
print("英语最小成绩:",df2["英语"].min())
#求最大成绩
print("语文最大成绩:",df2["语文"].max())
print("数学最大成绩:",df2["数学"].max())
print("英语最大成绩:",df2["英语"].max())
#求方差
print("语文方差:",df2["语文"].var())
print("数学方差:",df2["数学"].var())
print("英语方差:",df2["英语"].var())
#求标准差
print("语文标准差:",df2["语文"].std())
print("数学标准差:",df2["数学"].std())
print("英语标准差:",df2["英语"].std())
#求总成级
df2["总成绩"] = df2.apply(lambda x: x.sum(), axis=1)
#按总成级排序
df2 = df2.sort_values(by="总成绩",ascending=False)
print(df2)