This project uses an Excel file that includes all countries' real GDP data from Penn World Table.
This project filters the data and performs a time series analysis for each (Europe) OECD country from to 2000 to 2019.
- Independent variable: year
- Dependent variable: natural log of RGDP per capita of a country

Features: script stores the time series analysis in a dictionary, and provides regression interpretation for each country selected.
- Country(key):regression(value)

Barchart displays and ranks the average annual RGDP per capita growth rate of all OECD countries in Europe.
  ![barplot_with_Matplotlib](https://github.com/user-attachments/assets/a076083b-681d-4da8-8d9b-fd2d2c4e8dda)


Libraries: pandas, openpyxl, seaborn, and matplotlib
