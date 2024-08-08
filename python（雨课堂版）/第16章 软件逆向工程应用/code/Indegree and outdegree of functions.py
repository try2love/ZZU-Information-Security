# -*- coding: cp936 -*-
#��һ���汾
##from sets import Set
##ea=ScreenEA()
##callers=dict()
##callees=dict()
##for function_ea in Functions(SegStart(ea),SegEnd(ea)):#������ǰ���еĺ���
##    f_name=GetFunctionName(function_ea)#��ȡ��������
##    callers[f_name]=Set(map(GetFunctionName,CodeRefsTo(function_ea,0)))#���øú��������к���
##    for ref_ea in CodeRefsTo(function_ea,0):#�������øú��������к���
##        caller_name=GetFunctionName(ref_ea);
##        callees[caller_name]=callees.get(caller_name,Set())
##        callees[caller_name].add(f_name)#
##functions=Set(callees.keys()+callers.keys())
##for f in functions:
##    print '%-4d::%s::%4d'%(len(callers.get(f,[])),f,len(callees.get(f,[])))

#�ڶ����汾����ʱ��������
from sets import Set
ea=ScreenEA()
callers=dict()
callees=dict()

for function_ea in Functions(SegStart(ea),SegEnd(ea)):
    f_name=GetFunctionName(function_ea)
    callers[f_name]=Set(map(GetFunctionName,CodeRefsTo(function_ea,0)))
    callees[f_name]=Set(map(GetFunctionName,CodeRefsFrom(function_ea,0)))
    
functions=Set(callees.keys()+callers.keys())
for f in functions:
    print '%d:::%s:::%d'%(len(callers.get(f,[])),f,len(callees.get(f,[])))

