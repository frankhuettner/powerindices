import powerindices

# this example represents the UN security council
quota,weights = 39, [7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 
# quota,weights = 8,[4,4,3,2,1,1]   # a smaller example

# call the functions to compute the respective index
PBIs = powerindices.compute_pbi(quota,weights)
SSIs = powerindices.compute_ssi(quota,weights)
CSIs = powerindices.compute_csi(quota,weights)
# the indices are now stored as lists in the PBIs, SSIs, and CSIs
# print(SSIs)

# FORMATED OUTPUT
numberDigits = 4
formatspec = '{0:.%df}' % numberDigits
print('='*(22 + (len(weights)-1)*(numberDigits+5)))
print('weight  of i || '+' | '.join([formatspec.format(item) for item in weights]))
print('SSI of i     || '+' | '.join([formatspec.format(item) for item in SSIs]))
print('CSI of i     || '+' | '.join([formatspec.format(item) for item in CSIs]))
print('PBI of i     || '+' | '.join([formatspec.format(item) for item in PBIs]))
print('CSI/PBI of i || '+' | '.join([formatspec.format(item) for item in CSIs]))
print('='*(22 + (len(weights)-1)*(numberDigits+5)))
print('(quota: {})'.format(quota))


# ##### uncomment the following to get results printed into a file output.txt
# numberDigits = 5   # Set how many digits after comma you want in the output file?
# formatspec = '{0:.%df}' % numberDigits
# with open('powerindices_output.txt', 'a') as f:   
#     f.write('quota: {}'.format(quota)+'\n')
#     f.write('  weight ,      SSI ,      CSI ,      PSI ,  CSI/PSI \n')
#     for i in range(len(SSIs)):
#         f.write(' , '.join([formatspec.format(item) for item in [weights[i], SSIs[i],CSIs[i],PBIs[i],CSIs[i]/PBIs[i] ] ])+'\n')
# # #####