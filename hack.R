suppressMessages(library(dplyr))
suppressMessages(library(caret))
suppressMessages(library(rpart.plot))
suppressMessages(library(rpart))
#suppressMessages(library(rattle))
suppressMessages(library(randomForest))
d<-read.csv("C:\\Users\\hp\\Desktop\\Hack\\Soil types - Sheet1.csv",header = T)
id<-sample(2,nrow(d),replace = T,prob=c(0.75,0.25))
set.seed(1234)
train<-d[id==1,]
test1<-d[id==2,]
test<-test1[,-6]
modfit.rpart<-rpart(Crop~.,data=train,method = "class",xval=24)
print(modfit.rpart,digits = 23)
prediction<-predict(modfit.rpart,test,type = "class")
