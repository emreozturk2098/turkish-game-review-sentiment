# Graduate project, contribution and method
## Setting
CS549 Natural Language Processing, Özyeğin University, during Emre Öztürk's master's studies. Team: Emre Öztürk, Ali Baki Türköz and Demba Sow.

## Contribution, from slide 2
Emre and Ali Baki are lead contributors for literature review and paper writing. All three contributed annotation. Emre and Ali Baki contributed feature-based labeling and filtering code. Demba is the lead coding contributor, including scraping, training/testing, labeling and filtering. Emre's portfolio must preserve this distinction rather than attribute the complete model training to him.

## Task and data
A review can praise graphics and criticize NPC behavior in the same sentence. The study separates graphics, artificial intelligence and gameplay sentiment, alongside overall sentiment. The presentation reports approximately 2,100 Turkish Steam reviews from 35 games and manual labeling by three researchers. These are reported counts, not counts independently reconstructed from a complete corpus here.

## Team method described in slides
Whitespace/artifact cleanup, Turkish language filtering with langdetect, and morphological preprocessing using Zemberek are described. Slang and profanity were retained for emotional content. The team compared Turkish BERT general sentiment classification with unigram TF-IDF (2,000 features) and MultiOutputClassifier/logistic regression for aspect labels. The original model-training implementation is not supplied in this portfolio.

## Evidence and limits
The presentation uses three main aspects in its explanation, while the n-gram figure contains additional aspects. The exact final schema/split must be resolved from the team's training repository before treating this as a reproduced experiment. Neutral-heavy labels, sarcasm, mixed sentiment, keyword ambiguity and generalization are important limits. The presentation is a course deliverable; publication or deployment is not established.

## Sharing
The three synthetic annotation examples remain clearly labeled. Original supplied review/annotation workbook variants, Word documents and complete recovered labeling/filtering scripts are now archived separately. A complete original BERT training pipeline is not recovered. Existing organization reference: https://github.com/orgs/CS549-NLP-Project-TUR-01/repositories . A particular upstream repository and license are not independently verified here. This academic repository is public; sharing of the school materials was authorized by Emre.
