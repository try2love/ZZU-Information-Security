# -*- coding: cp936 -*-
#���������Ƿ���ɫ����û�ɹ�
for seg in Segments():
    for head in Heads(seg,SegEnd(seg)):
        if isCode(GetFlags(head)):
            SetColor(head,CIC_ITEM,0xffffff)
