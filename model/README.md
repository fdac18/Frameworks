# Predictive Model
- This is where all code and results pertaining to the predictive model will be stored.

- Example code in R for running topic models, comparing perplexity on two models
- source: https://stackoverflow.com/questions/21355156/topic-models-cross-validation-with-loglikelihood-or-perplexity


install.packages("topicmodels",repos='http://cran.us.r-project.org')
install.packages("doParallel",repos='http://cran.us.r-project.org')
install.packages("ggplot2",repos='http://cran.us.r-project.org')
install.packages("scales",repos='http://cran.us.r-project.org')
library(topicmodels)
library(doParallel)
library(ggplot2)
library(scales)

# Simple validation
data("AssociatedPress", package = "topicmodels")

## set a seed so that the output of the model is predictable
ap_lda <- LDA(AssociatedPress, k = 2, control = list(seed = 1234))
## ap_lda

burnin = 1000
iter = 1000
keep = 50

full_data  <- AssociatedPress
n <- nrow(full_data)
# Using 5-fold cross-validation to determine the number of topics to model (k) 
k <- 5

splitter <- sample(1:n, round(n * 0.75))
train_set <- full_data[splitter, ]
valid_set <- full_data[-splitter, ]

fitted <- LDA(train_set, k = k, method = "Gibbs",
                          control = list(burnin = burnin, iter = iter, keep = keep) )
perplexity(fitted, newdata = train_set) # about 2700
perplexity(fitted, newdata = valid_set) # about 4300

#----------------5-fold cross-validation, different numbers of topics----------------
## set up a cluster for parallel processing
cluster <- makeCluster(detectCores(logical = TRUE) - 1) # leave one CPU spare...
registerDoParallel(cluster) 

## load up the needed R package on all the parallel sessions
clusterEvalQ(cluster, {
   library(topicmodels)
})

folds <- 5
splitfolds <- sample(1:folds, n, replace = TRUE)
candidate_k <- c(2, 3, 4, 5, 10, 20, 30, 40, 50, 75, 100, 200, 300) # candidates for how many topics

## export all the needed R objects to the parallel sessions
clusterExport(cluster, c(“full_data”, “burnin”, “iter”, “keep”, “splitfolds”, “folds”, “candidate_k”))

- we parallelize by the different number of topics.  A processor is allocated a value
- of k, and does the cross-validation serially.  This is because it is assumed there
- are more candidate values of k than there are cross-validation folds, hence it
- will be more efficient to parallelise


system.time({
results <- foreach(j = 1:length(candidate_k), .combine = rbind) %dopar%{
   k <- candidate_k[j]
   results_1k <- matrix(0, nrow = folds, ncol = 2)
   colnames(results_1k) <- c(“k”, “perplexity”)
   for(i in 1:folds){
      train_set <- full_data[splitfolds != i , ]
      valid_set <- full_data[splitfolds == i, ]

      fitted <- LDA(train_set, k = k, method = “Gibbs”,
                    control = list(burnin = burnin, iter = iter, keep = keep) )
      results_1k[i,] <- c(k, perplexity(fitted, newdata = valid_set))
   }
   return(results_1k)
}
})
stopCluster(cluster)

results_df <- as.data.frame(results)

#plot
ggplot(results_df, aes(x = k, y = perplexity)) +
   geom_point() +
   geom_smooth(se = FALSE) +
   ggtitle(“5-fold cross-validation of topic modelling with the 'Associated Press' dataset”,
           “(ie five different models fit for each candidate number of topics)”) +
   labs(x = “Candidate number of topics”, y = "Perplexity when fitting the trained model to the hold-out set")
