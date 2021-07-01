import pandas as pd
import os
import schedule
import sys

limite_risultati = 24

#######################################################
def leggi_csv(tag,nomefile):
    df = pd.read_csv(nomefile)
    print(df.head(limite_risultati))
    pwd = os.getcwd()
    os.system("instagram-scraper "+tag+ " --tag --destination {}\\"+tag+"".format(pwd))

#######################################################

a = sys.argv[1]
b = sys.argv[2]
c = 3600

schedule.every(c).seconds.do(leggi_csv(a,'.//'+b))


