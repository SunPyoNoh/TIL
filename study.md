![1569460605965](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1569460605965.png)

![1569460628788](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1569460628788.png)



![1569461021049](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1569461021049.png)





















![1569460481737](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1569460481737.png)



![1569460677695](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1569460677695.png)

---





```R
 aov(대상변수~그룹변수, data=데이터명) # 그룹 변수는 factor 형

########################################

 analysis<-aov(Sepal.Width~Species, data=iris)
 summary(analysis)
#            Df  Sum Sq  Mean Sq F value Pr(>F)    
#Species       2  11.35   5.672   49.16 <2e-16 ***
#Residuals   147  16.96   0.115                   
#---
#Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ #1
```

> iris의 품종(Species) 별로 Sepal.Width 평균은 다르다



```R
bartlett.test(Sepal.Width~Species, data=iris)
 
	Bartlett test of homogeneity of variances
 
data:  Sepal.Width by Species
Bartlett's K-squared = 2.0911, df = 2, p-value = 0.3515
```

