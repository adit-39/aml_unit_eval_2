"""
MODI and ARNAB CONVERSATION:
Training is similiar to the method in Part 1
Instead of computing the q-index, we are finding the most occurrences in 20
(which denotes a second's worth of data) and declaring that state as the state
of the HMM (which is in Arnab, Modi and Other)

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
    mus_c = 0
    mod_c = 0
    arn_c = 0
    next = 0
    t = 0.000
    d=dict()
    d["other"]=0
    d["modi"]=0
    d["arnab"]=0
    print(obs_file+":")
    for obs in output_seq:
        p1 = M1.forward(obs)
        p2 = M2.forward(obs)
        p3 = M3.forward(obs)


        if(p1 > p2 and p1 > p3):
            predicted.append("Other")
            mus_c+=1
            d["other"]+=1
        elif(p2 > p3 and p2 > p1):
            predicted.append("Modi")
            mod_c+=1
            d["modi"]+=1
        else:
            predicted.append("Arnab")
            arn_c+=1
            d["arnab"]+=1
        t+=0.05
        next+=1

        if(next % 20 == 0):
            p_other = d["other"]/20.0
            p_modi = d["modi"]/20.0
            p_arnab = d["arnab"]/20.0
            #print("{0} : Modi = {1}, Arnab = {2}, Other = {3}".format(t,p_modi,p_arnab,p_other))
            if p_other>p_modi and p_other>p_arnab:
                print "{0} : Speech : Other".format(t)
            elif p_modi>p_other and p_modi>p_arnab:
                print "{0} : Speech : Modi".format(t)
            else:
                 print "{0} : Speech : Arnab".format(t)
            d["other"]=0
            d["modi"]=0
            d["arnab"]=0

    time = 0.000
    with open("op_"+obs_file,"w") as g:
        for val in predicted:
            g.write(str(time)+" :\t"+val+"\n")
            time+=0.005

    return predicted

if __name__=="__main__":
    d_music = read_file("music_1_trg_vq.txt")
    d_modi = read_file("modi_1_trg_vq.txt")
    d_arnab = read_file("arnab_1_trg_vq.txt")
    M1 = train_machine(d_music,"debate_initial.txt")
    M2 = train_machine(d_modi,"debate_initial.txt")
    M3 = train_machine(d_arnab,"debate_initial.txt")
    for i in range(6,10):
        obs_file = "c"+str(i)+"_test_vq.txt"
        all_obs = read_file(obs_file)
        pred_seq = test(all_obs,M1,M2,M3,obs_file)
        #print pred_seq
