# Name: Eliyho Tsuri
# Id: 201610672
import numpy
import numpy.random
import matplotlib.pyplot as plt
from scipy.spatial import distance
from math import floor
# =================== 1a ==================
# the function returns close to having n organs
def discrete_gauss(n, g = None):
     if g == None:
          g = [0.5,0.5]
     f = g
     while len(f) < n:
          f = numpy.convolve(f, g)
     return f
# =================== 1a ==================
# the function check if the number is on the limit
def check_num(n):
     if n < 2 or n > 1000:
          print("The number is not on limit\n")
          plt.suptitle("The number is not on limit\n")
          my_bar = range(1, 10)
          plt.show()
          return False
     return True
# =================== 1b ==================
# the function summarized the numbers on the list
def sum(my_list):
     my_sum = 0
     for index in my_list:
          my_sum += index
     return my_sum
# ================== 1cd ==================
# the function check the effect of non-optimal nuclear 
# use and the function show the graph results
def show_discrete_gauss(g = None):
     my_list = [2,5,10,25,50,100,500,1000]
     if g is None:
          g = [0.5,0.5]
     for i in my_list:
          if check_num(i) == False:
               return
          result = discrete_gauss(i,g)
          show("The discrete gauss results",result)
# ================= show ==================
# this function getting title and results graph
# the function show the title on the graph
def show(title,result):
     plt.suptitle(title)
     plt.xlabel("The x axis")
     plt.ylabel("The y axis")
     my_bar = range(1, len(result) + 1)
     plt.bar(my_bar, result)
     plt.show()
# =================== 1e ==================
# the function getting array and move the  
# results to the center of the graph
def move_peek_to_center(array):
     min_size = get_min_size(array)
     my_array = peek_center(min_size,array)
     return my_array
# =================== 1e ==================
# the function getting the list and return the  
# min of the number on the list of the results
def get_min_size(array):
     x = array.tolist().index(max(array))
     y = len(array) - array.tolist().index(max(array))
     min_size = min([x , y])
     return min_size
# =================== 1e ==================
# the function concentrates the values ​​in the  
# list and returns the new list after the  ​​ 
# values in the list have been centered
def peek_center(min_size,array):
     x = (array.tolist().index(max(array)) - min_size)
     y = (array.tolist().index(max(array)) + min_size)
     my_array = array[x:y]
     return my_array
# =================== 1e ==================
# the function getting 2 list and crop them   
# and return the middle of the tow lists
def crop(list1,list2):
     if len(list1) > len(list2) or len(list1) == len(list2):
          size = len(list1) - len(list2)
     else:
          size = len(list2) - len(list1)
     my_list = list1[floor(size / 2):floor(len(list1) - size / 2)]
     return my_list
# =================== 1e ==================
# the function show the distance between the 
# nearest built with the optimal nucleus
def cosine_distance(n,optimal_n):
     result = []
     for a in numpy.arange(0.02, 0.98, 0.02):
          non_optimal_n = discrete_gauss(n,[a,1-a])
          non_optimal = move_peek_to_center(non_optimal_n,)
          optimal_cropped_val = crop(optimal_n, non_optimal)
          result.append(distance.cosine(optimal_cropped_val,non_optimal))
     show("The distance between nearest built and optimal nucleus",result)
# =================== 2a =====================
# the function roll the cube over 1-6
def roll_cube():
     x = numpy.random.randint(1,7)
     return x
# =================== 2b =====================
# the function roll 1000 round's 1-6
def roll_results():
     list_results = []
     list_results = [roll_cube() for i in range(0, 1000)]
     roll_list = [numpy.average(list_results[0 : i + 1]) for i in range(0, len(list_results))]
     return roll_list
# =================== 2d =====================
# the function compare on the dropping_vs_dumping cube
def dropping_vs_dumping(n):
     roll_list = roll_results()
     show_list(roll_list,"mean of x(1:i) as a function of i","numbers of rolls i","mean value")
# =================== show ===================
# the function show the results of dropping_vs_dumping function
def show_list(roll_list,title,x,y):
     plt.plot([0, len(roll_list)], [3.5, 3.5], 'r', roll_list, 'b')
     plt.title(title)
     plt.xlim(1, 1000)
     plt.ylim(1, 6)
     plt.xlabel(x)
     plt.ylabel(y)
     plt.show()
# =================== 2e =====================
# the function round 100 rounds and every round 1000 throws the die
# the function The function calculates the average and variance of 
# the 100 trials per 1000 times of cube injection in each experiment
def average_vs_variance(n):
     m_list = [roll_results() for i in range(0, 100)]
     calc_average(m_list)
     calc_variance(m_list)
# =================== 2e =====================
# the function calc the average of the 100 on 1000 
# rolls the function show the result on the graph
def calc_average(m_list):
     average_list = [numpy.average([m_list[i][j] for i in range(0, len(m_list))]) for j in range(0, n)]
     show_average(average_list)
# =================== 2e =====================
# the function calc the variance of the 100 on 1000  
# rolls the function show the result on the graph
def calc_variance(m_list):
     variance_list = [numpy.var([m_list[i][j] for i in range(0, len(m_list))]) for j in range(0, n)]
     show_variance(variance_list)
# =================== 2e =====================
# the function show the average of the rounds
def show_average(cols_avrg):
     plt.plot(cols_avrg, "b", linewidth = 0.5, antialiased=False)
     plt.title("the average over 1000 rolls")
     plt.xlim(1, len(cols_avrg))
     plt.xlabel("number of trials")
     plt.ylabel("mean value")
     plt.show()
# =================== 2e =====================
# the function show the variance of the rounds
def show_variance(cols_var):
     plt.plot(cols_var, "b", linewidth = 0.5, antialiased=False)
     plt.title("the variance over 1000 rolls")
     plt.xlim(1, len(cols_var))
     plt.xlabel("number of trials")
     plt.ylabel("mean value")
     plt.show()              
# -------------------- Q1 ---------------------
# ================= 1a,b,c,d ==================
show_discrete_gauss()
show_discrete_gauss([0.1,0.9]) 
# =================== 1e ======================   
optimal_n = discrete_gauss(999)
cosine_distance(999,optimal_n)
# -------------------- Q2 ---------------------
n = 1000
m = 100
 # =================== 2de ====================
dropping_vs_dumping(n)
dropping_vs_dumping(n)
# ===================== 2f ====================
average_vs_variance(n)
