import sys, os, re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

sys.path.insert(0, 'tools')
from vedic_brahma_codec import decode_vedic_brahma_chunk

sample_lines = [
    "vdnZefena rhFk± Hkj}kt fu'kke; A",
    "je.kh;a izlÃªkkEcq lUeuq\";euks ;Fkk AA",
    "vUrks ukfLr fiiklk;kLrqfÃŽLrq ijea lq[ke~ A",
    "nsokuka uUnuks nsoks uksnuks osnfufUnuke~ A",
    "fnos nqnko uknsu nkus nkuoufUnu% AA",
    "Â¬ Hkw% Hkqo% Lo% rr~ lforqoZjs.;e~ A",
    "HkxksZ nsoL; /khefg A",
    "f/k;ks ;ks u% izpksn;kr~ AA",
    "u tk;rs fez;rs ok dnkfpÂêkk;a HkwRok Hkfork ok u Hkw;% A",
    "vtks fuR;% 'kkÃŒrksÂ·;a iqjk.kks u gU;rs gU;ekus 'kjhjs AA",
    "loZ/kekZu~ ifjR;T; ekesda 'kj.ka ozt A",
    "vgka Roka loZikisH;ks eks{kf;"
]

for s in sample_lines:
    print("---------------------------------------------")
    print(f"RAW:  {s}")
    dec = decode_vedic_brahma_chunk(s)
    print(f"DEVA: {dec}")
