import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class ProblemB {
    Map<Integer, List<int[]>> dest;

    private ProblemB() throws IOException {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String h = rd.readLine();
        String[] q = h.split("\\s+");
        int a = Integer.parseInt(q[1]);
        int b = Integer.parseInt(q[2]);
        h = rd.readLine();
        q = h.split(" ");
        int n = q.length;
        int[] p = new int[n];
        for(int i=0;i<n;i++) {
            p[i] = Integer.parseInt(q[i]);
        }
        Set<Integer> pset = new HashSet<>();
        for(int x: p) {
            pset.add(x);
        }

        if(a == b) {
            boolean res = true;
            for(int x: p) {
                if(!pset.contains(a-x)) {
                    res = false;
                    break;
                }
            }
            out(res?"YES":"NO");
            if(res) {
                StringBuilder buf = new StringBuilder();
                for(int i=0;i<n;i++) {
                    if(i > 0) {
                        buf.append(' ');
                    }
                    buf.append('0');
                }
                out(buf);
            }
        } else {
            dest = new HashMap<>();
            boolean res = true;
            for(int x: p) {
                boolean aOk = pset.contains(a-x);
                boolean bOk = pset.contains(b-x);
                if(!aOk && !bOk) {
                    res = false;
                    break;
                } else {
                    if(aOk) {
                        addEdgeAndBack(x,a-x,0);
                    }
                    if(bOk) {
                        addEdgeAndBack(x,b-x,1);
                    }
                }
            }
            Set<Integer> aSet = new HashSet<>();
            if(res) {
                for(int x: p) {
                    List<int[]> e = getEdges(x);
                    if(e.size() == 1) {
                        int[] edge = e.get(0);
                        if(edge[0] == x) {
                            if(edge[1] == 0) {
                                aSet.add(x);
                            }
                        } else {
                            boolean odd = true;
                            int curA = edge[1];
                            int prev = x;
                            while(true) {
                                int cur = edge[0];
                                if(curA == 0 && odd) {
                                    aSet.add(prev);
                                    aSet.add(cur);
                                }
                                e = getEdges(cur);
                                if(e.size() == 1) {
                                    if(!odd && e.get(0)[0] != cur) {
                                        res = false;
                                    }
                                    break;
                                }
                                int other = e.get(0)[0] == prev?1:0;
                                edge = e.get(other);
                                if(edge[1] == curA) {
                                    res = false;
                                    break;
                                }
                                curA = 1-curA;
                                prev = cur;
                                odd = !odd;
                            }
                            if(!res) {
                                break;
                            }
                        }
                    }
                }
            }
            out(res?"YES":"NO");
            if(res) {
                StringBuilder buf = new StringBuilder();
                for(int i=0;i<n;i++) {
                    if(i>0) {
                        buf.append(' ');
                    }
                    buf.append(aSet.contains(p[i])?'0':'1');
                }
                out(buf);
            }
        }
    }

    private void addEdgeAndBack(int from, int to, int u) {
        addEdge(from, to, u);
        addEdge(to, from, u);
    }

    private void addEdge(int from, int to, int u) {
        List<int[]> edges = getEdges(from);
        for(int[] edge: edges) {
            if(edge[0] == to) {
                return;
            }
        }
        edges.add(new int[] { to, u });
    }

    private List<int[]> getEdges(int from) {
        List<int[]> ds = dest.get(from);
        if(ds == null) {
            ds = new ArrayList<>();
            dest.put(from, ds);
        }
        return ds;
    }

    private static void out(Object x) {
        System.out.println(x);
    }

    public static void main(String[] args) throws IOException {
        new ProblemB();
    }
}
