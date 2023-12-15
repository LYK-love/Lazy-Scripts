import RNA.MessageRNA;

import java.util.List;

public class Main {

    /**
     * 转录是将 DNA 片段复制为 RNA 的过程。
     * 转录是指拷贝出一条与DNA链序列完全相
     * 同(除了T→U之外）的RNA单链的过程，是
     * 基因表达的核心步骤。
     *
     * 真核生物合成蛋白质的转录过程以特定的单链DNA片段作为模板，RNA聚合酶作为催化剂，合成前mRNA，前mRNA经进一步加工后转为成熟mRNA。
     * 转录时，DNA分子的双链打开（是否需要DNA解旋酶仍存在争议），在RNA聚合酶的作用下，游离的4种核糖核苷酸按照碱基互补配对原则结合到DNA单链上，
     *
     * 并在RNA聚合酶的作用下形成单链mRNA分子。
     * DNA 片段转录成可以编码蛋白质的RNA 分子，可以产生信使 RNA (mRNA)。
     *
     * DNA 的其他片段被复制到称为非编码 RNA (ncRNA)的 RNA 分子中。
     * mRNA 仅占总 RNA 样本的 1-3%。[1]不到2%的人类基因组可以转录成mRNA（人类基因组#编码与非编码DNA）
     * @param dna
     * @return
     */
    public static RNA transcription(DNA dna)
    {}

    /**
     *
     * @param mRNA
     * @param codon
     * @return
     */
    public static Peptide translation(MessageRNA mRNA, Codon codon)
    {

    }

    /**
     * 判断该DNA序列是由具有蛋白质编码信息. 是的话就称该片段为一组基因.
     * @param dnaSequence
     * @return
     */
    public boolean hasProteinCoding(List<DNA> dnaSequence)
    {
        return true;
    }

    /**
     * 基因表达包括转录（transcription）和
     * 翻译（translation）两个阶段。
     * @return
     */
    public static Protein genePre()
    {

    }
}
