# Archived course outputs
The CSV transcribes the BERT table embedded in slide 14 of the supplied presentation. Slide 11 describes evaluation on a validation set. It is a team-reported result, not a freshly executed benchmark or proof of an untouched test score.

The training code, split indices, leakage/duplicate audit and checkpoints are not supplied here. The project draft discusses PC-to-console evaluation as an aim; no verified completed cross-platform test output was found, so it is not claimed as an achievement.

The n-gram chart is copied as an image rather than digitized into falsely precise values. High accuracy alongside low macro-F1 in several aspects is consistent with the presentation's neutral-label imbalance discussion. Its `review_id` category is an unresolved reporting issue: the identifier should not be interpreted as a valid sentiment task, and the missing training code prevents verifying how it was handled. BERT overall sentiment and multi-output aspect metrics are different tasks and are not compared as one score ranking.
