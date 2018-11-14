import pandas as pd

data = pd.read_excel("C:/Users/TOOanau/PycharmProjects/SeleniumServiAidInfo/equipment-leader-info.xlsx")
ArticleNumber = data['Article Number']
#print(articlenumber[1])
#print(ArticleNumber)
for x in ArticleNumber:
    print(x)
    #print(ArticleNumber[x])