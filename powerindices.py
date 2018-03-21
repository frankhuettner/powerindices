'''
Copyright 2018 Frank Huettner

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''

# from numba import jit   # import numba and uncomment the @jit infront of the function if code is too slow -- can be around factor 3 for large intergers
from math import factorial as fac
import numpy as np


# @jit
def number_coalitions_weighting_x(quota,weights):  
    ''' input,  integers, quota
                list or tuple of integers, weight vector, 
        output, vector with lenght sum(weights)+1, containing quota many
                leading zeros 0,...,0 and
                then the number of coalitions which weight quota,...,sum(weights) 
                i.e. whose members have weights summing up to x = quota,...,sum(weights)
    ''' 
    W = np.array(weights, dtype=int)
    n = np.shape(W)[0]
    Wsum = np.sum(W)
    C = np.zeros(Wsum+1, dtype=int)
    # Backward counting filling C[x] for x = quota,...,Wsum 
    C[Wsum]=1
    maxQuWsumcum = np.maximum(quota, Wsum-np.cumsum(W,dtype=int))+W  # maxQuWsumcum = max{quota+W_i,Wsum-Wacc incl i} 
    for i in range(n):
        C[maxQuWsumcum[i]-W[i]:Wsum+1-W[i]] += C[maxQuWsumcum[i]:Wsum+1]
    # Forward counting filling C[x] for x = 0,...,quota-1 
    # C[0]=1            
    # minQuWcum = np.minimum(quota, np.cumsum(W,dtype=int)) 
    # for i in range(n):
    #     W_i=W[i]
    #     for x in range(minQuWcum[i],W_i-1,-1):
    #         C[x] += C[x-W_i]
    return C


# @jit
def number_coalitions_weighting_x_including_i(quota,weights,C,i):
    ''' input,  number, quota
                list or tuple of integers, weight vector
                C, a matrix storing number_coalitions_weighting_x_having
                i, a player
        output, numpy array, i.e. vector with length (sum(weights)+1)  
                leading zeros 0,...,0 and
                then the number of coalitions which weight x= quota,...,sum(weights) and include i
    ''' 
    n = len(weights)
    Wsum = sum(weights) 
    w_i = weights[i]            
    Cwith_i = np.zeros(Wsum+1, dtype=int)
    ###### Cwith_i[x] = number of coalitions with i weighting x 
    ##### we just need the entries for x = q,...,Wsum but could compute the others with the commented code below
    Cwith_i[Wsum-w_i+1:Wsum+1] = C[Wsum-w_i+1:Wsum+1] 
    for x in range(Wsum-w_i,quota-1,-1):      # calculate Cwith_i  
        Cwith_i[x]=(C[x]-Cwith_i[x+w_i])
        # Cwout_i = C[0:w_i].tolist()              # Cwout_i[x] = number of coalitions without i weighting x 
    # for x in range(w_i,quota):      # calculate Cwout_i from C 
    #     Cwout_i.append(C[x]-Cwout_i[x-w_i])
    # Cwith_i[0:quota] = C[0:quota] -Cwout_i[0:quota]    # we do not need this part of Cwith_i[x]
    return Cwith_i


# @jit
def number_coalitions_weighting_x_having_size_s(quota,weights):
    ''' input,  int, quota
                list or tuple of integers, weight vector 
        output, numpy array, i.e. matrix with dimension (sum(weights)+1) * (len(weights)+1), 
                containing containing quota many leading 0-rows and 
                then the number of coalitions which weight x= quota,...,sum(weights) and have size s= 0,...,len(weights) 
                e.g. C = number_coalitions_of_size_s_weighting_x(8,[1,1,2,3,4,4]) gives
                C[-1][-1] = 1 means there is 1 coalition that has weight sum(weights) and size len(weights) (grand coalition)
                C[10][4] = 5 means there are 5 coalition that weight 10 and have size 4 ({4411},{4321},{4321},{4321},{4321})   
                uncomment code at the end to also get C[3][2] = 2 means there are 2 coalition that weight 3 and have size 2 ({12},{12})  
    ''' 
    W = np.array(weights, dtype=int)
    Wsum = np.sum(W)
    n = np.shape(W)[0]
    C = np.zeros((Wsum+1,n+1), dtype=int)
    C[Wsum,n]=1
    # Backward counting filling C[x] for x = quota,...,Wsum
    maxQuWsumcum = np.maximum(quota, Wsum-np.cumsum(W,dtype=int))+W  # maxQuWsumcum = max{quota+W_i,Wsum-Wacc incl i} 
    for i in range(n):
        C[maxQuWsumcum[i]-W[i]:Wsum+1-W[i],:n] += C[maxQuWsumcum[i]:Wsum+1,1:n+1]

        # for s in range(n,0,-1):
        #         C[maxQuWsumcum[i]-W[i]:Wsum+1-W[i],s-1] += C[maxQuWsumcum[i]:Wsum+1,s]
    # Forward counting filling C[x,s] for x = 0,...,quota-1 
    # minWaccQ = np.minimum(quota, np.cumsum(W,dtype=int)) 
    # for i in range(n):
    #     W_i=W[i]
    #     for x in range(minWaccQ[i],W_i-1,-1):
    #         for s in range(1,n+1):
    #             C[x,s] += C[x-W_i,s-1]
    return C


# @jit
def number_coalitions_weighting_x_having_size_s_including_i(quota,weights,C,i):
    ''' input,  int, quota
                list or tuple of integers, weight vector
                C, a matrix storing number_coalitions_weighting_x_having_size_s
                i, a player
        output, numpy array, i.e. matrix with dimension (sum(weights)+1) * (len(weights)+1), 
                containing containing quota many leading 0-rows and 
                then the number of coalitions which weight x= quota,...,sum(weights) and have size s= 0,...,len(weights) 
                and which include i
    ''' 
    n = len(weights)
    Wsum = sum(weights) 
    w_i = weights[i]            
    ##### Cwith_i[x,s] stores the number of coalitions with i weighting x having size s
    ##### we just need the rows x = q,...,Wsum 
    Cwith_i = np.zeros((Wsum+1,n+1), dtype=int)
    Cwith_i[Wsum-w_i+1:Wsum+1,:] = C[Wsum-w_i+1:Wsum+1,:] 
    if w_i == 0 : 
        Cwith_i[Wsum,n] = C[Wsum,n] 
    for x in range(Wsum-w_i,quota-1,-1):      # calculate Cwith_i  
        for s in range(n-1,-1,-1):
            Cwith_i[x,s]=(C[x,s]-Cwith_i[x+w_i,s+1])
    return Cwith_i


def compute_pbi(quota,weights,minimalWinningCoalitionSize=1):
    ''' input,  int>0, the quota necessary to be winning i.e. a coalition holding W as weights wins if W>=quota
                list of integers>0, weights of the committee members
        output, list, stores the Penrose Banzhaf index of members with entries 

        Example: result = PBI(8,[4,4,3,2,1,1]) gives result[2]=0.375 meaning that Penrose Banzhaf index of member with weight 3 is .375
        
        >>> computePBI(8,[4,4,3,2,1,1])
        [0.5, 0.5, 0.375, 0.125, 0.125, 0.125]
    ''' 
    n = len(weights)
    Wsum = sum(weights)    
    for i in range(n):
        if weights[i] > Wsum - quota:
            oldweigth_i = weights[i]
            weights[i] = Wsum - quota + 1
            quota = quota - oldweigth_i + weights[i]
    PBIfactor = 1/2**(n-1)
    PBIs = []
    if minimalWinningCoalitionSize==1:
        C = number_coalitions_weighting_x(quota,weights)
        for i in range(n):
            Cwith_i = number_coalitions_weighting_x_including_i(quota,weights,C,i)        
            PBI = np.sum(Cwith_i[quota:quota+weights[i]])*PBIfactor  
            PBIs.append(PBI) 
    else: 
        C = number_coalitions_weighting_x_having_size_s(quota,weights)
        for i in range(n):
            Cwith_i = number_coalitions_weighting_x_having_size_s_including_i(quota,weights,C,i)
            w_i = weights[i]
            PBI = 0
            for s in range(minimalWinningCoalitionSize-1,n):
                    PBI += Cwith_i[quota:quota+w_i,s+1].sum(axis=0)            
            PBI += Cwith_i[quota+w_i:Wsum+1,minimalWinningCoalitionSize].sum(axis=0)
            PBI *=PBIfactor
            PBIs.append(PBI) 
    return PBIs


def compute_ssi(quota,weights,minimalWinningCoalitionSize=1):
    ''' input,  int, the quota necessary to be winning i.e. a coalition holding W as weights wins if W>=quota
                list of integers, weights of the committee members
        output, dict, stores the Shapley Shubik index of members with entries (weight: SSI)
    ''' 
    n = len(weights)
    Wsum = sum(weights)    
    for i in range(n):
        if weights[i] > Wsum - quota:
            oldweigth_i = weights[i]
            weights[i] = Wsum - quota + 1
            quota = quota - oldweigth_i + weights[i]
    C = number_coalitions_weighting_x_having_size_s(quota,weights)
    SSIfactors = [ fac(s)*fac(n-s-1)/fac(n) for s in range(n)] 
    SSI = [0]*n
    for i in range(n):
        w_i = weights[i]
        Cwith_i = number_coalitions_weighting_x_having_size_s_including_i(quota,weights,C,i)
        for s in range(minimalWinningCoalitionSize-1,n):
                SSI[i] += SSIfactors[s] * Cwith_i[quota:quota+w_i,s+1].sum(axis=0) 
        if minimalWinningCoalitionSize > 1:
            SSI[i] += SSIfactors[minimalWinningCoalitionSize] \
                      * Cwith_i[quota+w_i:Wsum+1,minimalWinningCoalitionSize].sum(axis=0)    
    return SSI

    
def compute_csi(quota,weights,minimalWinningCoalitionSize=1):
    ''' input,  int, the quota necessary to be winning i.e. a coalition holding W as weights wins if W>=quota
                list of integers, weights of the committee members
        output, dict, stores the Coleman Shapley index of members with entries (weight: CSI)
    ''' 

    n = len(weights)
    Wsum = sum(weights)    
    for i in range(n):
        if weights[i] > Wsum - quota:
            oldweigth_i = weights[i]
            weights[i] = Wsum - quota + 1
            quota = quota - oldweigth_i + weights[i]
    C = number_coalitions_weighting_x_having_size_s(quota,weights)
    CSIfactors =[0]+ [[ fac(n-t)/fac(n)*fac(s+t-1)/fac(s)/2**(s+t-1) \
                        for s in range(n-t+1)] for t in range(1,n+1)]   #[0] is for being able to call t=1,... later
    CSI = [0]*n
    for i in range(n):
        w_i = weights[i]
        Cwith_i = number_coalitions_weighting_x_having_size_s_including_i(quota,weights,C,i)
        for t in range(minimalWinningCoalitionSize,n+1):
            for s in range(n-t+1):
                CSI[i] += CSIfactors[t][s] * Cwith_i[quota:quota+w_i,t].sum(axis=0)
        if minimalWinningCoalitionSize > 1:
            for s in range(n-minimalWinningCoalitionSize+1):
                CSI[i] += CSIfactors[minimalWinningCoalitionSize][s] \
                          * Cwith_i[quota+w_i:Wsum+1,minimalWinningCoalitionSize].sum(axis=0)  
    return CSI
