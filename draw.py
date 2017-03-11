# -*- coding: utf-8 -*-
# @Time    : 2017/3/9 下午6:32
# @Author  : Zhixin Piao 
# @Email   : piaozhx@seu.edu.cn

import string
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    TPR = [0.0020080321, 0.0030120481, 0.015060241, 0.030120483, 0.042168673, 0.062248997, 0.082329318, 0.096385539, 0.12148594, 0.15361446, 0.18473895,
           0.21586345, 0.24297188, 0.27208835, 0.30321285, 0.33835343, 0.37449798, 0.41666666, 0.44176707, 0.47690764, 0.51305223, 0.54016066, 0.562249,
           0.59337348, 0.61144578, 0.63453817, 0.66265059, 0.68473893, 0.71084338, 0.72590363, 0.74598396, 0.76606429, 0.78915662, 0.8012048, 0.81526107,
           0.82831323, 0.84437752, 0.86345381, 0.86746991, 0.88152611, 0.89156628, 0.89859438, 0.9076305, 0.91666669, 0.92369479, 0.92971885, 0.93373495,
           0.93373495, 0.937751, 0.94277108, 0.9518072, 0.9558233, 0.95883536, 0.96184736, 0.96686745, 0.96887553, 0.97088355, 0.97389561, 0.97690761,
           0.97891569, 0.98092371, 0.98092371, 0.98192769, 0.98293173, 0.98293173, 0.98393571, 0.98493975, 0.98594379, 0.98594379, 0.98795182, 0.98795182,
           0.9889558, 0.98995984, 0.98995984, 0.99096388, 0.99096388, 0.99196786, 0.9929719, 0.99397588, 0.99497992, 0.99497992, 0.99598396, 0.99598396,
           0.99598396, 0.99598396, 0.99598396, 0.99598396, 0.99598396, 0.99598396, 0.99598396, 0.99698794, 0.99799198, 0.99799198, 0.99799198, 0.99799198,
           0.99799198, 0.99799198, 0.99799198, 0.99799198, 0.99799198, 0.99799198, 0.99799198, 0.99899596, 0.99899596, 0.99899596, 0.99899596, 0.99899596,
           0.99899596, 0.99899596, 0.99899596, 0.99899596, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
           1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
           1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
           1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

    FPR = [0.0, 0.0, 0.00011106175, 0.0006663705, 0.0012216793, 0.0022212351, 0.0029986673, 0.0041092848, 0.0047756555, 0.0062194578, 0.0078853844,
           0.0095513109, 0.011328299, 0.012438916, 0.014771213, 0.017880943, 0.021101732, 0.024544647, 0.027210129, 0.029209239, 0.032652155, 0.035872944,
           0.038982674, 0.042203464, 0.04509107, 0.047978677, 0.051754776, 0.055641938, 0.060084406, 0.064637937, 0.071301647, 0.077298976, 0.084073745,
           0.090626389, 0.099067084, 0.1053976, 0.1129498, 0.12005775, 0.1280542, 0.13560639, 0.14449133, 0.15393159, 0.16281652, 0.17258996, 0.1829187,
           0.19346957, 0.20502, 0.21434918, 0.22345625, 0.23467349, 0.24433585, 0.25410929, 0.26554865, 0.27454466, 0.28598401, 0.29653487, 0.30808529,
           0.31952465, 0.32940915, 0.34229231, 0.35506442, 0.36561528, 0.37738782, 0.38749444, 0.39848956, 0.40926254, 0.42125723, 0.43091959, 0.44380274,
           0.45679697, 0.46679252, 0.4776766, 0.48611727, 0.49455798, 0.50444245, 0.51577079, 0.52487785, 0.53509551, 0.5446468, 0.55508661, 0.56430477,
           0.5725233, 0.58229673, 0.59129274, 0.60151047, 0.6111728, 0.62161261, 0.63016438, 0.64038205, 0.6494891, 0.65770769, 0.66625947, 0.67503333,
           0.68325192, 0.69035983, 0.69724566, 0.70357621, 0.71079522, 0.71845847, 0.72667706, 0.73645049, 0.74411374, 0.75233227, 0.76088405, 0.77099067,
           0.77776545, 0.7839849, 0.79087073, 0.79831189, 0.80564195, 0.81297201, 0.8179698, 0.82496667, 0.8300755, 0.83607286, 0.84062636, 0.84662372,
           0.85262108, 0.85839629, 0.86361617, 0.86905819, 0.87450022, 0.87927586, 0.88538426, 0.89149266, 0.89649045, 0.90137714, 0.90548646, 0.91003996,
           0.91314971, 0.91714793, 0.92092401, 0.92569971, 0.92992002, 0.93402934, 0.93769437, 0.94102621, 0.94446915, 0.94669038, 0.9488005, 0.95290983,
           0.95757443, 0.96001774, 0.96290535, 0.96512663, 0.96701467, 0.96901375, 0.97090185, 0.97201246, 0.97378945, 0.97601068, 0.97723234, 0.97912037,
           0.98078632, 0.9814527, 0.98256332, 0.98400712, 0.98522878, 0.98656154, 0.9878943, 0.98911595, 0.98989338, 0.9907819, 0.99111503, 0.99167037,
           0.99222571, 0.99300313, 0.9938916, 0.99478012, 0.9953354, 0.99566859, 0.99622393, 0.99666816, 0.9967792, 0.99711239, 0.99744558, 0.99766773,
           0.99777877, 0.99811196, 0.99833405, 0.9985562, 0.99877834, 0.99888939, 0.99888939, 0.99900043, 0.99911153, 0.99922258, 0.99922258, 0.99944466,
           0.99955577, 0.99955577, 0.99955577, 0.99955577, 0.99955577, 0.99955577, 0.99955577, 0.99966681, 0.99966681, 0.99988896, 0.99988896]

    plt.plot(FPR, TPR, 'b')  # ,label=$cos(x^2)$)
    # plt.plot(years, price, 'r')
    plt.xlabel('FPR')
    plt.ylabel('TPR')
    # average
    # price(*2000
    # yuan))
    # plt.ylim(0, 15)
    plt.title('ROC')
    plt.legend()
    plt.show()