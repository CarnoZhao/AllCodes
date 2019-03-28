library(e1071)
library(rpart)
library(ROCR)

data = read.csv('../Data/BreastCancer.csv')
# Age BMI Glucose Insulin HOMA Leptin Adiponectin Resistin MCP.1 Classification
# 116 * 10
# Classification = 1 or 2
# data = data[sample(1:nrow(data)),]
data$Classification = ifelse(data$Classification == 1, 0, 1)
# print(head(data))
fit.glm = glm(Classification ~ ., data, family = binomial)
fit.svm = svm(Classification ~ ., data, kernel = 'linear')
fit.tree = rpart(Classification ~ ., data, method = 'class')

esti.glm = ifelse(fitted(fit.glm) > 0.5, 1, 0)
esti.svm = ifelse(fitted(fit.svm) > 0, 1, 0)
esti.tree = ifelse(predict(fit.tree, value = "prob")[,2] > 0.5, 1, 0)

err.rate.glm = sum(esti.glm != data$Classification) / length(data$Classification)
err.rate.svm = sum(esti.svm != data$Classification) / length(data$Classification)
err.rate.tree = sum(esti.tree != data$Classification) / length(data$Classification)

result = prediction(fitted(fit.glm), data$Classification)
perf = performance(result, measure = 'tpr', x.measure = 'fpr')
plot(perf, col = 'red')

result = prediction(fitted(fit.svm), data$Classification)
perf = performance(result, measure = 'tpr', x.measure = 'fpr')
plot(perf, add = TRUE, col = 'blue')

result = prediction(predict(fit.tree, value = "prob")[,2], data$Classification)
perf = performance(result, measure = 'tpr', x.measure = 'fpr')
plot(perf, add = TRUE, col = 'green')