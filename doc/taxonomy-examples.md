OCR Knowledge Taxonomy Examples
====

This document lists examples for each rule specified in [Knowledge Taxonomy](https://gist.github.com/zifeishan/8661640).

**Notation format in examples:**

    296   6       following     foliovj'Lug  VBG      O |||d,sw

    lineNum WordNum OCR1Output  OCR2Output   NERtag  POS   rulesThatCanFix

Format for *"rules that can fix"*: e.g., "a+b,b+c,e" means EITHER "rule a and b" OR "b and c" OR "e itself" can fix this error.

## Rules to Judge

**[twchar]**: If Tesseract output have letter in {', ?, ", -}, it is wrong


    296   6       following     foliovj'Lug  VBG      O |||d,sw
    297   7           table           table   NN      O 
    298:  8               "                   ''      O |||twchar
    299   9           which         lvhLcll  WDT      O |||d,sw
    

**[cwchar]**: If Cuneiform output have letter in {', :, >}, it is wrong

    231   7              H.              H.  NNP PERSON 
    232   8         WORTHEN         WORTHEN  NNP PERSON 
    233:  9               ,               >    ,      O |||cwchar

     35   1         BRYOZOA         BRYOZQA  NNP      O |||d,sw
     36:  2               *              "'   CD NUMBER |||cwchar
    
**[upp]**: If output has changes from lower case to upper case, then it is wrong

     21:  1             voL             VOL   NN      O |||upp,sw

**[upp]**: If output has a similar proportion of lower-case letters and upper-case letters, then it is wrong

    468:  2      ENToPRocTA      ENTOPROCTA   NN      O |||upp,d,sw

**[charuni]**: A word should only consist of letters, numbers, or special characters. A combination of those should be wrong.

    187   3      downloaded      downloadcd  VBN      O |||d,sw
    188   4            from            from   IN      O 
    189:  5             l44             144   NN      O |||charuni
    190   6             .92             .92   CD NUMBER 
    191   7               .               .    .      O 
    192  
    193:  1             l42             142   NN      O |||charuni
    194   2               .               .    .      O 
    195  
    196:  1             l58             158   NN      O |||charuni
    197   2              on              on   IN      O 
    198   3             Fri             Fri  NNP   TIME 


**[comb]**: Combinability: if combination can generate candidate, current output should be wrong

    249:  1             Dow            3OCI  NNP   MISC |||comb
    250   2         nloaded          IUcdOC  VBD      O |||
    251:  3             fro               O   NN      O |||comb
    252   4               m               E   NN      O |||

    779: 17        backward        back-war   RB      O |||comb,seg
    780  18               ,              d,    ,      O |||


**[url]**: URLs starts with "http" or "www" and can contain rare characters.

    6 http://WWW.bioone.org/doi/full/l0.1671/0272-4634%282000%29020%5B0784%3AMSDTCF htt://www.bioone.or/doi/full/10.1671/0272-4634%282000%29020%580784%3AMSDTCF   JJ PERCEN  |||url$1

    30 www.bioone.org/page/terms www.bioone.or/ae/terms  NNS      O |||url$1


**[dot]**: A dot (.) should not be followed by a lower-case letter

    804: 20               .               ,    .      O |||dot
    805  
    806   1        limiting        limiting  VBG      O 

    156                    this                 this ||
    157                   group                group ||
    158: X                    .                    , ||dot
    159                   among                among ||
    160  X                which               xvhich ||dict

**[upper]**: A general word should be upper-case only if it is in the first word in sentence. (?)

    806  19        syncline        synchne,   NN      O |||d,sw
    807  20               ,                    ,      O 
    808: 21        overlaid        Overlaid  VBN      O |||upper
    809  22              by              by   IN      O 
    810  23               a               a   DT      O 

    499   2           zoids           zoids  NNS      O 
    500   3           arise            arse  VBP      O |||d,sw
    501:  4   Independently   independently   RB      O |||upper
    502   5            from            from   IN      O 
    503   6               a               a   DT      O 

**[statc]**: Rare characters should not appear 

    994: 10               (               {   NN      O |||statc,path
    995  11      incomplete      incom-plet   JJ      O |||d,sw,comb
    996  12               )              e)   NN      O |||

**[statcgram]**: Rare character combinations should not appear

    No example found.

**[sw]**: A word with high frequency is correct
**[sw]**: A word with low frequency is wrong

    754:  5             CO2             COz   NN      O |||sw
    755   6               +               +   CC      O 
    756:  7             H20             H,O   NN      O |||sw

    732:  3            1:15            pls.   CD   TIME |||sw

    764: 12         conicus         conieus   NN      O |||sw

     25:  5             No.             No;   NN      O |||sw

    1134:  1          Calif.          Calif;  NNP LOCATI |||sw

    1249: 10            Dall            Dali  NNP PERSON |||sw

**[swgram]**: A word Ngram with high frequency is correct
**[swgram]**: A word Ngram with low frequency is wrong

    118: 22            1907             %07   CD   DATE |||sw,swgram
    119  23             and             and   CC   DATE 
    120: 24            1908            I908   CD   DATE |||sw,swgram

    569  12            more            more  JJR      O 
    570: 13            than            thin   IN      O |||swgram,pos
    571  14             160             160   CD NUMBER 

    640:  1              de             :dh   IN      O |||swgram
    641   2           Santa           Santa  NNP LOCATI 
    642   3           Marta           Marta  NNP LOCATI 

    523   6            that            that   IN      O 
    524   7     Pedicellina     Pedicellina  NNP PERSON 
    525:  8              is               s  VBZ      O |||swgram
    526   9       sometimes       sometimes   RB      O 

    128  32       belonging      be'longing  VBG      O |||cwchar,charuni
    129: 33              to              Yo   TO      O |||swgram,pos

    240:  5           large            urge   JJ      O |||swgram,pos
    241   6          number          number   NN      O 
    242   7              of              of   IN      O 

    670: 25          bother           other   VB      O |||swgram
    671  26              of              of   IN      O 

**[stats]**: A sentence of high frequency is correct 

**[d]**: A word in dictionary is correct
**[d]**: A word not in dictionary is wrong

    475:  1      Phylogenet      Phyiogenet  NNP      O |||d,sw

     34:  2            ?rst           first   JJ      O |||d,sw,edrule

    108:  5  diversi?cation diversification   NN      O |||d,sw,edrule

    816: 12          lantem         lantern   NN      O |||d,sw,edrule

    137: 13           fonns           forms  NNS      O |||d,sw

    187:  3      downloaded      downloadcd  VBN      O |||d,sw

**[pos]**: If the word have the POS in dictionary then it is correct
**[pos]**: If the word do not have the POS in dictionary then it is wrong
**[pos]**: If word-POS combination is rare in corpus then it is wrong


    570: 13            than            thin   IN      O |||swgram,pos

     38   3           paper           paper   NN      O 
     39:  4              is              18  VBZ      O |||pos
     40:  5           based           based  VBN      O 

    129: 33              to              Yo   TO      O |||swgram,pos

**[posgram]**: if a POS-ngram is rare, then at least one of its words is wrong

**[ner]**: If a word-NER combination is rare then it is wrong

    261   4             May                   MD   DATE 
    262   5               8               C   CD   DATE |||swgram
    263:  6               ,               O    ,   DATE |||ner,swgram
    264:  7            2013            C)CU   CD   DATE |||d,swgram,ner

    725:  6            1982            lpsz   CD   DATE |||ner,sw

    957:  1             411             Sai   CD NUMBER |||ner

    193:  5              13              I3   CD NUMBER |||ner
    194:  6         species         specie8  NNS      O |||d,sw

**[number]**: If a word consist of numbers and dashes, it is a valid number.

**[persondot]**: Person name can come with ".", and this dot does not end a sentence

    364   6              M.              M.  NNP PERSON 
    365   7        Hausdorf        Hausdorf  NNP PERSON 
    366:  8               .               ,    .      O |||persondot

    388   2              S.              S.  NNP PERSON 
    389   3             Bur             Bur  NNP PERSON 
    390:  4               .               ,    .      O |||persondot

**[by]**: BY should follow a PERSON. (may change NER)

     28   1              Br              BY  NNP      O |||dict,statw
     29:  2         CHARLES       CSLjLRKXS  NNP PERSON |||by,kbe,statw,upp
     30   3              T.              T.  NNP PERSON 
     31:  4           Bones           BRBZS  NNP PERSON |||by,kbe

     60:  1              BY              SY   IN      O |||d,sw,by
     61: 
     62   1           FRANK           FRANK   JJ      O 

    198  10              by              by   IN      O 
    199: 11      Proiesso-r       Professor  NNP      O |||d,sw,by
    200: 12      Coclterell       Cockereii  NNP      O |||ed,kbe

**[etal]**: et al should be followed by a PERSON.

    No example found.

**[lemma]**: If lemma do not appear in dictionary, the word is wrong

    No example found.

**[path]**: If all words in a path to root is frequent, all words on the path is correct

**[path]**: If all words in a path to root is rare, at least one word is wrong

**[path]**: If word Ngram on a path is frequent, these words is correct

    714:  1               [               l   NN      O |||path
    715:  2   Palaeontolngy   pslaeontolosy   NN      O |||ed
    716   3               ,               ,    ,      O 
    717   4             Vol             vol  NNP      O |||swgram
    ...
    735   1             1-2             1-2   CD NUMBER 
    736   2               .               .    .      O 
    737:  3               ]               1  SYM      O |||path

    992   8              of              of   IN      O 
    993   9        holotype        holotype   NN      O 
    994: 10               (               {   NN      O |||statc,path
    995: 11      incomplete      incom-plet   JJ      O |||d,sw,comb
    996  12               )              e)   NN      O |||
    997  13              54              54   CD NUMBER 


**[kbe]**: If we can link a word to an entity in knowledge base, the word is correct

Freebase

    316   6    Plesiechinus    Plesiechinus   NN      O 
    317   7        hawkinsi       Itawkinsi   NN      O |||
    318:  8 Jesionek-Szyma?ska Jesionek-Szymanska   NN      O |||kbe

    949   3      CALIFORNIA      CALIFORNIA  NNP LOCATI 
    950:  4         ACADEMY       ACADEMIA'  NNP      O |||swgram,kbe
    951:  5              OF              OF   IN      O 
    952   6        SCIENCES        SCIENCES  NNP      O 

    1084   5              C.              C.  NNP      O 
    1085:  6     consobrimus     ConsobrN2NS   NN      O |||ed,kbe

    412   1       Barentsia       Barentsia  NNP PERSON 
    413:  2            Iaxa            laaa  NNP PERSON |||ed,kbe
    414:  3     Kirkpatrick     Kirkpatrick  NNP PERSON 

Taxon

    1000   1      HETTANGIAN      HETTANGIAN  NNP   MISC 
    1001:  2      SINEMURIAN    SINEMURIAlai  NNP   MISC |||d,sw,kbe
    1002:  3        TOARCIAN        TOARCIAN  NNP   MISC 

    682   6             the             the   DT      O 
    683   7           names           names  NNS      O 
    684:  8   Scaphiocrinus   Seaphioerinus  NNP      O |||kbe
    685:  9               ,               ,    ,      O 
    686  10       Zeacrinus       Zeaerinus  NNP      O |||sw?
    687  11               ,               ,    ,      O 
    688: 12    Caeliocrinus    Ceelioerinns  NNP      O |||ed,kbe
    689: 13               ,               ,    ,      O 
    690  14            etc.            etc.   FW      O 


Location

    635  45             the             the   DT      O 
    636  46          Sierra          Sierra  NNP LOCATI 
    637: 47          Nevada          Xevada  NNP LOCATI |||d,sw,kbe,kbr

Temporal

    No example found.

**[kbr]**: If we can link two words to two entities and they have a relation, both of them are correct.

    20           Upper          Utlper  NNP      O  |||d,sw$1
    21         Miocene        2fioaene  NNP      O  |||d,sw,kbe$1
    22               ;               O    :      O  |||
    23        Deningen      aijtljaejl  NNP PERSON  |||ed+kbr$Oeningen

*Note: for this example, it is hard to use only KBE to get the last word right since edit distance might be too far. But if we know the relation between Denignen and Upper Miocene we might be able to get it right.*

## Rules to Generate Candidates

**[ed]**: Minimize edit distance to each option, while only generate candidate appearing in corpus / word-gram in corpus

    715:  2   Palaeontolngy   pslaeontolosy   NN      O |||ed

    688: 12    Caeliocrinus    Ceelioerinns  NNP      O |||ed,kbe


    473   3               (               (   CD NUMBER 
    474   4              P.              P.  NNP      O 
    475:  5        echimzta        ectzinat   FW      O |||comb,ed,kbe
    476   6               )              a)   FW      O |||(echinata)

    273   3             has            hila  VBZ      O |||d,sw
    274:  4        ulrezidy         slreadv   JJ      O |||ed,swgram
    275   5            been            been  VBN      O 

    688  43            both           both.   CC      O |||rmchar
    689  44             the             the   DT      O 
    690  45       parasitic       parasitic   JJ      O 
    691: 46             end             aud   NN      O |||ed,swgram,path

**[edrule]**: Weighted edit distance: some of the "edits" have small weights:

     34:  2            ?rst           first   JJ      O |||d,sw,edrule

    919: 14            ?oor           floor   NN      O |||d,sw,edrule

    782: 19   identi?cation   identificatio   NN      O |||edrule,comb,seg
    783  20               .              n.    .      O |||

    178   6         clearly         cfearfy   RB      O |||d,sw
    179:  7          de?ned          degned   JJ      O |||edrule
    180:  8         species         species  NNS      O 

**[comb]**: Combine words to generate new candidate if they are in a same box

         3               .               A    .      O  |||dot

         1               e               m   LS      O  |||
         2               '               e   ''      O  |||
         3         Americo           rican  NNP      O  |||ed,kbe
         4               .                    .      O  

    684: 15    Philadelphia    Philadel-phi  NNP LOCATI |||comb,seg
    685: 16               ,              a,    ,      O |||

    
**[seg]**: segment words to match dictionary / corpus

**[seg]**: segment Tesseract words by '-'

**[seg]**: segment words by removing any letter

    655: 19           ofour           ofour   NN      O |||seg

    657  21         ofthese         ofthese   NN      O |||seg

    680: 31   the/southwest    thesouthwest   VB      O |||seg

    821:  3     placesthese    places.these   NN      O |||seg

    221: 17           is125           is125   CD NUMBER |||seg,charuni

    687: 42       to-derive        Ioderive   JJ      O |||seg,d,sw

**[rmchar]**: Remove rare characters

    461: 20       different      dif-ferent   JJ      O |||rmchar

    281: 30     bifurcating    bifur-cating  VBG      O |||rmchar

    696: 10          paperi          paper'   NN      O |||rmchar

    876: 35   d1Stinguished   dis-tinguishe  VBN      O |||comb,upp,rmchar
    877: 36               ,              d,    ,      O |||
