import java.util.*;
import java.io.*;

public class zero {
    
    public static void main(String ... args) throws IOException {
        int y = 0;
        int x = 0;
        int z = 1;

        y = x ^ z;
        z = y ^ x;
        x = y ^ z;


        System.out.println(5/0);
        System.out.println(y + z + (x ^ y));
    }
}
