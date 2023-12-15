package Utils;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * DNA的双螺旋结构
 */
public class DoubleHelix<T> {
    private List<T> firstHelix;
    private List<T> secondHelix;

    public DoubleHelix()
    {
        firstHelix = new ArrayList<>();
        secondHelix = new ArrayList<>();
    }

    public ArrayList<T> get(int idx)
    {
        ArrayList<T> list = new ArrayList<>();
        T first = firstHelix.get(idx);
        T second = secondHelix.get(idx);
        list.add(first);
        list.add(second);
        return list;
    }

    public void set(T first, T second, int idx)
    {
        firstHelix.set(idx, first);
        secondHelix.set(idx, second);
    }

    public void append(T first, T second)
    {
        firstHelix.add(first);
        secondHelix.add( second);
    }


}
