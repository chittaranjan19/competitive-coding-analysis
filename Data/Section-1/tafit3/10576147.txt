import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ProblemA {
    BufferedReader rd;

    private ProblemA() throws IOException {
        rd = new BufferedReader(new InputStreamReader(System.in));
        compute();
    }

    private void compute() throws IOException {
        rd.readLine();
        String s = rd.readLine();
        int n = s.length();
        for(int i=1;i<25;i++) {
            for(int j=0;j<n;j++) {
                if(s.charAt(j)=='*') {
                    int k = j;
                    int p = 0;
                    while(p<4) {
                        k += i;
                        if(k >= n) {
                            break;
                        }
                        if(s.charAt(k) != '*') {
                            break;
                        }
                        p++;
                    }
                    if(p == 4) {
                        out("yes");
                        return;
                    }
                }
            }
        }
        out("no");
    }

    private static void out(Object x) {
        System.out.println(x);
    }

    public static void main(String[] args) throws IOException {
        new ProblemA();
    }
}
