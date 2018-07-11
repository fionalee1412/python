import pandas as pd
from pandas import DataFrame
from pickle import load
import datetime

# 获取昨天的日期
now = datetime.datetime.now()-datetime.timedelta(days = 1)
date = now.strftime('%Y%m%d')
# 拼接成文件名
predict_filename = 'training_data_yunnan_'+date+'.csv'

# 获取预测文件
predict_dir = '/home/hadoop/veda/data/dfqp/'
predict_path = predict_dir+predict_filename

# 读取文件
predict_file = pd.read_csv(predict_path)
# 获取预测字段
predict_values = predict_file.values
predict_X = predict_values[:,2:44]

# 获取模型
model_path = '/home/hadoop/veda/models/dfqp/GBM.sav'
# 利用模型进行预测
with open(model_path,'rb') as model_f:
    loaded_model = load(model_f)
    predict_y = loaded_model.predict(predict_X)

# 生成结果文件
fuid = predict_file['fuid']
fplatformname = predict_file['fplatformname']
dt = predict_file['dt']
result = pd.DataFrame({'dt':dt,'fplatformname':fplatformname,'fuid':fuid,'predict':predict_y})

# 保存结果文件
save_filename = 'predict_data_yunnan_'+date+'.csv'
predict_save_path = predict_dir+save_filename
result.to_csv(predict_save_path)