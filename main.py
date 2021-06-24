import getter.fileGetter as Getter
import pandas as pd

getter=Getter.multiGetter
get=getter()

features_df=pd.DataFrame(data=get.values(),index=get.keys())
print(features_df)
#'file', 'path', 'ext', 'name', 'eye_state', 'datetime','week_num'
print(features_df['eye_state'])
monday=features_df[:].query('eye_state=="O" and week_num == 0 ')
print('monday',monday,"\nNumber:",len(monday))

tuesday=features_df[:].query('eye_state=="O" and week_num == 1 ')
print('tuesday',tuesday,"\nNumber:",len(tuesday))

wednesday=features_df[:].query('eye_state=="O" and week_num == 2 ')
print('wednesday',wednesday,"\nNumber:",len(wednesday))

thursday=features_df[:].query('eye_state=="O" and week_num == 3 ')
print('thursday',thursday,"\nNumber:",len(thursday))

friday=features_df[:].query('eye_state=="O" and week_num == 4 ')
print('friday',friday,"\nNumber:",len(friday))

print(f'mon:tue:wed:thu:fri\n  {len(monday)}:  {len(tuesday)}:  {len(wednesday)}:  {len(thursday)}:  {len(friday)}')