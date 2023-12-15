package RNA;

import Nucleotide.Nucleotide;

import java.util.ArrayList;
import java.util.List;

/**
 *
 * RNA主要以单链形式存在于生物体内
 *
 * 按功能分, RNA可分为作为模板来规定蛋白质编码的mRNA, 和不用于蛋白质编码的non-coding RNA.
 *
 * If the stretch of DNA is transcribed into an RNA.RNA molecule that encodes a protein,
 * the RNA.RNA is termed messenger RNA.RNA (mRNA); the mRNA, in turn, serves as a template for the protein's synthesis through translation.
 *
 * Other stretches of DNA may be transcribed into small non-coding RNAs such as microRNA, transfer RNA.RNA (tRNA), small nucleolar RNA.RNA (snoRNA), small nuclear RNA.RNA (snRNA), or enzymatic RNA.RNA molecules called ribozymes[3] as well as larger non-coding RNAs such as ribosomal RNA.RNA (rRNA), and long non-coding RNA.RNA (lncRNA).
 */
public abstract class RNA {
    List<Nucleotide> nucleotideSequence = new ArrayList<>();
}
