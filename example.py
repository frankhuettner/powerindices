import powerindices  

''' IMPORTANT: ALL INPUTS MUST BE NON-NEGATIVE INTEGERS
WRONG: quota = .51, weigths = [.25, .14, .33, .11, .17]
CORRECT: quota = 51, weigths = [25, 14, 33, 11, 17]
'''

# This example represents the UN security council.
quota,weights = 39, [7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 

# call the functions to compute the respective index
PBIs = powerindices.compute_pbi(quota,weights, minimalWinningCoalitionSize=1)
SSIs = powerindices.compute_ssi(quota,weights, minimalWinningCoalitionSize=1)
CSIs = powerindices.compute_csi(quota,weights)
### The functions return the indices as lists so that
### they are now stored as lists in the PBIs, SSIs, and CSIs.
### We could simply print these list:
# print(SSIs)  
## but we've prepared a formated output below.


### EU after Brexit
# EU28POP = [332490349,8772865,11351727,7101859,4154213,854802,10578820,5748769,1315635,5503297,66989083,82521653,10768193,9797561,4784383,60589445,1950116,2847904,590667,460297,17081507,37972964,10309573,19644350,5435343,2065895,46528966,9995153,65808573]
# EU28ROUNDED = [int(round(i/10000)) for i in EU28POP]
# quota,weights = EU28ROUNDED[0]-EU28ROUNDED[-1],EU28ROUNDED[1:-1]
# PBIs = powerindices.compute_pbi(quota,weights, minimalWinningCoalitionSize=15)
# SSIs = powerindices.compute_ssi(quota,weights, minimalWinningCoalitionSize=15)
# CSIs = powerindices.compute_csi(quota,weights, minimalWinningCoalitionSize=15)




### Formated output
numberDigits = 5
formatspec = '{0:.%df}' % numberDigits
print('='*(22 + (len(weights)-1)*(numberDigits+5)))
print('weight of i  || '+' | '.join([formatspec.format(item) for item in weights]))
print('-'*(22 + (len(weights)-1)*(numberDigits+5)))
print('SSI of i     || '+' | '.join([formatspec.format(item) for item in SSIs]))
print('PBI of i     || '+' | '.join([formatspec.format(item) for item in PBIs]))
print('CSI of i     || '+' | '.join([formatspec.format(item) for item in CSIs]))
print('='*(22 + (len(weights)-1)*(numberDigits+5)))
print('(quota: {})'.format(quota))


# ##### uncomment the following to get results printed into a file output.txt
# numberDigits = 5   # Set how many digits after comma you want in the output file?
# formatspec = '{0:.%df}' % numberDigits
# with open('powerindices_output.txt', 'a') as f:   
#     f.write('quota: {}'.format(quota)+'\n')
#     f.write('  weight ,      SSI ,      CSI ,      PSI  \n')
#     for i in range(len(SSIs)):
#         f.write(' , '.join([formatspec.format(item) for item in [weights[i], SSIs[i],CSIs[i],PBIs[i] ] ])+'\n')
# # #####


# ## EU (computation might take a minute) 
# ## The weights are the population rounded by 10000 of each country.
# ## (It is rounded because otherwise it takes longer).
# ## 65% of the total population must be represented.
# ## Moreover, at least 55% of the countries must approve, i.e. 16 countries.
# EU28POP = [11351727, 7101859,10578820,5748769,82521653,1315635,4784383,10768193,46528024,66989083,4154213,60589445,854802,1950116,2847904,590667,9797561,460297,17081507,8772865,37972964,10309573,19644350,2065895,5435343,5503297,9995153,65808573]
# EU28Countries = ['Belgium','Bulgaria','Czech Republic','Denmark','Germany','Estonia','Ireland','Greece','Spain','France','Croatia','Italy','Cyprus','Latvia','Lithuania','Luxembourg','Hungary','Malta','Netherlands','Austria','Poland','Portugal','Romania','Slovenia','Slovakia','Finland','Sweden','UK' ]
# weights = [int(round(i/10000)) for i in EU28POP]
# quota = int(round(0.65*sum(EU28POP)/10000))
# PBIs = powerindices.compute_pbi(quota,weights, minimalWinningCoalitionSize=16)
# SSIs = powerindices.compute_ssi(quota,weights, minimalWinningCoalitionSize=16)
# CSIs = powerindices.compute_csi(quota,weights, minimalWinningCoalitionSize=16)

# # # Formated output EU28
# numberDigits = 5
# formatspec = '{0:.%df}' % (numberDigits)
# print('EU (quota: {}, sum of CSI: {:.5f} ,sum of PBI: {:.5f})'.format(quota,sum(CSIs),sum(PBIs)))
# print('country       |   weight  ||    SSI |     CSI |     PSI |  CSI/PSI \n')
# for i in range(len(SSIs)):
#    print('{:14s}|{:10d} ||'.format(EU28Countries[i],weights[i]) + ' | '.join([formatspec.format(item) for item in [SSIs[i],CSIs[i],PBIs[i],CSIs[i]/PBIs[i] ] ])+'\n')

# ### uncomment the following to get results printed into a file powerindices_output.txt
# #numberDigits = 8   # Set how many digits after comma you want in the output file?
# #formatspec = '{0:.%df}' % numberDigits
# #with open('EU28.txt', 'a') as f:   
# #    f.write('country,  weight ,      SSI ,      CSI ,      PSI ,  CSI/PSI \n')
# #    for i in range(len(SSIs)):
# #        f.write(EU28Countries[i]+ ', {}, '.format(weights[i]) +' , '.join([formatspec.format(item) for item in [SSIs[i],CSIs[i],PBIs[i],CSIs[i]/PBIs[i] ] ])+'\n')
# ##
