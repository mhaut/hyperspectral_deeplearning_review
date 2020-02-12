import numpy as np
import matplotlib.pyplot as plt




names = np.array(["Tensorflow", "Keras", "OpenCV", "Caffe", "PyTorch", "CNTK", "MXNET", "ConvnetJS", "Deeplearning4j", "Theano", "Paddle", "fastAI", "Chainer", "Horovod", "BigDL", "MatConvNet"])

stars_20180716 = np.array([102270, 30349, 25313, 24865, 16267, 14597, 14141, 9125, 9084, 8374, 7043, 5279, 3864, 2757, 2509, 1033])
forks_20180716 = np.array([64049, 11341, 18178, 15237, 3681, 3878, 5214, 1815, 4289, 2445, 1927, 1733, 1028, 370, 568, 666])


stars_20190907 = np.array([133322, 43786, 37798, 29000, 31416, 16394, 17647, 9787, 11130, 8900, 9851, 15384, 5028, 7380, 3152, 1205])
forks_20190907 = np.array([77067, 16673, 27983, 17530, 7712, 4365, 6276, 1951, 4735, 2504, 2628, 5517, 1327, 1130, 797, 713])

diff_stars = np.array([b-a for a,b in zip(stars_20180716, stars_20190907)])
diff_forks = np.array([b-a for a,b in zip(forks_20180716, forks_20190907)])


#plt.clf()
#plt.bar(np.arange(0,len(stars_20180716)*2,2)-0.5, stars_20180716, width=1, color="b", label="Github stars")
#plt.bar(np.arange(0,len(stars_20180716)*2,2)+0.5, forks_20180716, width=1, color="r", label="Github forks")
#plt.gcf().subplots_adjust(bottom=0.15)
#plt.legend()
#plt.xticks(np.arange(0,len(stars_20190907)*2,2), names, rotation=30, fontsize=6.5)
#plt.savefig('bar_diagram_2018.png', dpi=600, format='png', bbox_inches='tight')
##plt.show()

#plt.clf()
#plt.bar(np.arange(0,len(stars_20190907)*2,2)-0.5, stars_20190907, width=1, color="b", label="Github stars")
#plt.bar(np.arange(0,len(stars_20180716)*2,2)+0.5, forks_20190907, width=1, color="r", label="Github forks")
#plt.gcf().subplots_adjust(bottom=0.15)
#plt.legend()
#plt.xticks(np.arange(0,len(stars_20190907)*2,2), names, rotation=30, fontsize=6.5)
#plt.savefig('bar_diagram_2019.png', dpi=600, format='png', bbox_inches='tight')
##plt.show()

#plt.clf()
#inds = np.array(diff_stars).argsort()[::-1]

#plt.bar(np.arange(0,len(stars_20190907)*2,2)-0.5, np.array(diff_stars)[inds], width=1, color="b", label="Github stars")
#plt.bar(np.arange(0,len(stars_20180716)*2,2)+0.5, np.array(diff_forks)[inds], width=1, color="r", label="Github forks")
#plt.gcf().subplots_adjust(bottom=0.15)
#plt.legend()
#plt.xticks(np.arange(0,len(stars_20190907)*2,2), np.array(names)[inds], rotation=30, fontsize=6.5)
#plt.savefig('bar_diagram_diff.png', dpi=600, format='png', bbox_inches='tight')
##plt.show()

inds = np.array(stars_20190907).argsort()[::-1]
plt.clf()
plt.bar(np.arange(0,len(stars_20190907)*2,2)-0.5, stars_20190907[inds], width=1, color="blue", label="Github stars")
plt.bar(np.arange(0,len(stars_20180716)*2,2)+0.5, forks_20190907[inds], width=1, color="red", label="Github forks")


plt.bar(np.arange(0,len(stars_20180716)*2,2)-0.5, stars_20180716[inds], width=1, color="royalblue")
plt.bar(np.arange(0,len(stars_20180716)*2,2)+0.5, forks_20180716[inds], width=1, color="indianred")

for a,b,c in zip(names[inds], stars_20190907[inds], forks_20190907[inds]):
	print(a,b,c)
exit()


plt.gcf().subplots_adjust(bottom=0.15)
plt.legend()
plt.xticks(np.arange(0,len(stars_20190907)*2,2), names[inds], rotation=60, fontsize=6.5)
plt.savefig('bar_diagram_join.png', dpi=600, format='png', bbox_inches='tight')
#plt.show()
exit()
