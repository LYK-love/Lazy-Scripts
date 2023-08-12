short_AA = {
                    'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
                    'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
                    'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
                    'ALA': 'A', 'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'
                    }
long_AA = {value:key for key,value in short_AA.items()}

RNA_codon_table = {
# Second Base
#UCAG
#U
'UUU': 'Phe', 'UCU': 'Ser', 'UAU': 'Tyr', 'UGU': 'Cys',
'UUC': 'Phe', 'UCC': 'Ser', 'UAC': 'Tyr', 'UGC': 'Cys',
'UUA': 'Leu', 'UCA': 'Ser', 'UAA': '---', 'UGA': '---',
'UUG': 'Leu', 'UCG': 'Ser', 'UAG': '---', 'UGG': 'Trp',
#C
'CUU': 'Leu', 'CCU': 'Pro', 'CAU': 'His', 'CGU': 'Arg',
'CUC': 'Leu', 'CCC': 'Pro', 'CAC': 'His', 'CGC': 'Arg',
'CUA': 'Leu', 'CCA': 'Pro', 'CAA': 'Gln', 'CGA': 'Arg',
'CUG': 'Leu', 'CCG': 'Pro', 'CAG': 'Gln', 'CGG': 'Arg',
#A
'AUU': 'Ile', 'ACU': 'Thr', 'AAU': 'Asn', 'AGU': 'Ser',
'AUC': 'Ile', 'ACC': 'Thr', 'AAC': 'Asn', 'AGC': 'Ser',
'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg',
'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg',
#G
'GUU': 'Val', 'GCU': 'Ala', 'GAU': 'Asp', 'GGU': 'Gly',
'GUC': 'Val', 'GCC': 'Ala', 'GAC': 'Asp', 'GGC': 'Gly',
'GUA': 'Val', 'GCA': 'Ala', 'GAA': 'Glu', 'GGA': 'Gly',
'GUG': 'Val', 'GCG': 'Ala', 'GAG': 'Glu', 'GGG': 'Gly'
}

dnaCodonTable = {key.replace('U','T'):value for key, value in RNA_codon_table.items()}
def main():

    amino = input("\n Enter Cobon or Amino Acide code:")
    if(amino.islower()):
        amino = amino.upper()

    if len(amino) == 1:
        if long_AA.get(amino):
            print("You have entered a Acid from the Amino Acid Table, the Amino Acid,", amino, "translates to", long_AA.get(amino))
        else:
            print("Unknown")

    elif dnaCodonTable.get(amino):
        print("You have entered a codon from the DNA Condon Table, The codon", amino, "translates to",  dnaCodonTable.get(amino))
    
    elif RNA_codon_table.get(amino):
        print("You have entered a condon from the RNA Codon Table, The codon", amino, "translates to", RNA_codon_table.get(amino))
    
    elif short_AA.get(amino):
        print("You have entered a Acid from the Amino Acid Table, The Amino Acid,", amino, "translates to", short_AA.get(amino))
    else:
        print("Unknown")

main()