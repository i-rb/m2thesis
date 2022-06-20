import numpy as np
from scipy.optimize import minimize

print("For functions from M2 thesis: Be careful while interpreting one specific result. Numerical solutions are quite unestable.")

# Attention Case

def SB(theta_H=0.8,theta_L=0.2,nH=70,nL=30,mu=0.4, ret=False, pr=True):
    N=nH+nL
    def objective(x):
        return -(nL*(x[0] +(N-1)*(x[0]*x[2])**mu - theta_L*x[2]) + nH*(x[1] + (N-1)*(x[1]*x[3])**mu - theta_H*x[3]))
    def ICL(x):
        return x[0]-theta_L*x[2] - x[1] + theta_L*x[3]
    def ICH(x):
        return x[1]-theta_H*x[3] - x[0] + theta_H*x[2] # !!!
    def IRL(x):
        return x[0]-theta_L*x[2]  
    def IRH(x):
        return x[1]-theta_H*x[3]  # !!!
    def FEA(x):
        return 1 - nL*x[0]- nH*x[1]
    irl = {'type': 'ineq', 'fun': IRL} 
    irh = {'type': 'ineq', 'fun': IRH}  
    icl = {'type': 'ineq', 'fun': ICL}  
    ich = {'type': 'ineq', 'fun': ICH}  
    fea = {'type': 'eq', 'fun': FEA} 

    # initial guesses

    x0 = np.zeros(4)
    x0[0]=0.5
    x0[1]=0.5
    x0[2]=0.5
    x0[3]=0.5

    b = (0.0,10.0)
    bnds = (b, b, b, b)
    cons = ([irh,icl,fea])

    solution = minimize(objective,x0,method='SLSQP',bounds = bnds, constraints=cons)
    utility = -solution["fun"]
    suc = solution["success"]

    A_L = solution["x"][0]
    A_H = solution["x"][1]
    q_L = solution["x"][2]
    q_H = solution["x"][3]

    if pr:
        print("Utility:               "+str(utility))
        print(" ")
        print("Attention Low Cost :    "+str(round(nL*A_L,6))+"   ("+str(round(A_L,6))+" per user)")
        print("Attention High Cost:    "+str(round(nH*A_H,6))+"   ("+str(round(A_H,6))+" per user)")
        print("Quality Low Cost   :    "+str(round(q_L,6)))
        print("Quality High Cost  :    "+str(round(q_H,6)))
    
    if ret==True:
        return [utility,[A_H,A_L,A_H*nH,A_L*nL,q_H,q_L],suc]
    


def FB(theta_H=0.8,theta_L=0.2,nH=70,nL=30,mu=0.4, ret=False, pr=True):
    N=nH+nL
    def objective(x):
        return -(nL*(x[0] +(N-1)*(x[0]*x[2])**mu - theta_L*x[2]) + nH*(x[1] + (N-1)*(x[1]*x[3])**mu - theta_H*x[3]))
    def ICL(x):
        return x[0]-theta_L*x[2] - x[1] + theta_L*x[3]
    def ICH(x):
        return x[1]-theta_H*x[3] - x[0] + theta_H*x[2] # !!!
    def IRL(x):
        return x[0]-theta_L*x[2]  
    def IRH(x):
        return x[1]-theta_H*x[3]  # !!!
    def FEA(x):
        return 1 - nL*x[0]- nH*x[1]
    irl = {'type': 'ineq', 'fun': IRL} 
    irh = {'type': 'ineq', 'fun': IRH}  
    icl = {'type': 'ineq', 'fun': ICL}  
    ich = {'type': 'ineq', 'fun': ICH}  
    fea = {'type': 'eq', 'fun': FEA} 

    # initial guesses

    x0 = np.zeros(4)
    x0[0]=0.5
    x0[1]=0.5
    x0[2]=0.5
    x0[3]=0.5

    b = (0.0,10.0)
    bnds = (b, b, b, b)
    cons = ([irh,irl,fea])

    solution = minimize(objective,x0,method='SLSQP',bounds = bnds, constraints=cons)
    utility = -solution["fun"]
    suc = solution["success"]

    A_L = solution["x"][0]
    A_H = solution["x"][1]
    q_L = solution["x"][2]
    q_H = solution["x"][3]

    if pr:
        print("Utility:               "+str(utility))
        print(" ")
        print("Attention Low Cost :    "+str(round(nL*A_L,6))+"   ("+str(round(A_L,6))+" per user)")
        print("Attention High Cost:    "+str(round(nH*A_H,6))+"   ("+str(round(A_H,6))+" per user)")
        print("Quality Low Cost   :    "+str(round(q_L,6)))
        print("Quality High Cost  :    "+str(round(q_H,6)))
    
    if ret==True:
        return [utility,[A_H,A_L,A_H*nH,A_L*nL,q_H,q_L],suc]
    
    
## QUALITY CASE

def SB2(theta_H=0.8,theta_L=0.2,nH=70,nL=30,mu=0.3, ret=False, pr=True):
    N=nH+nL
    def objective(x):
        return -(nL*(x[0] +(N-1)*(x[2])**mu - theta_L*x[2]) + nH*(x[1] + (N-1)*(x[3])**mu - theta_H*x[3]))
    def ICL(x):
        return x[0]-theta_L*x[2] - x[1] + theta_L*x[3]
    def ICH(x):
        return x[1]-theta_H*x[3] - x[0] + theta_H*x[2] # !!!
    def IRL(x):
        return x[0]-theta_L*x[2]  
    def IRH(x):
        return x[1]-theta_H*x[3]  # !!!
    def FEA(x):
        return 1 - nL*x[0]- nH*x[1]
    irl = {'type': 'ineq', 'fun': IRL} 
    irh = {'type': 'ineq', 'fun': IRH}  
    icl = {'type': 'ineq', 'fun': ICL}  
    ich = {'type': 'ineq', 'fun': ICH}  
    fea = {'type': 'eq', 'fun': FEA} 

    # initial guesses

    x0 = np.zeros(4)
    x0[0]=0.5
    x0[1]=0.5
    x0[2]=0.5
    x0[3]=0.5

    b = (0.0,10.0)
    bnds = (b, b, b, b)
    cons = ([irh,icl,fea])

    solution = minimize(objective,x0,method='SLSQP',bounds = bnds, constraints=cons)
    utility = -solution["fun"]
    suc = solution["success"]

    A_L = solution["x"][0]
    A_H = solution["x"][1]
    q_L = solution["x"][2]
    q_H = solution["x"][3]

    if pr:
        print("Utility:               "+str(utility))
        print(" ")
        print("Attention Low Cost :    "+str(round(nL*A_L,6))+"   ("+str(round(A_L,6))+" per user)")
        print("Attention High Cost:    "+str(round(nH*A_H,6))+"   ("+str(round(A_H,6))+" per user)")
        print("Quality Low Cost   :    "+str(round(q_L,6)))
        print("Quality High Cost  :    "+str(round(q_H,6)))
    
    if ret==True:
        return [utility,[A_H,A_L,A_H*nH,A_L*nL,q_H,q_L],suc]
    


def FB2(theta_H=0.8,theta_L=0.2,nH=70,nL=30,mu=0.3, ret=False, pr=True):
    N=nH+nL
    def objective(x):
        return -(nL*(x[0] +(N-1)*(x[2])**mu - theta_L*x[2]) + nH*(x[1] + (N-1)*(x[3])**mu - theta_H*x[3]))
    def ICL(x):
        return x[0]-theta_L*x[2] - x[1] + theta_L*x[3]
    def ICH(x):
        return x[1]-theta_H*x[3] - x[0] + theta_H*x[2] # !!!
    def IRL(x):
        return x[0]-theta_L*x[2]  
    def IRH(x):
        return x[1]-theta_H*x[3]  # !!!
    def FEA(x):
        return 1 - nL*x[0]- nH*x[1]
    irl = {'type': 'ineq', 'fun': IRL} 
    irh = {'type': 'ineq', 'fun': IRH}  
    icl = {'type': 'ineq', 'fun': ICL}  
    ich = {'type': 'ineq', 'fun': ICH}  
    fea = {'type': 'eq', 'fun': FEA} 

    # initial guesses

    x0 = np.zeros(4)
    x0[0]=0.5
    x0[1]=0.5
    x0[2]=0.5
    x0[3]=0.5

    b = (0.0,10.0)
    bnds = (b, b, b, b)
    cons = ([irh,irl,fea])

    solution = minimize(objective,x0,method='SLSQP',bounds = bnds, constraints=cons)
    utility = -solution["fun"]
    suc = solution["success"]

    A_L = solution["x"][0]
    A_H = solution["x"][1]
    q_L = solution["x"][2]
    q_H = solution["x"][3]

    if pr:
        print("Utility:               "+str(utility))
        print(" ")
        print("Attention Low Cost :    "+str(round(nL*A_L,6))+"   ("+str(round(A_L,6))+" per user)")
        print("Attention High Cost:    "+str(round(nH*A_H,6))+"   ("+str(round(A_H,6))+" per user)")
        print("Quality Low Cost   :    "+str(round(q_L,6)))
        print("Quality High Cost  :    "+str(round(q_H,6)))
    
    if ret==True:
        return [utility,[A_H,A_L,A_H*nH,A_L*nL,q_H,q_L],suc]
    
    
    
    

def SB_ads(b_ad=1, theta_H=0.8,theta_L=0.2,nH=70,nL=30,mu=0.4, ret=False, pr=True):
    N=nH+nL
    def objective(x):
        return -b_ad*x[4]*(nL*((N-1)*(x[0]*x[2])**mu) + nH*((N-1)*(x[1]*x[3])**mu))
    def ICL(x):
        return x[0]-theta_L*x[2] - x[1] + theta_L*x[3]
    def ICH(x):
        return x[1]-theta_H*x[3] - x[0] + theta_H*x[2] 
    def IRL(x):
        return x[0]-theta_L*x[2]  
    def IRH(x):
        return x[1]-theta_H*x[3] 
    def FEA(x):
        return 1 - nL*x[0]- nH*x[1] - x[4]
    irl = {'type': 'ineq', 'fun': IRL} 
    irh = {'type': 'eq', 'fun': IRH}  
    icl = {'type': 'eq', 'fun': ICL}  
    ich = {'type': 'ineq', 'fun': ICH}  
    fea = {'type': 'eq', 'fun': FEA} 

    # initial guesses

    x0 = np.zeros(5)
    x0[0]=0.4
    x0[1]=0.2
    x0[2]=0.4
    x0[3]=0.35
    x0[4]=0.3

    b = (0.0,10.0)
    bnds = (b, b, b, b, b)
    cons = ([irh,icl,fea])

    solution = minimize(objective,x0,method='SLSQP',bounds = bnds, constraints=cons)
    utility = -solution["fun"]
    suc = solution["success"]

    A_L = solution["x"][0]
    A_H = solution["x"][1]
    q_L = solution["x"][2]
    q_H = solution["x"][3]
    A_a = solution["x"][4]

    if pr:
        print("Utility:               "+str(utility))
        print(" ")
        print("Attention ADS      :    "+str(round(A_a,6)))
        print("Attention Low Cost :    "+str(round(nL*A_L,6))+"   ("+str(round(A_L,6))+" per user)")
        print("Attention High Cost:    "+str(round(nH*A_H,6))+"   ("+str(round(A_H,6))+" per user)")
        print("Quality Low Cost   :    "+str(round(q_L,6)))
        print("Quality High Cost  :    "+str(round(q_H,6)))
    
    if ret==True:
        return [utility,[A_H,A_L,A_H*nH,A_L*nL,q_H,q_L, A_a],suc]



def FB_ads(b_ad=1, theta_H=0.8,theta_L=0.2,nH=70,nL=30,mu=0.4, ret=False, pr=True):
    N=nH+nL
    def objective(x):
        return -b_ad*x[4]*(nL*((N-1)*(x[0]*x[2])**mu) + nH*((N-1)*(x[1]*x[3])**mu))
    def ICL(x):
        return x[0]-theta_L*x[2] - x[1] + theta_L*x[3]
    def ICH(x):
        return x[1]-theta_H*x[3] - x[0] + theta_H*x[2] # !!!
    def IRL(x):
        return x[0]-theta_L*x[2]  
    def IRH(x):
        return x[1]-theta_H*x[3]  # !!!
    def FEA(x):
        return 1 - nL*x[0]- nH*x[1] - x[4]
    irl = {'type': 'eq', 'fun': IRL} 
    irh = {'type': 'eq', 'fun': IRH}  
    icl = {'type': 'ineq', 'fun': ICL}  
    ich = {'type': 'ineq', 'fun': ICH}  
    fea = {'type': 'eq', 'fun': FEA} 

    # initial guesses

    x0 = np.zeros(5)
    x0[0]=0.0015
    x0[1]=0.01
    x0[2]=0.02
    x0[3]=0.03
    x0[4]=0.7

    b = (0.0,10.0)
    bnds = (b, b, b, b, b)
    cons = ([irh,irl,fea])

    solution = minimize(objective,x0,method='SLSQP',bounds = bnds, constraints=cons)
    utility = -solution["fun"]
    suc = solution["success"]

    A_L = solution["x"][0]
    A_H = solution["x"][1]
    q_L = solution["x"][2]
    q_H = solution["x"][3]
    A_a = solution["x"][4]

    if pr:
        print("Utility:               "+str(utility))
        print(" ")
        print("Attention ADS      :    "+str(round(A_a,6)))
        print("Attention Low Cost :    "+str(round(nL*A_L,6))+"   ("+str(round(A_L,6))+" per user)")
        print("Attention High Cost:    "+str(round(nH*A_H,6))+"   ("+str(round(A_H,6))+" per user)")
        print("Quality Low Cost   :    "+str(round(q_L,6)))
        print("Quality High Cost  :    "+str(round(q_H,6)))
    
    if ret==True:
        return [utility,[A_H,A_L,A_H*nH,A_L*nL,q_H,q_L,A_a],suc]