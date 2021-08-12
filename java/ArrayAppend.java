// ArrayAppend.java

import java.util.Arrays;

public class ArrayAppend
{
    public static int[] AppendInt(int[] input_array, int value)
    {
        int[] array = Arrays.copyOf(input_array, input_array.length + 1);
        array[array.length - 1] = value;
        return array;
    }
}

