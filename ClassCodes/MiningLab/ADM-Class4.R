#See NaiveBayes.R
n = 200
p.spam = 0.25
p.email = 1 - p.spam

vocabulary = as.character(strsplit(LETTERS, ''))

p.words.spam = runif(length(vocabulary))
p.words.email = ifelse(p.words.spam > 0.5, p.words.spam / 2, p.words.spam * 2)
n.words = 20

class = sample(c("spam", "email"), 1, prob = c(p.spam, p.email))
if (class == "spam") {
  words = sample(vocabulary, n.words, replace = TRUE, prob = p.words.spam)
} else {
  words = sample(vocabulary, n.words, replace = TRUE, prob = p.words.email)
}
words