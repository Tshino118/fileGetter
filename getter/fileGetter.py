import glob
import os
import datetime
week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
def monoGetter():
    path = glob.glob("./domain/*")[0]
    file, ext = os.path.splitext(os.path.basename(path))
    print('path:',file,'ext:',ext)
    splitfile = file.split('_')
    print('splitpath:',splitfile)
    name,var=splitfile[0],splitfile[1]
    print('name:',name,'var:',var)
    eye_state, dte = var[0],var[1:]
    dte=f"20{dte}"
    dte = datetime.datetime.strptime(dte, '%Y%m%d%H%M%S')
    print('eye_state:',eye_state,'datetime:',dte)
    week_num=datetime.date(dte).weekday()
    print('week_day:',week_days[week_num])
    return {'file':file, 'path':path, 'ext':ext, 'name':name, 'eye_state':eye_state, 'datetime':dte,'week_num':week_num}
    
def multiGetter():
    features={}
    for path in glob.iglob("./domain/*"):
        print(path)
        file, ext = os.path.splitext(os.path.basename(path))
        splitfile = file.split('_')
        name,var=splitfile[0],splitfile[1]
        eye_state, dte = var[0],var[1:]
        dte=f"20{dte}"
        dte = datetime.datetime.strptime(dte, '%Y%m%d%H%M%S')
        week_num=dte.weekday()
        features[f'{file}'] = {'file':file, 'path':path, 'ext':ext, 'name':name, 'eye_state':eye_state, 'datetime':dte,'week_num':week_num}
    return features
    