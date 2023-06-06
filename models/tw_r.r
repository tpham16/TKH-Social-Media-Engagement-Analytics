library(glmnet)

df <- read.csv('data/tweets.csv')

str(df)
print(summary(df$Likes))
print(summary(df$Comments))
print(summary(df$Retweets))

hist(df$Likes)
hist(df$Comments)
hist(df$Retweets)

index <- sample(1:nrow(df), 0.8*nrow(df))

train <- df[index,]
test <- df[-index,]

x_train <- subset(train, select=c(Comments, Retweets))
y_train <- train$Likes

x_test <- subset(test, select=c(Comments, Retweets))
y_test <- test$Likes

lambdas <- 10^seq(2, -3, by = -.1)

lasso_reg <- cv.glmnet(as.matrix(x_train), y_train, alpha = 1, lambda = lambdas, standardize = TRUE)

coefficients <- coef(lasso_reg$glmnet.fit)
print(coefficients)

# levels of significance 

print(summary(lm(Likes~Comments + Retweets, data=train)))