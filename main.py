import getter.fileGetter as Getter
import getter.folderUnwrap as unwrap
import getter.weekdaysNumber as weekNumber

import pandas as pd
import os
import shutil

getter=Getter.multiGetter
get=getter()

features_df=pd.DataFrame(data=get.values(),index=get.keys())
print(features_df)
#'file', 'path', 'ext', 'name', 'eye_state', 'datetime','week_num'
print(features_df['eye_state'])

names=features_df['name'].unique()
weekNum=weekNumber.weekdaysNum

for name in names:
    print(f'\n{name}')
    week_n=weekNum(features_df[features_df['name']==name])

shinohara_thu_O=features_df[features_df['name']=='shinohara'].query('eye_state=="O" and week_num == 3')
abe_thu_O=features_df[features_df['name']=='abe'].query('eye_state=="O" and week_num == 3')

himei_thu_O=features_df[features_df['name']=='himei'].query('eye_state=="O" and week_num == 3')
ideguchi_thu_O=features_df[features_df['name']=='ideguchi'].query('eye_state=="O" and week_num == 3')
inoue_thu_O=features_df[features_df['name']=='inoue'].query('eye_state=="O" and week_num == 3')
maeta_thu_O=features_df[features_df['name']=='maeta'].query('eye_state=="O" and week_num == 3')

newdatas={
    'shinohara_thu_O':shinohara_thu_O,
    'abe_thu_O':abe_thu_O,
    'himei_thu_O':himei_thu_O,
    'ideguchi_thu_O':ideguchi_thu_O,
    'inoue_thu_O':inoue_thu_O,
    'maeta_thu_O':maeta_thu_O
}

for newdir,newdata in newdatas.items():
    os.mkdir(rf'./data/{newdir}')
    datapath=newdata['path']
    [shutil.move(path, rf'./data/{newdir}') for path in datapath]


