        
from Pyfhel import PyCtxt,Pyfhel,PyPtxt
import numpy as np

HE=Pyfhel()
HE.contextGen(scheme='bfv',n=2**14,t_bits=20)
HE.keyGen()

integer1=np.array([11],dtype=np.int64)
integer2=np.array([5],dtype=np.int64)

ctxt1=HE.encryptInt(integer1)
ctxt2=HE.encryptInt(integer2)

print(ctxt1)
print(ctxt2)

ctxt_sum=ctxt1*ctxt2

result=HE.decryptInt(ctxt_sum)
print(result)













