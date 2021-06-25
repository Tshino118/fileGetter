def weekdaysNum(features_df):
    monday=features_df[:].query('eye_state=="O" and week_num == 0 ')

    tuesday=features_df[:].query('eye_state=="O" and week_num == 1 ')

    wednesday=features_df[:].query('eye_state=="O" and week_num == 2 ')

    thursday=features_df[:].query('eye_state=="O" and week_num == 3 ')

    friday=features_df[:].query('eye_state=="O" and week_num == 4 ')

    print(f'mon:tue:wed:thu:fri\n  {len(monday)}:  {len(tuesday)}:  {len(wednesday)}:  {len(thursday)}:  {len(friday)}')
    return [len(monday),len(tuesday),len(wednesday),len(thursday),len(friday)]
