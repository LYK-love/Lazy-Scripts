可以看到, 两个代码块的代码部分做出了很大的改动, 但是注释部分是相似的. 在很多情况下, 我们需要将这种情况识别为代码-注释的不一致, 但是, 对于这个例子中的情况, 由于注释部分仅仅描述了代码的版权信息, 因此注释部分的不变是正常的. 从这个例子可以看到, 代码的注释有不同种类, 而不同种类的注释的相似并不都代表着注释克隆, 或者说不都代表着对检测和维护代码-注释一致性有益的注释克隆. 本文提出的注释克隆检测方法主要用于代码-注释一致性的检测, 因此有必要对注释进行分类处理, 以获得更好的效果.



* Zhai等人提出的CPC是一个注释分类和注释传播分析工具. CPC根据注释对应的代码粒度(例如类, 方法和声明)以及注释描述的代码方面(例如代码的功能, 代码的实现细节, 代码的使用方式)进行分类. 本文提出的注释克隆检测技术结合了CPC的分类法, 我们只在方法层面进行检测. 这个分类法的好处是它在处理注释的同时考虑了程序的语义, 因此可以更好地揭示程序中的错误. 



* 我们使用CPC的分类法处理我们的数据集, 对注释进行分类. 由于我们的方法只关注方法层面的注释, 因此我们只选择CPC在方法层面的分类法. 由于CPC不同粒度的分类法是相似的, 它们都具有六个类别, 只是相同类别在不同粒度下的含义有细微区别, 因此很容易将本方法扩展到其它的代码粒度. 此外, CPC在语句层面处理注释, 这和我们将注释切割成语句级别的子注释并进行分类的思想是一致的. 