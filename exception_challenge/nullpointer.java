import java.util.*;
import java.io.*;
public class nullpointer {
    public static void main(String ... args) throws IOException {
        HashMap<Integer, String> map = new HashMap<Integer, String>();
        System.out.println(map.get(0).length());
    }
}
