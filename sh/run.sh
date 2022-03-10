#!/bin/zsh

# make training list
data=/Users/riedhammerko/git/seqlrn/3-hmm/res/recordings
/bin/ls $data > list.all
cat list.all | grep -v  '^[0-9]_.\+_4[5-9].wav' > list.test
cat list.all | grep  '^[0-9]_.\+_4[5-9].wav' > list.train

# compute mfcc
mkdir ft
jstk app.Mfcc --in-list list.all ft/ --dir $data -f t:wav/8 -w hamm,25,10 -b 0,4000,-1,.5 --turn-wise-mvn

# init cb
jstk app.Initializer --gmm cb.init -n 128 -s sequential_5 --list list.train --dir ft/
jstk app.GaussEM -i cb.init -o cb.em10 -p 8 -l list.train  -d ft/ -n 10
jstk arch.Configuration --compile phones words --semi cb.em10 --write conf.xml cb.0

# transcriptions
for i in train test; do
	awk -v a='zero,one,two,three,four,five,six,seven,eight,nine' -F_ '{ split(a,m,","); print $0, m[$1+1] }' list.$i > list.$i.trl
done

# train
jstk app.Trainer conf.xml cb.0 cb.1 list.train.trl ft/ -a linear -t vt -p 8

for i in `seq 2 6`; do
	j=`expr $i - 1`
	jstk app.Trainer conf.xml cb.$j cb.$i list.train.trl ft/ -a forced -t vt -p 8
done

# test
i=6
jstk app.IWRecognizer conf.xml cb.$i sil -l list.test ft/ out.$i -p 8 -n 1
jstk app.Decoder conf.xml cb.$i -l list.test ft/ -bs 1000 -bw 15 -i 0.01 -w 0.01 -q -o outd.$i
paste list.test outd.6| less

# evaluate
./eval.py out.6
./eval.py <(paste list.test outd.6)