import re
import sign
list=['good morning','hello','how are you','hey','hie']
l={'good morning' : 'goodmorning',
   'hello':'hello','hey':'hello','hie':'hello','thank':'thanku','thanks':'thanku',
   'how are you':'greetings','bye':'bye','bathroom':'bathroom',
   'i see':'oic','it':'it',
   'call':'call','phone':'call','telephone':'call',
   ' i':'i',' me':'i','them':'they','they':'they','our':'our',
   'run':'run','engineer':'engineer','some':'some',
   'food':'food','lunch':'food','water':'water',
   'i don\'t know':'idk','i do not know':'idk','i know':'ik',
   'like':'ilikeit','don\'t like':'idontlikeit',
   'sick':'sick','sick':'ill','headache':'headache',
   'may':'mayi','can':'mayi','should':'mayi',
   'want':'iwant','need':'need',
   'are you ok':'ruok','are you fine':'ruok','are you alright':'ruok',
   'orange':'color','pink':'color','purple':'color','red':'color','white':'color','yellow':'color',
   'love':'emotion','faith':'emotion','trust':'emotion','belief':'emotion','believe':'emotion',
   'classroom':'wherestheclassroom','what for lunch':'whatforlunch',
   'what':'whqts','how':'whqts','where':'whqts','when':'whqts',
   }
def a(str):
    say=[]
    for i in l:
        match = re.search(i,str,re.M|re.I)
        if(match):
            say=say+[l[match.group()]]
    if(len(say)):
        print("gif to print")
        for i in say:
            sign.attach(i+'.gif')
    else:
        print("cant load")
        
    
