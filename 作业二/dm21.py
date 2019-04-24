# coding = utf-8
import random

import numpy as np
import pandas as pd
import math
import csv
import matplotlib.pyplot as plt


def ziji(items,k):
    sub_list_all = []
    N = len(items)
    for i in range(2 ** N):
        combo = []
        for j in range(N):
            # test jth bit of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        if(len(combo)==k):
            sub_list_all.append(combo)
    return sub_list_all


def pan(d):
    sum=0
    das=set(d)
    for i in data:
        if das.issubset(i):
            sum=sum+1
    return  sum
def C(ck_1,k):
    ta=[]
    for d in ck_1:
        for da in d:
            if da not in ta:
                ta.append(da)
    #print (ta)
    ck=ziji(ta,k)
    ck2=[]
    #print(ck)
    for s in ck:
        if(pan(s)/total>=sup):
            ck2.append(s)
            #print(s,"sup:",pan(s)/total)
            frequently[frozenset(s)]=pan(s)/total
            frequently1.append(s)
    return  ck2



def jian(ck,ck_1,k):

    ck3=[]
    flag=0
    for i in ck:
        ck2 = ziji(i, k - 1)
        for j in ck2:
            if j not in ck_1:
                flag=1
        if flag==0:
            ck3.append(i)
    return  ck3


def rule(ck):

    ziji1=[]
    len1=len(ck)
    if(len1<=1):
        return 0
    b = frequently[frozenset(ck)]
    #print("ck", ck)
    #print("b", b)
    for i in range(1<<len1):
        if (i >= 1) & (i < len1):
            ziji1=ziji1+ziji(ck,i)
    fail=[]
    #print("ziji1",ziji1)
    for ck2 in ziji1:
        flag=0
        for j in fail:
            if(j.issubset(ck2)):
                flag=1
        if(flag==0):
            ck1=frozenset(ck)-frozenset(ck2)
            #print("ck1",ck1)
            #print("ck2",ck2)
            for i in frequently:
                if (i == ck1):
                    a = frequently[i]
                    #print("a",a)
                if (i==frozenset(ck2)):
                    c=frequently[i]
            con1 = b / a
            d=b / c
            cosine=math.sqrt(d*con1)
            l=con1/c

            if (con1 >= con):
                print(ck1, "-->", ck2, "=", con1)
                print("lift:",l)
                print("cosine:",cosine)
            else:
                #print(ck1, "-->", ck2, "=", con1,"fail")
                fail.append(frozenset(ck2))
            #print("关联规则",ck1,"-->",ck2,"置信度：",con1)
    #print(fail)
    return 0




if __name__ == "__main__":

    list1 = [[]]
    diction = []

    user = 'pitcher_id'
    pre_id = '452657'
    count = 0

    file = csv.reader(open('atbats2.csv','r'))

    for c in file:
        if c[8] == user:
            continue
        id = c[8]
        product = c[2]
        if product == 'Double Play':
            product = 'Double'
        if product == 'Triple Play':
            product = 'Triple'
        if 'Out' in product:
            product = 'Out'
        if 'Interference' in product:
            product = 'Interference'
        if [product] not in diction:
            diction.append([product])
        #开始下一单
        if id != pre_id:
            pre_id = id
            count += 1
            list1.append([product])
        #继续这一单
        else:
            if product not in list1[count]:
                list1[count].append(product)


    print(diction)
    print(list1[0:50])
    
    sup = 0.1
    con = 0.5
    frequently=dict()
    frequently1=[]
    # print(total)
    data=list1
    total = len(data)
    aaa = diction
    aaa1 = C(aaa, 1)
    k=1
    C8=aaa1
    C9=[]
    while(1):
        C7=C9
        k=k+1
        C9=C(C8,k)
        C8=jian(C9,C8,k)
        #print("C9:",k,C9)
        if(len(C9)==0):
            break
    #print (C7)
    print(frequently)
    for i in frequently1:
        rule(i)

    list2 = []
    a = list(frequently.keys())
    for i in a:
        s=""
        for j in i:
            s=s+" "+j
        list2.append(s)
    plt.bar(list2,frequently.values())
    plt.xticks(rotation=80)
    plt.savefig('./d.png')
    plt.show()
