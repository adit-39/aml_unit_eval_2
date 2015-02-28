# aml_unit_eval_2
Usage of HMMs in speech related applications

## Part 1:
Quality of Speech:
  *Usage* : python speech_quality.py
  *Requirements* : The training and test files in the format c<num>_trng_vq.txt and c<num>_test_vq.txt
  *Output*: Output files of predicted values at various time values corresponding to the input along with Quality index and number of occurrences on terminal

## Part 2:
Separation of Conversation Participants:
  *Usage* : python speech_classification.py > output
  *Requirements* : The training and test files in the format participant_trng_vq.txt and c<num>_test_vq.txt (a_*.txt was changed)
  *Output*: The output file with a split up of who speaks in the conversation at a particular second
