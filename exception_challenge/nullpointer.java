import java.util.*;
import java.io.*;
public class nullpointer {
    public static void main(String ... args) throws IOException {
        HashMap<Integer, String> map = new HashMap<Integer, String>();

        map.put(0, "hello");
        map.put(3, "yo");
        map.put(6, "hi");
        map.put(9, "sup");

        for (int key : map.keySet()) {
            map.put(key, map.get(key) + " my friend");
        }

        System.out.println(map.get(0).length());
        System.out.println(map.size());
    }
}
