import pandas as pd
import numpy as np
import os
file_path = os.path.join(os.path.dirname(__file__), "asiap_pwt.xlsx")
pwt = pd.read_excel(file_path,'asiap_pwt')
# data comes from ECO220 class: Penn World Table & Asiaphoria
# use pwt.head() and print(pwt.dtypes) to check code

# create new columns
pwt['rgdp_per_capita'] = pwt['rgdpna']/pwt['pop']
pwt['ln_rgdp_per_capita'] = np.log(pwt['rgdp_per_capita'])

# print(pwt.dtypes)
'''
country                object
countrycode            object
oecd                    int64
continent              object
year                    int64
rgdpna                float64
pop                   float64
rgdp_per_capita       float64
ln_rgdp_per_capita    float64
'''

# sort data: sort out the 2000-2019 data of oecd countries in Europe
sorted_data = pwt[(pwt['oecd']==1) & (pwt['continent']=='Europe') & (pwt['year'] > 1999) & (pwt['year'] < 2020)]
    # select rows whose columns meet certain conditions

# check the specific list of (Europe) oecd countries
countrylist = set()
for countryname in sorted_data['country']:
    countrylist.add(countryname)
countrylist = list(countrylist)
print(f"List of (Europe) oecd countries {countrylist}")
print("This code analyzes (Europe) oecd countries' annual real gdp per capita growth rate.\n")

# analyze annual rgdp growth rate
import statsmodels.api as sm

# build a dictionary to quickly access the regression model of each (Europe) oecd country
i=0
countrydict = {}
while i < len(countrylist):
    temp_var = sorted_data[(sorted_data['country']==str(countrylist[i]))]
    x = temp_var['year']
    y = temp_var['ln_rgdp_per_capita']
    x_n = sm.add_constant(x)  # let the model accurately present the constant term (intercept) in our regression
    model = sm.OLS(y, x_n)  # build regression analysis model
    results = model.fit()  # return results of analysis
    countrydict[countrylist[i]] = results
    i += 1

# define a get coefficient function - since we use natural log, we interpret the coefficient as (b*100)%
def get_coef(var:str):
    coefficient = round(float(countrydict[var].params['year'])*100,4)
    return coefficient

# analyze a specific country's growth rate
def investigate_country():
    investigate = input("Country to investigate: ")
    while True:
        if investigate in countrylist:
            # show explaination of coefficient
            print(f"The real GDP per capita growth rate between 2000-2019 in {investigate} is {get_coef(investigate)}% per year, on average.")
            # show entire regression analysis if needed
            if int(input(f"To see full regression information of {investigate}, input 3: ")) == 3:
                print(f"Information loaded - {investigate}: \n")
                print(countrydict[investigate].summary())
                print('Parameters: ', countrydict[investigate].params)
                print('R2: ', countrydict[investigate].rsquared)
            break
        else:
            investigate = input("Invalid country name, input again (check list above): ")

# prepare for plot drawing
import seaborn as sns
import matplotlib.pyplot as plt

# sort the dictionary according to value, descending order
newdict = {}
for key in countrydict:
     newdict[key] = get_coef(key)
sorted_dict = dict(sorted(newdict.items(), key=lambda item: item[1], reverse=True))

# create 2 lists for plot drawing
countryname_list = []
coef_list = []
for key in sorted_dict:
     coef_list.append(sorted_dict[key])
     countryname_list.append(key)

df = pd.DataFrame({"country":countryname_list, "coef":coef_list})

# draw plot; assign list contents to x, y
def draw_plot():
    plt.figure(figsize=(14, 8)) #1400*800png
    p = sns.barplot(y="country", x="coef", data=df)
    plt.xlabel("2000-2019 RGDP per Capita Growth Rate(%)", size=16)
    plt.ylabel("European OECD Countries", size=16)
    plt.bar_label(p.containers[0])
    plt.title("Comparing Annual RGDP per Capita Growth Rate of European OECD Countries 2000-2019")
    plt.savefig("barplot_with_Matplotlib.png")
    plt.show()

# build menu for user convenience
def Menu():
    print("\n--------------------Menu--------------------")
    print("To analyze a specific country: \t\tinput 1")
    print("To check overall growth rate rank: \tinput 2")
    return input("Input your choice: ")

# run the program - make it smooth
while True:
    keyboard_input = Menu()
    if keyboard_input == "1":
        investigate_country()
        continue
    elif keyboard_input == "2":
        draw_plot()
        continue
    else:
        print("\nExited")
        break