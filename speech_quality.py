""" STEPS TO COMPLETE:
* a) Train HMMs:
*       Instantiate a HMM for each type of training data(one with silent, one
*       with single, one with multi)
* b) Test HMMs:
*       Take vectors of size 10 and predict an output based on which machine
*       gives higher probability for the sequence using forward algo (Eval prob)
* c) Check with the audio:
*       Listen to audio and see if predicted outputs were correct
*
"""

from myhmm_log import MyHmmLog

def read_file(name):
	"""
	Function to take in a training or test file and compose a list of 10-member
	sequences for use later
	"""
	with open(name) as f:
		model=f.readlines()

	s=[]
	sequences=[]
	i=0;

	for word in model:
		i+=1
		word=word[:-1]
		s.append(word)
		if i %10 == 0 or i == (len(model)-1):
			sequences.append(s)
			s=[]

	return sequences


def train_machine(data,init_model_file):
    """
    Function to take in training data as a list of 10-member lists along with an
    initial model file and output a HMM machine trained with that data.
    """
    M = MyHmmLog(init_model_file)
    M.forward_backward_multi(data)

    return(M)

def test(output_seq,M1,M2,M3,obs_file):
    """
    Function to take in the test observation sequence and output "silent",
    "single" or "multi" based on which of the three machines gives the highest
    probability in the evaluation problem for that output sequence
    """
    predicted = []
    sil_c = 0
    sin_c = 0
    mul_c = 0
    for obs in output_seq:
        p1 = M1.forward(obs)
        p2 = M2.forward(obs)
        p3 = M3.forward(obs)
        if(p1 > p2 and p1 > p3):
            predicted.append("silent")
            sil_c+=1
        elif(p2 > p3 and p2 > p1):
            predicted.append("single")
            sin_c+=1
        else:
            predicted.append("multi")
            mul_c+=1

    time = 0.000
    with open("op_"+obs_file,"w") as g:
        for val in predicted:
            g.write(str(time)+" :\t"+val+"\n")
            time+=0.005
    print(obs_file+":")
    d=dict()
    d["silent"]=sil_c
    d["single"]=sin_c
    d["multi"]=mul_c
    print d

    q_index(sil_c,sin_c,mul_c)
    return predicted

def q_index(sil_c,sin_c,mul_c):
	"""
	Function to compute the quality index which is normalized frequency dist
	for the entire output for the file
	Higher quality-index implies more streamlined conversation
	Lower implies more people talking at a time, hence poor conversation quality
	"""
    q = (10*sil_c + 10*sin_c -10*mul_c)/(sil_c + sin_c + mul_c)
    print "Quality Index = ",q
    print("*"*60)


if __name__=="__main__":
    d_silent = read_file("silent_1_trg_vq.txt")
    d_single = read_file("single_1_trg_vq.txt")
    d_multi = read_file("multi_1_trg_vq.txt")
    M1 = train_machine(d_silent,"debate_initial.txt")
    M2 = train_machine(d_single,"debate_initial.txt")
    M3 = train_machine(d_multi,"debate_initial.txt")
    for i in range(1,11):
        obs_file = "c"+str(i)+"_test_vq.txt"
        all_obs = read_file(obs_file)
        pred_seq = test(all_obs,M1,M2,M3,obs_file)
        #print pred_seq
