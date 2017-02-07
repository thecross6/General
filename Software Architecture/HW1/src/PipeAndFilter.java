import java.util.HashSet;
import java.util.Set;

public class PipeAndFilter {
   public static void main(String []args) {
      System.out.println("Hello World");
      Set<String> wordSet = new HashSet<String>();
      wordSet.add("Ass");
      wordSet.add("Shit");
      wordSet.add("Ass");
      System.out.println(wordSet);
   }
} 