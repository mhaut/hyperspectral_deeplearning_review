
from datetime import date
import numpy as np
import matplotlib.pyplot as plt

#https://github.com/opencv/opencv
#https://github.com/BVLC/caffe
#https://github.com/Theano/Theano

#https://github.com/tensorflow/tensorflow

#https://github.com/pytorch/pytorch
#https://github.com/keras-team/keras

#init_time = "21/05/2014"
init_time = "01/01/2014"
init_time = np.array(init_time.split("/")).astype("int")
#fin_time = "07/09/2019"
fin_time = "01/01/2020"
fin_time = np.array(fin_time.split("/")).astype("int")


caffe_t = ["12/01/2015","12/10/2015","18/09/2016","13/03/2017","24/09/2017","08/05/2018", "06/10/2018", "15/03/2019", "07/09/2019"]
caffe_v = [1860, 5730, 11550, 15420, 19290, 23160, 25080, 27030, 29000]
keras_t = ["06/10/2015", "06/10/2016", "04/04/2017", "22/09/2017", "04/02/2018", "02/04/2018", "10/06/2018", "18/11/2018", "23/04/2019", "07/09/2019"]
keras_v = [2610, 7950, 13290, 18630, 23940, 26610, 29280, 34620, 39960, 43939]
openCV_t = ["31/05/2014", "30/05/2015", "18/08/2016", "01/06/2017", "07/04/2018", "09/01/2019", "07/09/2019"]
openCV_v = [2460, 5010, 10080, 15150, 22740, 30360, 38003]
pytorch_t=["22/01/2017","21/04/2017","15/08/2017","09/01/2018","11/05/2018","27/07/2018","04/10/2018","08/01/2019","02/05/2019","02/07/2019","07/09/2019"]
pytorch_v=[2040, 4140, 6240, 10410, 14610, 16710, 18810, 23010, 27180, 29280, 31416]
tensorflow_t = ["10/11/2015", "11/11/2015", "16/11/2015", "11/12/2015", "29/01/2016", "27/03/2016", "09/06/2016", "14/12/2016", "07/09/2019"]
tensorflow_v = [2610, 7950, 10620, 13290, 15960, 18630, 23940, 37290, 133644]
theano_t = ["21/05/2014", "18/03/2015","18/08/2015", "11/12/2015", "17/03/2016", "01/06/2016", "19/02/2017","08/09/2017", "01/10/2018", "07/09/2019"]
theano_v = [540, 1140, 1710, 2310, 2910, 3510, 5280, 6480, 8250, 8900]

#dateaxis = ["21/05/2014", "01/01/2015","01/01/2016","01/01/2017","01/01/2018","01/01/2019", "07/09/2019"]
dateaxis = ["01/01/2014", "01/01/2015","01/01/2016","01/01/2017","01/01/2018","01/01/2019"]

list_n = ["Caffe", "Keras", "OpenCV", "PyTorch", "Theano", "TensorFlow"]
list_t = [caffe_t, keras_t, openCV_t, pytorch_t, theano_t, tensorflow_t]
list_v = [caffe_v, keras_v, openCV_v, pytorch_v, theano_v, tensorflow_v]


for val_t, stars, name in zip(list_t, list_v, list_n):
	positions = []
	for date_star in val_t:
		date_star = np.array(date_star.split("/")).astype("int")
		b = date(init_time[-1],init_time[-2],init_time[-3])
		a = date(date_star[-1],date_star[-2],date_star[-3])
		positions.append((a-b).days)
	plt.plot(positions, stars, label=name, linewidth=3)
plt.ylim(0,150000)
plt.xlim(0,(date(fin_time[-1],fin_time[-2],fin_time[-3]) - \
			date(init_time[-1],init_time[-2],init_time[-3])).days+10)

positions = []
for datea in dateaxis:
	datea = np.array(datea.split("/")).astype("int")
	b = date(init_time[-1],init_time[-2],init_time[-3])
	a = date(datea[-1],datea[-2],datea[-3])
	positions.append((a-b).days)
print(positions)
#exit()
plt.gcf().subplots_adjust(bottom=0.15)
plt.ylabel("Github stars", fontsize = 15)
plt.xlabel("Year", fontsize = 15)
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3, mode="expand", borderaxespad=0.)
plt.xticks(positions, [a.replace("01/01/","") for a in dateaxis], fontsize=10)#, rotation=45)
#plt.xticks(positions, dateaxis, fontsize=10, rotation=45)
plt.yticks(range(0,150000,20000),range(0,150000,20000), fontsize=10)
plt.savefig('stars_github.png', dpi=600, format='png', bbox_inches='tight')
#plt.show()
