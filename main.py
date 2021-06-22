import getter.fileGetter as Getter
import gui.dashGUI as dgui
import gui.tkinterGUI as tgui
import pandas as pd

getter=Getter.multiGetter
features=getter()

features_df=pd.DataFrame(data=features.values(),index=features.keys())
print(features_df)