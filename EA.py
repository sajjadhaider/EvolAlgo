import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

startTime = time.time();
parentSize = 10;
offspringSize = 10;
parents = [[0 for x in range(3)] for x in range(parentSize)];
offspring = [[0 for x in range(3)] for x in range(offspringSize)];

def initialize_parents():
    # random numbers
    for i in range(parentSize):
        for j in range(2):
            parents[i][j] = np.random.uniform(-5,5);
                        
def compute_fitnessP():
    for i in range(parentSize):
        #parents[i][2] = parents[i][0]**2 + parents[i][1]**2;
        #parents[i][2] = (1-parents[i][0])**2 + (parents[i][1] - parents[i][0]*parents[i][0])**2;
        parents[i][2] = (parents[i][0]**2 + parents[i][1] - 11)**2 + (parents[i][0] + parents[i][1]**2 - 7)**2;    
        
def compute_fitnessO():
    for i in range(offspringSize):
        #offspring[i][2] = offspring[i][0]**2 + offspring[i][1]**2;
        #offspring[i][2] = (1-offspring[i][0])**2 + (offspring[i][1] - offspring[i][0]*offspring[i][0])**2;
        offspring[i][2] = (offspring[i][0]**2 + offspring[i][1] - 11)**2 + (offspring[i][0] + offspring[i][1]**2 - 7)**2; 

def mutation(ind):
    if np.random.uniform(0,1) < 0.2:
        offspring[ind][0] = offspring[ind][0] + np.random.uniform(-0.25,0.25);
    if np.random.uniform(0,1) < 0.2:
        offspring[ind][1] = offspring[ind][1] + np.random.uniform(-0.25,0.25);
    
    if offspring[ind][0] > 5:
        offspring[ind][0] = 5;
    elif offspring[ind][0] < -5:
        offspring[ind][0] = -5;
        
    if offspring[ind][1] > 5:
        offspring[ind][1] = 5;
    elif offspring[ind][1] < -5:
        offspring[ind][1] = -5;
    

def crossover(ind, p1, p2):
    offspring[2*ind] =  parents[p1][0:1] + parents[p2][1:2] + [0];
    offspring[2*ind+1] =  parents[p2][0:1] + parents[p1][1:2] + [0];                    
    mutation(2*ind);
    mutation(2*ind+1);        
      
def parent_selection():
    for k in range(5):
        index1 = np.random.randint(0,parentSize);
        index2 = np.random.randint(0,parentSize);
        crossover(k,index1,index2);

def survival_selection():    
    tempArray = [[0 for x in range(3)] for x in range(parentSize+offspringSize)];    
    for i in range(parentSize):
        tempArray[i] = parents[i];        
    for i in range(offspringSize):
        tempArray[parentSize+i] = offspring[i];       
    tempArray = sorted(tempArray, key=lambda x: x[2], reverse=True);
    for i in range(parentSize):
        parents[i] = tempArray[i];
    
iterationCount = 2000;                    
genSize = 150  ;           
xaxis = [i for i in range(genSize)];
bsf = [[0 for x in range(iterationCount)] for x in range(genSize)];

for i in range(iterationCount):                                                    
    initialize_parents();
    compute_fitnessP();
    for generation in range(genSize):    
        parent_selection();    
        compute_fitnessO();
        survival_selection();
        bsf[generation][i] = parents[0][2];

np_bsf = np.array(bsf);
avg_bsf = np_bsf.mean(axis=1)        
plt.plot(xaxis,avg_bsf);
plt.ylabel('Avg Best-so-Far');
plt.xlabel('Generations');
plt.show();
print time.time() - startTime;