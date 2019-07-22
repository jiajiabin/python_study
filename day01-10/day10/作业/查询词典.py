import pickle
pkl_file = open('manage.pkl', 'rb')

data1 = pickle.load(pkl_file)
print(data1.get_wors_translate("Arab"))

pkl_file.close()