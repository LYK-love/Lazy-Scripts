import Nucleotide.Nucleotide;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Codon: 三个(组成DNA或RNA的)核苷酸的序列, 被称为密码子.
 * FUnction: Specifies a particular amino acid or acts as a start or stop signal for protein synthesis.
 * A codon is a sequence of three nucleotides in DNA or RNA that
 * 三个单核苷酸形成一组密码子，而每个密码子代表一个氨基酸或停止信号.
 * 因为密码子由三个核苷酸组成，故一共有43=64种密码子。
 * 例如，RNA序列UAGCAAUCC包含了三个密码子：UAG，CAA和UCC。这段RNA编码代表了长度为3个氨基酸的一段蛋白质序列。（DNA也有类似的序列，但是以T代替了U）。
 */
public class Codon {
    private List<Nucleotide> nucleotideSequence;

    public Codon(Nucleotide a, Nucleotide b, Nucleotide c)
    {
        nucleotideSequence = new ArrayList<>(Arrays.asList(a,b,c));
    }

    public Codon(List<Nucleotide> list)
    {
        if(list.size() != 3)
            throw new IllegalArgumentException("The size of the nucleotide sequence must be 3.");

        nucleotideSequence = new ArrayList<>(list);
    }
    public List<Nucleotide> get()
    {
        return nucleotideSequence;
    }
}
