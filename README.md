# aml_unit_eval_2
Usage of HMMs in speech related applications

## Part 1: <br>
Quality of Speech: <br>
  *Usage* : python speech_quality.py  <br>
  *Requirements* : The training and test files in the format c<num>_trng_vq.txt and c<num>_test_vq.txt <br>
  *Output*: Output files of predicted values at various time values corresponding to the input along with Quality  index and number of occurrences on terminal <br>

## Part 2: <br>
Separation of Conversation Participants: <br>
  *Usage* : python speech_classification.py > output <br>
  *Requirements* : The training and test files in the format participant_trng_vq.txt and c<num>_test_vq.txt <br> a_test.txt was changed <br>
  *Output*: The output file with a split up of who speaks in the conversation at a particular second <br>
