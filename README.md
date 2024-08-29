Excel file includes all countries' real GDP data from Penn World Table.

This repository provides codes that perform a regression analysis for each OECD country in Europe from to 2000 to 2019
- Explainatory variable: year
- Dependent variable: natural log of RGDP per capita of a country

To perform a regression analysis for all countries or adjust the time period, simply change the Boolean conditions of the filter:
- sorted_data = pwt[(pwt['oecd']==  ) & (pwt['continent']=='   ') & (pwt['year'] >   ) & (pwt['year'] <   ) ... add any conditions you want]


The codes provide:
- A regression table and key parameters for the country selected.
  The dictionary of country(key):regression(value) allows user to input any (Europe) OECD country name to directly obtain its regression output without having to filter each set of data using Excel.
- An interpretation of the coefficient of the OLS line for the country selected.
- A barchart that displays and ranks the average annual RGDP per capita growth rate of all OECD countries in Europe.
  ![barplot_with_Matplotlib](https://github.com/user-attachments/assets/a076083b-681d-4da8-8d9b-fd2d2c4e8dda)


Used pandas, openpyxl, seaborn, and matplotlib
