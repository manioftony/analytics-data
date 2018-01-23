import pandas as pd
old=pd.read_csv("/home/mani/Documents/result/csv/sushruta/totalimage.csv")
new=pd.read_csv("/home/mani/Documents/result/csv/sushrutanew/eyepacs/dr_onehot.csv")
print 'sushruta',old[old.mild==1].shape[0]
print 'sushruta',old[old.moderate==1].shape[0]
print 'sushruta',old[old.severe==1].shape[0]
print 'sushruta',old[old.proliferate==1].shape[0]

print "           "
print "           "
print "           "
print "           "

print 'sushruta-new',new[new.mild==1].shape[0]
print 'sushruta-new',new[new.moderate==1].shape[0]
print 'sushruta-new',new[new.severe==1].shape[0]
print 'sushruta-new',new[new.proliferate==1].shape[0]

