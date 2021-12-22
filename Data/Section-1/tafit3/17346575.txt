import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

public class ProblemB {
    BufferedReader rd;

    ProblemB() throws IOException {
        rd = new BufferedReader(new InputStreamReader(System.in));
        compute();
    }

    private void compute() throws IOException {
        String[] h = split(rd.readLine());
        long n = plong(h[h.length-1]);
        long p = 1;
        long m = 0;
        for(int i=1;i<h.length;i+=2) {
            if(h[i].equals("-")) {
                m++;
            } else if(h[i].equals("+")) {
                p++;
            }
        }
        StringBuilder buf = new StringBuilder();
        if(p == 1) {
            if(m == 0) {
                buf.append(n).append(" = ").append(n);
            }
        } else {
            long right = n + m;
            long left = p;

            long rightM = n + m*n;
            long leftM = p*n;
            long y = -1;
            if(right >= left && right <= leftM) {
                y = right;
            } else if(left >= right && left <= rightM) {
                y = left;
            }
            if(y >= 0) {
                Queue<Long> leftList = new ArrayDeque<>();
                long z = y - p;
                for(int i=0;i<p;i++) {
                    if(z >= n-1) {
                        leftList.add(n);
                        z -= n-1;
                    } else {
                        leftList.add(1+z);
                        z = 0;
                    }
                }

                Queue<Long> rightList = new ArrayDeque<>();
                z = y - n - m;
                for(int i=0;i<m;i++) {
                    if(z >= n-1) {
                        rightList.add(n);
                        z -= n-1;
                    } else {
                        rightList.add(1+z);
                        z = 0;
                    }
                }

                buf = new StringBuilder();
                boolean plus = true;
                for (String g : h) {
                    if (buf.length() > 0) {
                        buf.append(' ');
                    }
                    if (g.equals("?")) {
                        if (plus) {
                            buf.append(leftList.poll());
                        } else {
                            buf.append(rightList.poll());
                        }
                    } else {
                        if (g.equals("+")) {
                            plus = true;
                        } else if (g.equals("-")) {
                            plus = false;
                        }
                        buf.append(g);
                    }
                }
            }
        }
        if(buf.length() == 0) {
            out("Impossible");
        } else {
            out("Possible");
            out(buf);
        }
    }

    private long plong(String s) {
        return Long.parseLong(s);
    }

    public String[] split(String s) {
        if(s == null) {
            return new String[0];
        }
        int n = s.length();
        int start = -1;
        int end = 0;
        int sp = 0;
        boolean lastWhitespace = true;
        for(int i=0;i<n;i++) {
            char c = s.charAt(i);
            if(isWhitespace(c)) {
                lastWhitespace = true;
            } else {
                if(lastWhitespace) {
                    sp++;
                }
                if(start == -1) {
                    start = i;
                }
                end = i;
                lastWhitespace = false;
            }
        }
        if(start == -1) {
            return new String[0];
        }
        String[] res = new String[sp];
        int last = start;
        int x = 0;
        lastWhitespace = true;
        for(int i=start;i<=end;i++) {
            char c = s.charAt(i);
            boolean w = isWhitespace(c);
            if(w && !lastWhitespace) {
                res[x++] = s.substring(last,i);
            } else if(!w && lastWhitespace) {
                last = i;
            }
            lastWhitespace = w;
        }
        res[x] = s.substring(last,end+1);
        return res;
    }

    private boolean isWhitespace(char c) {
        return c==' ' || c=='\t';
    }

    private static void out(Object x) {
        System.out.println(x);
    }

    public static void main(String[] args) throws IOException {
        new ProblemB();
    }
}
