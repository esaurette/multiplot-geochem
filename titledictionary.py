# -*- coding: utf-8 -*-
"""
Plot Title Dictionary
Emily Saurette
March 12, 2019
"""

titledict = {}

headers =  [
        'SAMPLE DEPTH (mbgs)', 
        'Month-Year', 
        'pH', 
        'Eh', 
        'pe',
        'Alkalinity (mg/L as CaCO3)', 
        'Ca',
        'Na', 
        'Li', 
        'Be', 
        'B', 
        'Mg', 
        'Al', 
        'Si', 
        'P', 
        'K', 
        'Ti', 
        'V', 
        'Cr',
        'Mn', 
        'Fe', 
        'Co', 
        'Ni', 
        'Cu', 
        'Zn', 
        'As', 
        'Se', 
        'Sr', 
        'Mo', 
        'Ag', 
        'Cd',
        'Sn', 
        'Sb', 
        'Cs', 
        'Ba', 
        'Tl', 
        'Pb', 
        'U', 
        'F', 
        'Cl', 
        'N(3)', 
        'Br',
        'N(5)', 
        'S(6)', 
        'S(2)', 
        'Formate', 
        'DOC', 
        'PO4-P', 
        'NH4-N', 
        'Fe(2+)',
        'S(2-)', 
        'pct_err', 
        'si_Calcite', 
        'si_Siderite', 
        'si_Gibbsite',
        'si_Alunite', 
        'si_Gypsum', 
        'si_Anglesite', 
        'si_Jarosite',
        'si_Melanterite', 
        'si_Epsomite']

# headers not included as titles: 'CORE', 'TOP (mbgs)', 'BOTTOM (mbgs)', 'LOA (cm)', 'Eo', 'Alkalinity Digits Titrated (to pink endpoint)',
# 'Alkalinity Sample Volume (mL)', 


titles = [
        'Depth\n$\\regular^{(mbgs)}$', 
        'Date', 'pH\n$\\regular^{\ }$',
        'Eh\n$\\regular^{(mV)}$', 
        'pE\n$\\regular^{\ }$', 
        'Alk\n$\\regular^{(mg\ L^{-1},\ CaCO_3)}$',
        'Ca',
        'Na', 
        'Li', 
        'Be', 
        'B', 
        'Mg', 
        'Al', 
        'Si', 
        'P', 
        'K', 
        'Ti', 
        'V', 
        'Cr',
        'Mn', 
        'Fe', 
        'Co', 
        'Ni', 
        'Cu', 
        'Zn', 
        'As', 
        'Se', 
        'Sr', 
        'Mo', 
        'Ag', 
        'Cd',
        'Sn', 
        'Sb', 
        'Cs', 
        'Ba', 
        'Tl', 
        'Pb', 
        'U', 
        'F', 
        'Cl',
        'NO$_2$',
        'Br',
        'NO$_3$',
        'SO$_4$',
        'S$_2$O$_3$',
        'Formate',
        'DOC',
        'PO$_4$-P',
        'NH$_4$-N',
        'Fe${2+}$',
        'S${2-}$',
        'Percent Error',
        'Calcite (Si)\n$\\regular^{CaCO_3}$',
        'Siderite (Si)\n$\\regular^{FeCO_3}$',
        'Gibbsite (Si)\n$\\regular^{Al(OH)_3}$',
        'Alunite (Si)\n$\\regular^{KAl_3(SO_4)_2(OH)_6}$',
        'Gypsum (Si)\n$\\regular^{CaSO_4\u20227H_2O}$',
        'Anglesite (Si)\n$\\regular^{PbSO_4}$',
        'Jarosite (Si)\n$\\regular^{KFe_3(SO_4)_2(OH)_6}$',
        'Melanterite (Si)\n$\\regular^{FeSO_4\u20227H_2O}$',
        'Epsomite (Si)\n$\\regular^{MgSO_4\u20227H_2O}$'
        ]

i=0
for i in range(len(headers)):
    titledict[headers[i]]=titles[i]
    i += 1

