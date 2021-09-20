#!/bin/env Rscript

## Getting the destination pathway

actualPathway <- getwd()

destinationPathway <- file.path(normalizePath(dirname("../output")), "output")

setwd(destinationPathway)

## Reading the dataframe of data

openingFile <- read.csv("CompleteData.csv")

## Creating a function to compute varience of each gene

savingVariances <- function(x){
    return(var(x))
}

## Creating a dataframe of variance of each gene

varianceDataframe <- apply(X = openingFile[, 2:(ncol(openingFile) - 1)], MARGIN  = 2, FUN = savingVariances)

## Reformating the variance gene data in a dataframe R object

varianceDataframe <- as.data.frame(varianceDataframe)

## Sorting gene varience in an descending order

varianceDataframe <- varianceDataframe[order(varianceDataframe, decreasing = TRUE),, drop=FALSE]

## Creating a function to save genes with a varience superior to a threshold

SavingVarienceDataframe <- function(x){
  
  ## Selecting genes with variences superior to a threshold
  
  columnsToSelect <- as.vector(rownames(varianceDataframe[varianceDataframe$varianceDataframe > x,, drop = FALSE]))
  
  ## Subset Dataframe columns with columnsToSelect (columns with genes whose the variance > x)
  
  dataFrameSubset <- subset(openingFile, select = columnsToSelect)
  
  ## Adding labels to the newDataFrame
  
  dataFrameSubset <- cbind(openingFile$X, dataFrameSubset)
  dataFrameSubset <- cbind(dataFrameSubset, openingFile$Labels)
  colnames(dataFrameSubset)[1] <- "X"
  colnames(dataFrameSubset)[ncol(dataFrameSubset)] <- "Labels"
  
  ## Saving dataframes in folder according the thresholds
  
  if (x == 10){
    write.csv(dataFrameSubset, file = "399GenesDataframe/newDataFrame.csv", 
              row.names=FALSE, quote = FALSE)
  }
  
  else{
    write.csv(dataFrameSubset, file = "2264GenesDataframe/newDataFrame.csv", 
              row.names=FALSE, quote = FALSE)
  }
}

## Saving genes with varience superior to threshold

SavingVarienceDataframe(4)
SavingVarienceDataframe(10)
