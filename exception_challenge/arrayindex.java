import java.util.*;
import java.io.*;

public class arrayindex {

    static class Number {
        protected int data;

        Number(int x) {
            data = x;
        }

        void messUp() {
            this.data = (this.data + 7) % 3;
        }

        public String toString() {
            return String.format("NUMBER: %d", this.data);
        }
    }

    public static void main(String ... args) throws IOException {
        int[] array = new int[12];

        System.out.println(array[13]);

        Number mynumber = new Number(0);
        mynumber.messUp();
        mynumber.messUp();
        System.out.println(mynumber);
    }
}
