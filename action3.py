#Action3: 对汽车质量数据进行统计

import pandas as pd
#Step1，数据加载
result = pd.read_csv("car_complain.csv")
print(result)
#Step2，数据预处理,拆分problem类型 => 多个字段
result = result.drop("problem",1).join(result.problem.str.get_dummies(","))
print(result.columns)
#Step3，数据统计
#品牌投诉总数
df_brand = result.groupby(["brand"])["id"].agg(["count"]).sort_values("count",ascending=False)
print("品牌投诉总数")
print(df_brand)
print("\n")
# #车型投诉总数
df_carmodel = result.groupby(["car_model"])["id"].agg(["count"]).sort_values("count",ascending=False)
print("车型投诉总数")
print(df_carmodel)
print("\n")
#哪个品牌的平均车型投诉最多
df_brand_carmodel =result.groupby(["brand","car_model"])["id"].agg(["count"]).groupby(["brand"]).mean().sort_values("count",ascending=False)
print(df_brand_carmodel)