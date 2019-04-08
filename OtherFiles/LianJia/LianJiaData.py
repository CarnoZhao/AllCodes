import pandas as pd
import numpy as np
import LianJiaFunctions

df = pd.read_csv('LianJia.csv', sep = '\t')
df.drop_duplicates('names', 'first', inplace = True)
df = df.reset_index(drop = True)
# 整租 · 金台路地铁 近朝阳公园 装修好 诚意出租 带车位     朝阳    甜水园  82㎡    东南    1室1厅1卫       中楼层  （17层）        链家    14天前发布  [{is_subway_house: 近地铁}, {decoration: 精装}, {central_heating: 集中供暖}, {is_key: 随时看房}] 16000

# names, district, location, roomspace, orientation, numrooms, height, floors, owner, postdate, attrs, price

df["is_total"] = df.names.apply(
        lambda x: 1 if ' · ' in x else np.nan)
df["roomspace"] = df.roomspace.apply(
        lambda x: int(x[:-1]))
df["numrooms"] = df.numrooms.apply(
        LianJiaFunctions.room_num_clean)
for kind in ('bed', 'dining', 'bath'):
    df['num' + kind] = df.numrooms.apply(
            lambda x: x[kind])
df["floors"] = df.floors.apply(
        lambda x: int(x[1:-2]))
LianJiaFunctions.attrs_clean(df)
df.pop('attrs')
df.to_csv('LianJiaRaw.csv')
for useless in ('names', 'district', 'location', 'orientation', 'numrooms', 'height', 'floors', 'owner', 'postdate'):
    df.pop(useless)
df.to_csv('LianJiaClean.csv')
print(df.describe())
# xaxis, yaxis, roomspace, price, is_total, numbed, numdining, numbath, two_bathroom, central_heating, is_new, deposit_1_pay_1, is_key, decoration, is_subway_house, rent_period_month
