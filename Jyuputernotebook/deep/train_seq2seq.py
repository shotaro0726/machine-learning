import sys
sys.path.append('..')
import numpy as np
import matplotlib.pyplot as plt  
from dataset import sequence
from common.optimizer import Adam
from common.trainer import Trainer
from common.util import eval_seq2seq
from seq2seq import Seq2seq
from peeky_seq2seq import PeekySeq2seq

(x_train,t_train),(x_test,t_test) = sequence.load_data('addition.txt')
x_train,x_test = x_train[:,::-1], x_test[:,::-1]
char_to_id, id_to_char = sequence.get_vocab()

vocab_size = len(char_to_id)
wordvec_size = 16
hidden_size = 128
batch_size = 128
max_epoch = 25
max_grad = 5.0

model = Seq2seq(vocab_size, wordvec_size, hidden_size)
optimizer = Adam()
trainer = Trainer(model, optimizer)

acc_list = []
for epoch in range(max_epoch):
    trainer.fit(x_train,t_train,max_epoch=1,batch_size=batch_size,max_grad=max_grad)
    corrent_num = 0
    
    for i in range(len(x_test)):
        question, corrent = x_test[[i]], t_test[[i]]
        verbose = i < 10
        corrent_num += eval_seq2seq(model,question,corrent,id_to_char,verbose)
    
    acc = float(corrent_num) / len(x_test)
    acc_list.append(acc)
    print('val acc %.3f%' % (acc * 100)) 
    # plt.plot(acc * 100)
    # plt.show()