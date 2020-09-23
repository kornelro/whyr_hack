library(readr)
content <- read_csv('data/content.csv')
write_csv(content[, 1:2], 'data/content-clean.csv')
