import powerindices



US_states = ["Alabama",
"Alaska",
"Arizona",
"Arkansas",
"Colorado",
"Connecticut",
"Delaware",
"Florida",
"Georgia",
"Idaho",
"Indiana",
"Iowa",
"Kansas",
"Kentucky",
"Louisiana",
"Maine",
"Michigan",
"Minnesota",
"Mississippi",
"Missouri",
"Montana",
"Nebraska",
"Nevada",
"New Hampshire",
"New Mexico",
"New York",
"North Carolina",
"North Dakota",
"Ohio",
"Oklahoma",
"Oregon",
"Pennsylvania",
"Rhode Island",
"South Carolina",
"South Dakota",
"Tennessee",
"Texas",
"Utah",
"Virginia",
"West Virginia",
"Wisconsin",
"Wyoming",
"Hawaii",
"Illinois",
"Kalifornien",
"Maryland",
"Massachusetts",
"New Jersey",
"Vermont",
"Washington",
"Washington D.C."]

votes =[9,
3,
11,
6,
9,
7,
3,
29,
16,
4,
11,
6,
6,
8,
8,
4,
16,
10,
6,
10,
3,
5,
6,
4,
5,
29,
15,
3,
18,
7,
7,
20,
4,
9,
3,
11,
38,
6,
13,
5,
10,
3,
4,
20,
55,
10,
11,
14,
3,
12,
3]


weights = votes 
quota = 270 
PBIs = powerindices.compute_pbi(quota,weights)
SSIs = powerindices.compute_ssi(quota,weights)
CSIs = powerindices.compute_csi(quota,weights)
print('sum of SSI: {}, sum of CSI: {}, quota: {}, number of voters: {}'.format(sum(SSIs),sum(CSIs),quota,len(weights)))


# ## Formated output
numberDigits = 15
formatspec = '{0:.%df}' % numberDigits
print('state,  weight ,      SSI ,      CSI ,      PSI ')
for i in range(len(US_states)):
        print('{:>15} , {:4d}, '.format(US_states[i],weights[i])+' , '.join([formatspec.format(item) for item in [SSIs[i],CSIs[i],PBIs[i] ] ]))

# ##### uncomment the following to get results printed into a file output.txt
numberDigits = 8   # Set how many digits after comma you want in the output file?
formatspec = '{0:.%df}' % numberDigits
with open('electoral_college.txt', 'a') as f:   
    f.write('quota: {}'.format(quota)+'\n')
    f.write('quota: {}'.format(quota)+'\n')
    f.write('state,  weight ,      SSI ,      CSI ,      PSI  \n')
    for i in range(len(SSIs)):
        f.write(US_states[i]+', '+str(weights[i])+', ' + ' , '.join([formatspec.format(item) for item in [SSIs[i],CSIs[i],PBIs[i] ] ])+'\n')
# #####