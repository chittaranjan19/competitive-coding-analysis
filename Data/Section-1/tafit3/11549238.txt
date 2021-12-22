import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ProblemB {
    BufferedReader rd;

    ProblemB() throws IOException {
        rd = new BufferedReader(new InputStreamReader(System.in));
        compute();
    }

    private void compute() throws IOException {
        char[] a = rd.readLine().toCharArray();
        char[] b = rd.readLine().toCharArray();
        char[] c = rd.readLine().toCharArray();
        long[] ap = count(a);
        long[] bp = count(b);
        long[] cp = count(c);
        long bg = 0;
        long cg = 0;
        for(long i=0;i<=100000;i++) {
            long m = 100000;
            boolean ok = true;
            for(int j=0;j<26;j++) {
                long x = ap[j]-i*bp[j];
                if(x < 0) {
                    ok = false;
                    break;
                }
                if(cp[j] > 0 && x >= 0) {
                    long r = x / cp[j];
                    m = Math.min(r, m);
                }
            }
            if(ok && i+m > bg+cg) {
                bg = i;
                cg = m;
            }
        }
        StringBuilder buf = new StringBuilder();
        for(int i=0;i<bg;i++) {
            buf.append(b);
        }
        for(int i=0;i<cg;i++) {
            buf.append(c);
        }
        for(int i=0;i<26;i++) {
            char d = (char)('a' + i);
            for(int j=0;j<(ap[i]-bg*bp[i]-cg*cp[i]);j++) {
                buf.append(d);
            }
        }
        out(buf);
    }

    private long[] count(char[] c) {
        long[] r = new long[26];
        for(char z: c) {
            r[z-'a']++;
        }
        return r;
    }

    private static void out(Object x) {
        System.out.println(x);
    }

    public static void main(String[] args) throws IOException {
        new ProblemB();
    }
}
